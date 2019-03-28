import pandas as pd # pandas is a data manipulation library
import numpy as np #provides numerical arrays and functions to manipulate the arrays efficiently
import random
import matplotlib.pyplot as plt # data visualization library
from wordcloud import WordCloud, STOPWORDS #used to generate world cloud

class totalratingclass():
    def totalratingfn(self):
        data= pd.read_csv('~/Desktop/movielens/movies.csv')
        ratings_data=pd.read_csv('~/Desktop/movielens/ratings.csv',sep=',')
#        tags_data=pd.read_csv('~/Desktop/movielens/tags.csv',sep=',')

        movie_data_ratings_data=data.merge(ratings_data,on = 'movieId',how = 'inner')
#        unique_genre=data['genres'].unique().tolist()

        most_rated = movie_data_ratings_data.groupby('title').size().sort_values(ascending=False)[:10]
        #print(most_rated.head(25))

        rate = list()
        count = 0

        for movieTitle, ratings in most_rated.iteritems():           
            value = {
                "title" : movieTitle,
               "rating" : ratings,               
            }           
            rate.append(value)
            if count == 10:
                break
            count += 1

        print("rate \n" , rate)
        return(rate)