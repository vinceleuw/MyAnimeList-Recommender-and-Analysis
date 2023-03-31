"""
Vincent le
CSE 163

This file implements an initializer to create a recommender object, used to
recommend animes based off of an inputted show. Also implements the recommend
function used to output the recommendations. Uses a Nearest Neighbors algorithm
to calculate the most similar anime.
"""
import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors


class Recommender:
    """
    Initializes a Recommender object used to create the Nearest Neighbors
    machine learning model to create recommendations.
    """
    def __init__(self, anime, ratings, rows=5000000):
        """
        Initializes an object given two data frames containing the anime
        entries, and user ratings, as well as another parameter to tell how
        many rows of the user ratings data frame will be used.
        """
        self._pivot = None
        self._model = None

        anime_info = anime[['MAL_ID', 'Name']]
        user_ratings = ratings.head(rows).merge(anime_info, left_on='MAL_ID',
                                                right_on='MAL_ID', how="left")

        # Filters data for users who have completed more than 150 shows, and animes
        # that have more that 250 users completed.
        user_counts = user_ratings['user_id'].value_counts()
        anime_counts = user_ratings['MAL_ID'].value_counts()
        filtered_counts = user_ratings[user_ratings['user_id'].
            isin(user_counts[user_counts >= 150].
            index)]
        filtered_counts = user_ratings[user_ratings['MAL_ID'].
            isin(anime_counts[anime_counts >= 250].
            index)]

        rating_counts = (filtered_counts.
            groupby(by='Name').
            count().
            reset_index()[['Name', 'rating']]
        )

        user_ratings = filtered_counts.merge(rating_counts, left_on='Name',
                               right_on='Name', how='left')

        self._pivot = user_ratings.pivot_table(index='Name', columns='user_id',
                                               values='rating_y').fillna(0)

        pivot_matrix = csr_matrix(self._pivot.values)
        self._model = NearestNeighbors(metric="cosine", algorithm="brute")
        self._model.fit(pivot_matrix)


    def recommend(self, entry, n=11):
        """
        Function used to output the recommendations based off a given anime
        entry. Also takes in another parameter used to decide the number of
        recommendations given.
        """
        query = self._pivot.loc[entry].values.reshape(1, -1)
        distance, suggestions = self._model.kneighbors(query, n_neighbors=n)

        for i, dist in enumerate(distance.flatten()):
            if i == 0:
                print('Recommendations for: ',
                      self._pivot.index[suggestions.flatten()[i]])
            else:
                print('{}: {}, {} distance'.format(
                      i,
                      self._pivot.index[suggestions.flatten()[i]],
                      distance.flatten()[i])
                      )