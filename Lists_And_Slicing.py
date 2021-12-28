#LISTS DATA STRUCTURE AND SLICING
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 15:51:14 2021
Lists Practice (part one)
Indexing, Slicing, and Striding (for lists and strings)
@author: yousuf
"""


# PART ONE
print("PART ONE \n")

# list can include any primitive data type
# lists are ordered collections and are iterable

l1 = [1, 2, 3, 2, 5, 7]
l2 = [1, "String", True, False, 6, "hey"]

# print every item in l2
for i in range(len(l2)):
    print(l2[i])

# add 'bye' at the end of l2
l2.append('bye')
print(l2)

# add 'yousuf' to beginning of list
l2.insert(0, "yousuf")
print(l2)

# remove 'hey' from list
l2.remove("hey")
print(l2)

#reverse order of l1
l1.reverse()
print(l1)

#sort l1 list from ascending order
l1.sort()
print(l1)




# PART TWO
print("PART TWO \n")

digits = [0,1,2,3,4,5,6,7,8,9]


# Indexing, slicing, and striding
# works for both lists and strings

# get last element of digits
last_dig = digits[-1]
#print(last_dig)

# get all elements from 2 to end
two_on_lst = digits[2:]
#print(two_on_lst)

# Striding

#print all even numbers in digits
print(digits[0::2]) #[startingInt, endingInt, skipInt]
#negative strides will go backwards



