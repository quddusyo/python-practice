#TUPLES
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 19:22:11 2021
Tuples Practice
@author: yousuf
"""

# like lists but are IMMUTEABLE
# tuples are lists with constraints and use ()
# CANNOT add or remove elements


t = (1,2,3)


#useful for when you dont want to change data
creditCard1 = (21321312312, 'yousuf', 'y@gmail.com', '11/28', 151)
creditCard2 = (67656432092, 'joe', 'joe@gmail.com', '09/28', 555)

creditCards = [creditCard1, creditCard2]

print(creditCards)


# can set multiple varibles to tuples easily
# called tuple unpacking
cardNum, name, email, expDate, cvvNum = creditCard1
print(cardNum)
print(name)
print(email)
print(expDate)
print(cvvNum)


# tuple for loop example for multiple tuples in list
for cardNum, name, email, expDate, cvvNum in creditCards:
    print(cardNum)
    print(name)
    print(email)
    print(expDate)
    print(cvvNum)
