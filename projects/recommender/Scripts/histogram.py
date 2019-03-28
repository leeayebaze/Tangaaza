import pandas as pd # pandas is a data manipulation library
import numpy as np #provides numerical arrays and functions to manipulate the arrays efficiently
import random
import matplotlib.pyplot as plt # data visualization library
from wordcloud import WordCloud, STOPWORDS #used to generate world cloud

data= pd.read_csv('~/Desktop/movielens/movies.csv')
ratings_data=pd.read_csv('~/Desktop/movielens/ratings.csv',sep=',')
tags_data=pd.read_csv('~/Desktop/movielens/tags.csv',sep=',')

class histogramclass():
    def histogramfn(self):
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

        # Function that control the color of the words
        def random_color_func(word=None, font_size=None, position=None,
                            orientation=None, font_path=None, random_state=None):
            h = int(360.0 * tone / 255.0)
            s = int(100.0 * 255.0 / 255.0)
            l = int(100.0 * float(random_state.randint(70, 120)) / 255.0)
            return "hsl({}, {}%, {}%)".format(h, s, l)


        #Finally, the result is shown as a wordcloud:
        words = dict()
        trunc_occurences = keyword_occurences[0:50]
        for s in trunc_occurences:
            words[s[0]] = s[1]
        tone = 100 # define the color of the words
        f, ax = plt.subplots(figsize=(14, 6))
        wordcloud = WordCloud(width=550,height=300, background_color='white', 
                            max_words=1628,relative_scaling=0.7,
                            color_func = random_color_func,
                            normalize_plurals=False)
        wordcloud.generate_from_frequencies(words)
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis('off')
        #plt.show()

        # lets display the same result in the histogram
        fig = plt.figure(1, figsize=(18,13))
        ax2 = fig.add_subplot(2,1,2)
        y_axis = [i[1] for i in trunc_occurences]
        x_axis = [k for k,i in enumerate(trunc_occurences)]
        x_label = [i[0] for i in trunc_occurences]
        plt.xticks(rotation=85, fontsize = 15)
        plt.yticks(fontsize = 15)
        plt.xticks(x_axis, x_label)
        plt.ylabel("No. of occurences", fontsize = 24, labelpad = 0)
        ax2.bar(x_axis, y_axis, align = 'center', color='b')
        plt.title("Popularity of Genres",bbox={'facecolor':'k', 'pad':5},color='w',fontsize = 30)
        plt.show()
