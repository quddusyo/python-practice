#WEB SCRAPING
import pandas as pd
import requests
from bs4 import BeautifulSoup
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 00:19:58 2021
Web Scraping Practice
@author: yousuf
"""


page = requests.get('https://www.cbc.ca/weather/s0000047.html')
soup = BeautifulSoup(page.content, 'html.parser')

# select the week by id
week = soup.find(id="int-forcast-inner")
#print(week)

# select weekdays by id for week
week_days = [week.find(id="u-data").get_text()]
print(week_days)

#select dates by id for week
week_weather = week.find(id="l-data")
print(week_weather)






#select day forecast for week by class
week_forecast = week.find_all(class_="dayforecast")
#print(week_forecast)
week_temp = [item.find(class_="celsius").get_text() for item in week_weather]
print(week_temp)

#list of week info as variable
week_info = [item.get_text().strip('\t\n') for item in week_forecast]

weather_info = pd.DataFrame(
    {
     'forecast': week_info,
     })
print(weather_info)