#ZIP FUNCTIONS
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 21:58:26 2021
Zip Functions Practice
@author: yousuf
"""


list1 = [1,2,3,4,5]
list2 = ['one', 'two', 'three', 'four', 'five']

#create new list of tuples with with of occurenses of the
#two lists
zipped = list(zip(list1, list2))
print(zipped)
#shorter list will take presidence and larger list will be trunkated


#unzip a zipped list
unzipped = list(zip(*zipped)) #asterisk to unzip (*)
print(unzipped)



#for (l1, l2) in zip(list1, list2):
#    print(l1)
#    print(l2)


''' 
print 3 lists zipped together
l1 = [apple]
l2 = [3]
l3 = [0.99]
>> ['I bought 3 apples for 0.99.']
'''
items = ['apple', 'banana', 'orange']
counts = [3,6,4]
prices = [0.99, 0.25, 0.50]

sentences = []
for (item, count, price) in zip(items, counts, prices):
    item, count, price = str(item), str(count), str(price)
    sentence = "I bought " + count + " " + item + "s for " + price + "."
    sentences.append(sentence)
print(sentences)