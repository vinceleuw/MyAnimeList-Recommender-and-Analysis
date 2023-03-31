"""
Vincent Le
CSE 163

This file implements the functions used to plot and analyze data from the
given data sets on anime. Creates a pie chart showing general popularity
of anime based on genres, and creates another chart of distribution of
anime scores by genre.
"""
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict


def most_pop_genres(anime, filename):
    """
    Function used to create a plot of the most popular genres of animes. Takes
    in the dataset of MyAnimeList entries as a parameter.
    """
    # Extracts total number of members per genre.
    genre_members = defaultdict(int)
    for members, genres in zip(anime['Members'], anime['Genres']):
        for genre in genres:
            genre_members[genre] += members
    
    # Sorts by descending order.
    sorted_members = sorted(genre_members.items(),
                            key=lambda x: x[1], reverse=True)

    # Creates labels and plots data as a pie chart.
    labels = [genre[0] for genre in sorted_members] 
    member_pct = [members[1] for members in sorted_members]

    fig, ax = plt.subplots(figsize=(20, 20))
    ax.pie(member_pct)
    plt.legend(labels)
    plt.title('Most Popular Anime Genres by Members', fontsize=25)
    plt.savefig(filename)


def genre_distribution(anime, filename):
    """
    Function used to create a plot of the distribution of scores between each
    genre. Takes in the dataset of MyAnimeList entries as a parameter
    """
    # Extracts individual scores for each genre.
    genre_scores = defaultdict(list)
    for scores, genres in zip(anime['Score'], anime['Genres']):
        for s in genres:
            genre_scores[s].append(float(scores))
    
    # Sorts genres by average score.
    sorted_scores = sorted(genre_scores.items(),
                           key=lambda x: sum(x[1]) / len(x[1]))

    scores = [x[1] for x in sorted_scores]
    labels = [x[0] for x in sorted_scores]

    # Creates cat plot boxplot to visualize distribution of scores.
    fig, [ax1, ax2] = plt.subplots(2, figsize=(20, 25))
    ax1.boxplot(scores, vert=False)
    ax1.set_yticklabels(labels, fontsize=14)
    ax1.set_xlabel('Scores', fontsize=20)
    ax1.set_ylabel('Genres', fontsize=20)
    ax1.set_title('Distribution of Scores in Genre', fontsize=28)

    counts = [len(x[1]) for x in sorted_scores]

    # Creates another bar chart to visualize number of shows per genre.
    ax2.bar(labels, counts, width=0.8, align='center')
    ax2.set_xticklabels(labels=labels, rotation=90)
    ax2.set_ylabel('Number of Anime', fontsize=20)
    ax2.set_xlabel('Genre', fontsize=20)
    ax2.set_title('Count of Animes in Genre', fontsize=28)

    plt.savefig(filename)