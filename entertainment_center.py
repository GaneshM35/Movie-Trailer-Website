# coding=utf-8

"""
Module to display movie object, attributes and instances
main Python script to run
"""

import media
import fresh_tomatoes


# Movie Objects
nanban = media.MovieTrailer(
    "Nanban",
	'''Nanban (English: Friend) is a 2012 Indian 
    Tamil coming of age comedy film directed by Shankar.''',
    "https://upload.wikimedia.org/wikipedia/en/thumb/3/33/Nanban_film.jpg/220px-Nanban_film.jpg",  # noqa
    "https://www.youtube.com/watch?v=i9lhWe3Yt8c")

shahjahan = media.MovieTrailer(
    "Shahjahan",
	'''The film is about a man Ashok (Vijay) who 
    helps lovers. He understands the psychology of 
    women and knows how to catch their heart.''',
    "http://www.5starmusiq.com/movieimages/Tamil/S/2001/Shahjahan_B.jpg",  # noqa
    "https://www.youtube.com/watch?v=gZIIFjS_Il0")

saattai = media.MovieTrailer(
    "Saattai",
    '''Saattai (English : Whip) is a 2012 Indian 
    Tamil drama film written and directed by 
    M. Anbazhagan.''',
    "https://upload.wikimedia.org/wikipedia/en/6/6a/Saattai_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=f63mbBDGcXU")

remo = media.MovieTrailer(
    "Remo",
    '''Remo is a 2016 Indian Tamil-language romantic 
    comedy film produced by R. D. Raja, written and	
    directed by Bakkiyaraj Kannan. It stars Sivakarthikeyan	
    and Keerthy Suresh in the leading roles.''',
    "https://upload.wikimedia.org/wikipedia/en/thumb/e/e0/Remo_Sivakarthikeyan_poster.jpg/220px-Remo_Sivakarthikeyan_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=GEB4qrrWIgs")

thani_oruvan = media.MovieTrailer(
    "Thani Oruvan",
    '''Thani Oruvan (English: The Lone One) is an Indian 
    2015 Tamil-language crime thriller film directed 
    by Mohan Raja and written by Subha.''',
    "https://upload.wikimedia.org/wikipedia/en/thumb/f/f1/Thani_Oruvan.jpg/220px-Thani_Oruvan.jpg",  # noqa
    "https://www.youtube.com/watch?v=r5Lih8rKd6k")

thuppakki = media.MovieTrailer(
    "Thuppakki",
    '''Thuppakki (English: The Gun) is a 2012 Indian 
    Tamil-language action film written and directed	
    by AR Murugadoss. It features Vijay and 
    Kajal Aggarwal in the lead roles.''',
    "https://upload.wikimedia.org/wikipedia/en/thumb/b/be/Thuppakki_poster.jpg/220px-Thuppakki_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=A1AGs0qeY0U")

# Creating list for movie objects
movies = [nanban, shahjahan, saattai, remo, thani_oruvan, thuppakki]
fresh_tomatoes.open_movies_page(movies)
