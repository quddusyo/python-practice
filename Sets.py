#SET
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 19:59:34 2021
Set Practice
@author: yousuf
"""


# A set cannot contain duplicates and can grow or shrink
# Sets are unordered

s={'blueberry', 'rasberry'}

s.add('strawberry')

print(s)


#remove all duplicates from a list
l = [1,2,2,2,23,3,4,5,6]
set_l = set(l)
l = list(set_l)
print(l)


#union method for sets
#adds both sets togather ignoring duplicates
lib1 = {'Harry Potter', 'Hunger Games', 'Lord of the Rings'}
lib2 = {'Harry Potter', 'Romeo and Juliet'}
town = lib1.union(lib2)
print(town)

#intersection method return commons in both sets
at_both_lib = lib1.intersection(lib2)
print(at_both_lib)

#difference method returns instances different from
#first set 
diff = lib1.difference(lib2)
print(diff)

#clear method clears a set
clear = lib1.clear()
print(clear)