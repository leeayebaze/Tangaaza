#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 14:59:30 2019

@author: ayebaze
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class RecommenderClass():

    def recommenderFn(self):
        #column headers for the dataset
        data_cols = ['user id','movie id','rating','timestamp']
        item_cols = ['movie id','movie title','release date',
        'video release date','IMDb URL','unknown','Action',
        'Adventure','Animation','Childrens','Comedy','Crime',
        'Documentary','Drama','Fantasy','Film-Noir','Horror',
        'Musical','Mystery','Romance ','Sci-Fi','Thriller',
        'War' ,'Western']
        user_cols = ['user id','age','gender','occupation',
        'zip code']

        #importing the data files onto dataframes
        users = pd.read_csv('~/Desktop/ml-100k/u.user', sep='|',
        names=user_cols, encoding='latin-1')
        item = pd.read_csv('~/Desktop/ml-100k/u.item', sep='|',
        names=item_cols, encoding='latin-1')
        data = pd.read_csv('~/Desktop/ml-100k/u.data', sep='\t',
        names=data_cols, encoding='latin-1')

        #printing the head of these dataframes
        #print(users.head())
        #print(users.tail(100))
        #print(item.head())
        #print(data.head())

        #print(users.info())
        #print(item.info())
        #print(data.info())

        #Create one data frame from the three
        dataset = pd.merge(pd.merge(item, data),users)
        #print(dataset.head(1000))

        #Next we use groupby to group the movies by their titles. 
        #Then we use the size function to returns the total number of entries under each movie title. 
        #This will help us get the number of people who rated the movie/ the number of ratings.
        ratings_total = dataset.groupby('movie title').size()
        #print(ratings_total.head())

        ratings_mean = (dataset.groupby('movie title'))['movie title','rating'].mean()
        #print(ratings_mean.head())

        ratings_total = pd.DataFrame({'title':ratings_total.index,
        'total ratings': ratings_total.values})
        ratings_mean['title'] = ratings_mean.index
        print(ratings_mean.index)

        #Now we head for the merging part. Now we sort the values by the total rating and this helps us sort the data frame by the number of people who viewed the movie
        final = pd.merge(ratings_mean, ratings_total).sort_values(by = 'total ratings',
        ascending= False)
        #print(final.head())

        #We need to look at the basic characteristics of the data to determine the minimum cutoff of total ratings. 
        #print(final.describe())

        #I see the 75th percentile is at around 80.I decide to set the cutoff at 100. With a bit of slicing I am able to ascertain that the 340th element has a total rating of approximately 100. So next try to cut off the remaining data. Then we sort the new Data frame with respect to the mean ratings. 
        final = final[:300].sort_values(by = 'rating',ascending = False)
        
        movies = list()
        count = 0

        for index, row in final.iterrows():
            # print(index)
            # print("Title %s " % row['title'])
            # print(" - Rating %s " % row['rating'])
            # print(" - Total ratings %s \n" % row['total ratings'])
            value = {
                "title" : row['title'],
                "rating" : row['rating'],
                "total" : row['total ratings'],
            }
            # print(" Value \n" , value)
            movies.append(value)
            if count == 5:
                break
            count += 1

        print("movies \n" , movies)
        return(movies)
        # print("Total %s" % final.get('total ratings'))
        # lineID = 0
        # logdata = {}
        # for line in final:            
        #     lineData = nltk.word_tokenize(line)
        #     logdata[lineID] = lineData
        #     lineID += 1

        # for line in final.get("total ratings"):       
        #     print("line id %s" % line)     

        # for line in final.get('rating'):       
        #     print("Current line %s" % line)    
        # return(logdata)
        #print(final.head())


        #https://acodeforthought.wordpress.com/2016/12/26/building-a-simple-recommender-system-with-movie-lens-data-set/