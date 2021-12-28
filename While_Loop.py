#WHILE LOOPS
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 14:27:40 2021
While Loop Practice
@author: yousuf
"""


#set yousuf to be tired
#yousuf is no longer tired at 9
#print tired and number until 9
#then print ready
yousuf = "tired"
i = 0
while yousuf == "tired":
    i+=1
    if i == 9:
        yousuf = "ready"
    print(i)
    print(yousuf)