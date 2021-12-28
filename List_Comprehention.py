#LIST COMPREHENTIONS
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 13:40:59 2021
List Comprehention Practice
@author: yousuf
"""


names = ['Jennifer', 'Sean', 'Jane', 'Sophie']

# one way to add persons into an empty list
l = []
for person in names:
    l.append(person)
print(l)

# List comprehention equivalent same code above
print([person for person in names])




movies_and_rating = {'interstellar':9, 'Dark Knight':8, '50 Shades':3}

# get all movies with rating higher than 6
l=[]
for movie in movies_and_rating:
    if movies_and_rating[movie] > 6:
        l.append(movie)
print(l)

# list comprehention of movies with rating higher than 6
print( [movie for movie in movies_and_rating if movies_and_rating[movie] > 6] )

