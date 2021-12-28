#MUTABILITY
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 12:57:33 2021
Mutability Practice
@author: yousuf
"""


# Lists, dict, orderDict, sets are mutable
# Tuples are immutable



# you cannot mutate the tuple, but you can mutate the list
# inside the tuple because it is mutable, and vise versa
t = (1, 2, [1, 2, 3])
t[2][2] = 4
print(t)