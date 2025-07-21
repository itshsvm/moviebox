import random
from pickledb import PickleDB



db = PickleDB("cache.db")


def reset_user_clicks(user_id):
    db.set(f"{user_id}", 0)



def get_user_clicks(user_id):
    user = db.get(f"{user_id}")
    return user


def increment_user_clicks(user_id):
    current_clicks = db.get(f"{user_id}") or 0
    db.set(f"{user_id}", current_clicks + 1)


def set_user_clicks(user_id, clicks):
    db.set(f"{user_id}", clicks)
    return clicks


def not_exists(user_id):
    if db.get(f"{user_id}") is None:
        db.set(f"{user_id}", 0)



def get_clicks(user_id):
    clicks = db.get(f"{user_id}")
    if clicks is None:
        return 0
    return clicks


def get_random_film(films, last):
    title = [fl for fl in films.keys()]

    if len(set(title)) <= 1:
        return title[0]
    
    while True:
        selected = random.choice(title)
        if selected != last:
            return selected, *films[selected]
        
        
def build_picture(name):
    return f'https://image.tmdb.org/t/p/w500/{name[1]}'