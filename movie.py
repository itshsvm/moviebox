import json
import random
import requests

from config import API_TOKEN

def get_all_movie(show_page=False, this_page=False):
    pages = random.randint(1, 500)

    url = f"https://api.themoviedb.org/3/movie/popular?language=en-US&page={pages}"
    headers = {"accept": "application/json", "Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(url, headers=headers)
    data = json.loads(response.content)

    print(data['page'])

    film_data = []
    output = dict()
    for (k, v) in data.items():
        film_data.append(v)
        data = filter(lambda x: type(x) != int, film_data)
        for i in data:
            for j in i:
                output[j['title']] = [j['poster_path'], j['overview'], j['release_date'], j['vote_average']] 
    
    if show_page == True:
        return output, pages

    return output


def get_star_rating(vote_average):
    stars = vote_average / 2
    full = int(stars)
    half = stars - full >= 0.50
    star_str = '⭐' * full
    if half:
        star_str += '☆'  # type: ignore
    
    return  star_str

def get_movie_by_genre(genre):
    url = f"https://api.themoviedb.org/3/discover/movie?with_genres={genre}&language=en-US"
    headers = {"accept": "application/json", "Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(url, headers=headers)
    data = json.loads(response.content)
    
    film_data = []
    output = dict()
    for (k, v) in data.items():
        film_data.append(v)
        data = filter(lambda x: type(x) != int, film_data)
        for i in data:
            for j in i:
                output[j['title']] = [j['poster_path'], j['overview'], j['release_date'], j['vote_average']]
    
    return output


def build_caption(film):
    caption = f"""
Name: {film[0]}

Overview:
{film[2]}

Release Date:
{film[3]}

Vote Average: {get_star_rating(film[4])}

If you want to see another movie, just type /movie again.
    """
    return caption
