#IF-ELSE AND ELIF STATEMENT
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 14:20:37 2021
If-Else And Elif(Else-If) Statement Practice
@author: yousuf
"""


#One Time Guessing Game
#promp user to enter a number
#if guess too high, print guess too high
#if too low, print guess too low
#else print you got it

#set num to be the answer
num = 15
guess = int(input("enter a number: "))
if guess > num:
    print ("your guess is too high")
elif guess < num:
    print("Sorry guess too low")
else:
    print("YOU GOT IT!")