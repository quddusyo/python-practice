# CALENDER MODULE
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 08:51:04 2021
Calender Module Practice
@author: yousuf
"""


import calendar

#print every day of the week, first 3 letters
print(calendar.weekheader(3))
print()

#print index of first weekday
print(calendar.firstweekday())
print()

#print every day of march 2021
#weekdays should contain first 3 letters
#instead of default 2
print(calendar.month(2021, 3, w=3))

#print every day of 2021 march
print(calendar.monthcalendar(2021, 3))

#print whole 2021 year
print(calendar.calendar(2021))

#variable to check leap_year of 2020 //TRUE
is_leap_year = calendar.isleap(2020)
print(is_leap_year)