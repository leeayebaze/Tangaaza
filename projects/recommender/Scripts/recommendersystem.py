#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 10:07:56 2019

@author: ayebaze
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('dark')
#matplotlib inline

#this is for ploting of the graph 

##from IPython import get_ipython
##get_ipython().run_line_magic('matplotlib', 'inline')


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
#pd.set_option('display.max_columns', True)

ratings_data = pd.read_csv("/home/ayebaze/MovieLens/ratings.csv")
ratings_data.head()

movie_names = pd.read_csv("/home/ayebaze/MovieLens/movies.csv")
movie_names.head()

movie_data = pd.merge(ratings_data, movie_names, on='movieId')
#movie_data.head()

#movie_data.groupby('title')['rating'].mean().head()

movie_data.groupby('title')['rating'].mean().sort_values(ascending=False).head()
#movie_data.head()

movie_data.groupby('title')['rating'].count().sort_values(ascending=False).head()
#print(movie_data)

ratings_mean_count = pd.DataFrame(movie_data.groupby('title')['rating'].mean())
ratings_mean_count['rating_counts'] = pd.DataFrame(movie_data.groupby('title')['rating'].count()) 
ratings_mean_count.head()
#print(ratings_mean_count)

#plt.figure(figsize=(8,6))  
#plt.rcParams['patch.force_edgecolor'] = True  
#ratings_mean_count['rating_counts'].hist(bins=50) 

#The Output shows that most movies recieved less than 50 ratings while those with more than 100 is very low
#--------------------------------------------------------------------------------------

##plt.figure(figsize=(8,6))  
##plt.rcParams['patch.force_edgecolor'] = True  
##ratings_mean_count['rating'].hist(bins=50) 

#integer values have taller bars than floating values people assign ratings as 1,2,3,4,5 and few autliers
#Data has weak mean normal distribution with a mean of 3.5
#----------------------------------------------------------------------------------------

##plt.figure(figsize=(8,6))  
##plt.rcParams['patch.force_edgecolor'] = True  
##sns.jointplot(x='rating', y='rating_counts', data=ratings_mean_count, alpha=0.4)  

#The graph shows that movies with higher average ratings actually have more no of ratings compared with movies with lower average ratings

user_movie_rating = movie_data.pivot_table(index='userId', columns='title', values='rating')  
user_movie_rating.head()
#print(user_movie_rating.head())

#The matrix of the Movie titles and the corresponding user ratings.
#-----------------------------------------------------------------------------------------

forrest_gump_ratings = user_movie_rating['Forrest Gump (1994)']
forrest_gump_ratings.head()
#print(forrest_gump_ratings)

#The ratings for the pandas series.

movies_like_forest_gump = user_movie_rating.corrwith(forrest_gump_ratings)

corr_forrest_gump = pd.DataFrame(movies_like_forest_gump, columns=['Correlation'])  
corr_forrest_gump.dropna(inplace=True) 
corr_forrest_gump.head()  

corr_forrest_gump.sort_values('Correlation', ascending=False).head(10)  
#print(corr_forrest_gump)

#The movies that correlate with Forest Gump are very few
#There is a challenge of sorting the values.

corr_forrest_gump = corr_forrest_gump.join(ratings_mean_count['rating_counts'])
#print(corr_forrest_gump.head()) 
corr_forrest_gump[corr_forrest_gump ['rating_counts']>50].sort_values('Correlation', ascending=False).head()
#The line above is not working to find the ratings whic are >50

print(corr_forrest_gump.head())

#To solve the problem above we retrieve only those correlated movies that have at least more than 50 ratings

#https://stackabuse.com/creating-a-simple-recommender-system-in-python-using-pandas/
