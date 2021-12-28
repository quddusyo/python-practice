#DICTIONARIES
#from collections import OrderedDict
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 12:03:12 2021
Dictionaries Practice
Dictionaries are unordered
Ordered Dictionary requires import!
@author: yousuf
"""


# Key:value pairs
# constant time (very fast)
# Super organized data (mini database)

groceries = {'bananas': 5, 'oranges': 3}
print(groceries['bananas']) #returns 5
# if key is not in dictionary, it will give you keyError

# same method as above but instead of keyError, it returns
# None
print(groceries.get('notInList'))


contacts = {
    'joe': ['123-456', 'joe@gmail.com'],
    'jane': ['587-777', 'jane@gmail.com'],
    'jack': ['987-423', 'jack@cloud.ca']
    }

print(contacts['joe'])


sentence = 'guess how many words are in this sentence'
wordCount = {
    'guess': 1,
    'how': 1,
    'many': 1
    }

#sorting a dictionary
# dict.items() returns
# object dict_items to list of tuples of key,value pairs
print(wordCount.items())
# NOTE: to not get the dict_items object, USE list
print(list(wordCount.items()))


# dict.keys() returns
# object dict_items of list of only keys
print(wordCount.keys())


# dict.values() returns
# object dict_items of list of only values
print(wordCount.values())

# to add to a dictionary simply use new key
# wordCount['words'] = 1 # this will add 'words':1 to dict

# to remove a key:value pair use .pop(key) returns value
# to remove last item/ARBITRARY use .popitem() returns tuple (key,value)

# dict.clear() empties out dictionary