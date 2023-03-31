"""
Vincent Le
CSE 163

This final project focuses on analyzing data scraped from MyAnimeList.net. It
analyzes two CSV files, one with data on each anime entry the website contains,
and one with data on scores that users have given to shows they completed. Two
charts are created from this data analyzing anime popularity by genre, and 
anime score distribution by genre. In addition to this, it creates a 
recommender system using machine learning to recommend a given number of shows
based on a user input.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from data_processing import process_data
import plots
from recommender import Recommender

# File paths for data sets
ANIME_PATH = 'anime.csv'
RATINGS_PATH = 'rating_complete.csv'


def main():
    # Testing using first 20 rows.
    #anime, ratings = process_data(ANIME_PATH, RATINGS_PATH, 20)

    # Testing plots using smaller datasets.
    #plots.most_pop_genres(anime, 'test_pop_genres.png')
    #plots.genre_distribution(anime, 'test_genre_dist.png')

    anime, ratings = process_data(ANIME_PATH, RATINGS_PATH)

    plots.most_pop_genres(anime, 'pop_genres.png')
    plots.genre_distribution(anime, 'genre_dist.png')

    # Testing using 1000000 rows of user ratings and 6 recommendations.
    #test = Recommender(anime, ratings, 1000000)
    #entry = input('Enter an anime: ')
    #test.recommend(entry, 6)

    recommender = Recommender(anime, ratings, 5000000)
    entry = input('Enter an anime: ')
    recommender.recommend(entry)


if __name__ == '__main__':
    main()