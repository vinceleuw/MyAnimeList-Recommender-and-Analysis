"""
Vincent Le
CSE 163

This file is used for the preprocessing of data before analysis.
"""
import pandas as pd
import numpy as np


def process_data(anime_data, rating_data, nrows=None):
    """
    Function that takes in the anime and ratings datasets and cleans
    and manipulates the data, keeping only certain columns and removing
    NA values.
    """
    anime = pd.read_csv(anime_data, nrows=nrows)
    ratings = pd.read_csv(rating_data, nrows=nrows)

    interest = ['MAL_ID', 'Name', 'Score', 'Genres', 'Type',
                'Episodes', 'Studios', 'Source', 'Rating', 'Members']
    anime_filtered = anime[interest]
    anime_filtered = anime_filtered.replace('Unknown', np.nan)
    anime_filtered = anime_filtered.dropna()

    for col in ['Genres', 'Studios']:
        anime_filtered[col] = anime_filtered[col].str.split(', ')

    ratings = ratings.rename(columns={'anime_id': 'MAL_ID'})
    
    return anime_filtered, ratings