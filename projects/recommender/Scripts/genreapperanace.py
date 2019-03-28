import pandas as pd # pandas is a data manipulation library
import numpy as np #provides numerical arrays and functions to manipulate the arrays efficiently
import random
import matplotlib.pyplot as plt # data visualization library
from wordcloud import WordCloud, STOPWORDS #used to generate world cloud

data= pd.read_csv('~/Desktop/movielens/movies.csv')
ratings_data=pd.read_csv('~/Desktop/movielens/ratings.csv',sep=',')
tags_data=pd.read_csv('~/Desktop/movielens/tags.csv',sep=',')

class genreappearanceclass():
    def genreappearancefn(self):
        #define a function that counts the number of times each genre appear:
        def count_word(df, ref_col, liste):
            keyword_count = dict()
            for s in liste: keyword_count[s] = 0
            for liste_keywords in df[ref_col].str.split('|'):
                if type(liste_keywords) == float and pd.isnull(liste_keywords): continue
                for s in liste_keywords: 
                    if pd.notnull(s): keyword_count[s] += 1
            # convert the dictionary in a list to sort the keywords  by frequency
            keyword_occurences = []
            for k,v in keyword_count.items():
                keyword_occurences.append([k,v])
            keyword_occurences.sort(key = lambda x:x[1], reverse = True)
            return keyword_occurences, keyword_count

        #here we  make census of the genres:
        genre_labels = set()
        for s in data['genres'].str.split('|').values:
            genre_labels = genre_labels.union(set(s))
            
        #counting how many times each of genres occur:
        keyword_occurences, dum = count_word(data, 'genres', genre_labels)
#        print(keyword_occurences)
        Totalgenre = list()
        count = 0

        for moviegenres, genrelabels in keyword_occurences.copy():           
            value = {
                "genres" : moviegenres,
               "genre_labels" : genrelabels,               
            }           
            Totalgenre.append(value)
            if count == 20:
                break
            count += 1

        print("Totalgenre \n" , Totalgenre)
        return(Totalgenre)