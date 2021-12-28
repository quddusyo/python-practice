#DATETIME MODULE with PYTZ
import datetime
import pytz
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 14:36:53 2021
Datetime Module Practice
@author: yousuf
"""


# return todays date
today = datetime.date.today()
print(today)


#return birthday date
birthday = datetime.date(1999, 7 ,14)
print(birthday)


#return days since birth
days_since_birth = (today - birthday).days
print(days_since_birth)


#return todays date plus 10 days
tdelta = datetime.timedelta(days=10)
print(today + tdelta)


print(datetime.time(7, 2, 28, 15))
#datetime.date(Y, M, D)
#datetime.time(h, m, s, ms)
#datetime.datetime(Y, M, D, h, m, s, ms) #most common


#add 10 hours to current day
hour_delta = datetime.timedelta(hours=10)
print(datetime.datetime.now() + hour_delta)


datetime_today = datetime.datetime.now(tz=pytz.UTC)
datetime_pacific = datetime_today.astimezone(pytz.timezone('Canada/Mountain'))
print(datetime_pacific)

#print all timezones
#for tz in pytz.all_timezones:
#    print(tz)


#string formatting with dates
#2021-12-15 -> Decenmber 15, 2021

#%B for month, %d for day, %Y for year
print(datetime_pacific.strftime('%B %d, %Y'))


#return str time to datetime
# (March 09, 2019 -> 2019-03-09)
print(datetime.datetime.strptime('March 09, 2019', '%B %d, %Y'))

#if you put repr() around whole datetime it will turn it into a datetime object
print(repr(datetime.datetime.strptime('March 09, 2019', '%B %d, %Y')))