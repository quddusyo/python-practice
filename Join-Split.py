#JOIN AND SPLIT FUNCTIONS
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 16:34:12 2021
Join And Split Practice
@author: yousuf
"""


# join and split are ONLY used for strings
problems = 'broke, brown, short, nerdy'
print(problems) 

#print list representation of problems
l = problems.split(", ") #will split everything between ,
print(l)

#print str of list with ',' between
joined = ','.join(l)
print(joined)