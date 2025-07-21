import threading
import telebot
from utils import *
from config import TOKEN
from telebot import types
from cache import CacheManager
from movie import build_caption, get_all_movie

bot = telebot.TeleBot(TOKEN)

MAX_CLICKS = 3

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Welcome to the MovieBox! Use /movie to get a random movie or /genre <genre name> to get movies by genre.")



@bot.message_handler(commands=['movie'])
def movie(message):
    user_id = message.from_user.id
    timer = threading.Timer(180.0, reset_user_clicks, args=[user_id])
    timer.start()
    name = get_random_film(get_all_movie(), last=None)

    caption = build_caption(name)
    
    keyboard = types.InlineKeyboardMarkup()
    next_movie = types.InlineKeyboardButton("Next Movie 🎬", callback_data="next_movie")
    keyboard.add(next_movie)

    bot.send_photo(chat_id=message.chat.id, photo=build_picture(name), caption=caption, reply_markup=keyboard)

@bot.message_handler(commands=['genre'])
def genre(message):
    genre = message.text.split()[1] if len(message.text.split()) > 1 else None
    if not genre:
        bot.reply_to(message, "Please specify a genre.")
        return

    films = get_all_movie()
    selected_film = get_random_film(films, last=None)

    caption = build_caption(selected_film)
    keyboard = types.InlineKeyboardMarkup()
    next_movie = types.InlineKeyboardButton("Next Movie 🎬", callback_data="next_movie")

    keyboard.add(next_movie)

    bot.send_photo(
        chat_id=message.chat.id,
        photo=build_picture(selected_film),
        caption=caption,
        reply_markup=keyboard
    )

@bot.callback_query_handler(func=lambda call: call.data == "next_movie")
def next_movie_callback(call):

    user_id = call.from_user.id


    not_exists(user_id)

    clicks = get_clicks(user_id)
    

    if clicks >= MAX_CLICKS:
        bot.answer_callback_query(call.id, "🚫 You've reached the 3-movie limit. Please try again in a few minutes.")
        return
    

    increment_user_clicks(user_id)

    films = get_all_movie()
    selected_film = get_random_film(films, last=None)
    caption = build_caption(selected_film)
    


    bot.edit_message_media(types.InputMediaPhoto(
        media=build_picture(selected_film),
        caption=caption
    ), chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=call.message.reply_markup)


    


if __name__ == "__main__":
    CacheManager().run()
    timer = threading.Timer(180.0, CacheManager().clear, args=[])
    timer.start()


    print("Bot is running...")
    bot.infinity_polling()
