#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 19:10:14 2019

@author: ayebaze
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

class Recommender2Class():
    def recommender2Fn(self):
        #column headers for the dataset
        data_cols = ['user id','movie id','rating','timestamp']
        item_cols = ['movie id','movie title','release date','video release date','IMDb URL','unknown','Action','Adventure','Animation','Childrens','Comedy','Crime','Documentary','Drama','Fantasy','Film-Noir','Horror','Musical','Mystery','Romance ','Sci-Fi','Thriller','War' ,'Western']
        user_cols = ['user id','age','gender','occupation','zip code']

        #importing the data files onto dataframes 
        users = pd.read_csv('~/Desktop/ml-100k/u.user', sep='|', names=user_cols, encoding='latin-1')
        item = pd.read_csv('~/Desktop/ml-100k/u.item', sep='|', names=item_cols, encoding='latin-1')
        data = pd.read_csv('~/Desktop/ml-100k/u.data', sep='\t', names=data_cols, encoding='latin-1')

        utrain = (data.sort_values('user id'))[:99832]
        #print(utrain.tail())
        utest = (data.sort_values('user id'))[99833:]
        #print(utest.head())

        utrain = utrain.as_matrix(columns = ['user id', 'movie id', 'rating'])
        #print(utrain)

        utest = utest.as_matrix(columns = ['user id', 'movie id', 'rating'])
        #print(utest)

        users_list = []
        for i in range(1,943):
            userList = []
            for j in range(0,len(utrain)):
                if utrain[j][0] == i:
                    userList.append(utrain[j])    
                else:
                    break
            utrain = utrain[j:]
            users_list.append(userList) 
            
        #print(len(users_list))

        def EucledianScore(train_user, test_user):
            sum = 0
            for i in test_user:
                score = 0
                for j in train_user:
                    if(int(i[1]) == int(j[1])):
                        score= ((float(i[2])-float(j[2]))*(float(i[2])-float(j[2])))
                sum = sum + score            
            return(math.sqrt(sum))            

        score_list = []               
        for i in range(0,942):
            score_list.append([i+1,EucledianScore(users_list[i], utest)])
            score = pd.DataFrame(score_list, columns = ['user id','Eucledian Score'])
        score = score.sort_values(by = 'Eucledian Score')
        #print(score)
        score_matrix = score.as_matrix()

        user= int(score_matrix[0][0])
        common_list = []
        full_list = []
        for i in utest:
            for j in users_list[user-1]:
                if(int(i[1])== int(j[1])):
                    common_list.append(int(j[1]))
                full_list.append(j[1])

        common_list = set(common_list)  
        full_list = set(full_list)
        recommendation = full_list.difference(common_list)

        item_list = (((pd.merge(item,data).sort_values(by = 'movie id')).groupby('movie title')))['movie id', 'movie title', 'rating']
        item_list = item_list.mean()
        item_list['movie title'] = item_list.index
        item_list = item_list.as_matrix()

        recommendation_list = []
        for i in recommendation:
            recommendation_list.append(item_list[i-1])
            
        recommendation = (pd.DataFrame(recommendation_list,columns = ['movie id','mean rating' ,'movie title'])).sort_values(by = 'mean rating', ascending = False)
        #return(recommendation)
        #print(recommendation[['mean rating','movie title']])

        recommendationsystem = list()
        count = 0

        for index, row in recommendation.iterrows():
            # print(index)
            # print("Title %s " % row['title'])
            # print(" - Rating %s " % row['rating'])
            # print(" - Total ratings %s \n" % row['total ratings'])
            value = {
                "movieid" : row['movie id'],
                "meanrating" : row['mean rating'],
                "movietitle" : row['movie title'],

            }
            # print(" Value \n" , value)
            recommendationsystem.append(value)
            if count == 5:
                break
            count += 1

        print("recommendation \n" , recommendationsystem)
        return(recommendationsystem)

#        return(recommendation[['mean rating','movie title']])    
        #https://acodeforthought.wordpress.com/2016/12/29/building-a-recommender-system-on-user-user-collaborative-filtering-movielens-dataset/