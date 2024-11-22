# -*- coding: utf-8 -*-
__author__ = 'Sophie'

import pandas as pd
import numpy as np

# Load Data
userHeader = ['user_id', 'gender', 'age', 'ocupation', 'zip']
users = pd.read_csv('dataSet/users.txt', engine='python',
                    sep='::', header=None, names=userHeader, encoding='ISO-8859-1')

movieHeader = ['movie_id', 'title', 'genders']
movies = pd.read_csv('dataSet/movies.txt', engine='python',
                     sep='::', header=None, names=movieHeader, encoding='ISO-8859-1')

ratingHeader = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_csv('dataSet/ratings.txt', engine='python',
                      sep='::', header=None, names=ratingHeader, encoding='ISO-8859-1')

# Merge data
mergeRatings = pd.merge(pd.merge(users, ratings), movies)

# Clone DataFrame
def cloneDF(df):
    a = pd.DataFrame(df.values.copy(), df.index.copy(), df.columns.copy())
    return a.apply(pd.to_numeric, errors='ignore')  # Convert to numeric for numerical columns only

# Show Films with more votes. (groupby + sorted)
numberRatings = cloneDF(mergeRatings)
numberRatings = numberRatings.groupby('title').size().sort_values(ascending=False)
print('Films with more votes: \n%s' % numberRatings[:10])
print('\n==================================================================\n')

# Show avg ratings movie (groupby + avg)
<<<<<<< HEAD
=======
avgRatings = cloneDF(mergeRatings)
avgRatings = avgRatings.groupby(['movie_id', 'title']).mean(numeric_only=True)
print('Avg ratings: \n%s' % avgRatings['rating'][:10])
print('\n==================================================================\n')


# Show data ratings movies (groupby + several funtions)
>>>>>>> 22a35241b94ff71766ed79d0af0aa5c452267d18
dataRatings = cloneDF(mergeRatings)
dataRatings = dataRatings.groupby(['movie_id', 'title'])['rating'].agg(['mean', 'sum', 'count', 'std'])
print('Films ratings info: \n%s' % dataRatings[:10])
print('\n==================================================================\n')

# Show data ratings movies, applying a function (groupby + lambda function)
myAvg = cloneDF(mergeRatings)
myAvg = myAvg.groupby(['movie_id', 'title'])['rating'].agg(
    SUM=np.sum, COUNT=np.size, AVG=np.mean, myAVG=lambda x: x.sum() / float(x.count()))
print('My info ratings: \n%s' % myAvg[:10])
print('\n==================================================================\n')

# Sort data ratings by created field (groupby + lambda function + sorted)
<<<<<<< HEAD
=======
<<<<<<< HEAD
sortRatingsField = cloneDF(mergeRatings)
sortRatingsField = sortRatingsField.groupby(['movie_id', 'title'])['rating'].agg(
<<<<<<< HEAD
    COUNT=np.size, myAVG=lambda x: x.sum() / float(x.count()))
sortRatingsField = sortRatingsField.sort_values(by='COUNT', ascending=False)  
print('My info sorted: \n%s' % sortRatingsField[:15])
=======
<<<<<<< HEAD
    COUNT=np.size, myAVG=lambda x: x.sum() / float(x.count())).sort_values(by = 'COUNT', ascending=False)
#print('My info sorted: \n%s' % sortRatingsField[:15])
=======
=======
>>>>>>> 92fc51fa78a6ef01da3917baf6e15edd65dd2884
sortRatingsFieldEmmanuel = cloneDF(mergeRatings)
sortRatingsFieldEmmanuel = sortRatingsFieldEmmanuel.groupby(['movie_id', 'title'])['rating'].agg(
    COUNT=np.size, myAVG=lambda x: x.sum() / float(x.count())).sort_values(by='COUNT',  ascending=False) #test Emmanuel , sort('COUNT', ascending=False)
print('My info sorted: \n%s' % sortRatingsFieldEmmanuel[:15])
<<<<<<< HEAD
print('test')
=======

# Essaie des modifications Deborah


print('test')


>>>>>>> 01e98f7fcc97ae20c4e249c842ee0beb2b5ecdf4
>>>>>>> 22a35241b94ff71766ed79d0af0aa5c452267d18
>>>>>>> 92fc51fa78a6ef01da3917baf6e15edd65dd2884
