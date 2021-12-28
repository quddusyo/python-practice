#REGEX
import re
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 13:58:08 2021
Regex Practice
@author: yousuf
"""

#.search returns first instance found
#.findall returns all instances found
text = 'A random string'

#return first match from the text where text included either A,B, or C
#only returns first match found (span and match Match object)
pattern = re.compile('[ABC]')

result = pattern.search(text)

print(result)

#return first match from the text where text included from a to c
pattern = re.compile('[a-c]')

result = pattern.search(text)

print(result)

#return first match from the text where text included from a to c
#and A to C
pattern = re.compile('[a-cA-C]')

result = pattern.search(text)

print(result)


#return first number that appears in a string
text = 'A random string where it include 21321312313yousuf'
pattern = re.compile('[0-9]+')

result = pattern.search(text)

print(result)



# EMAIL TEXT SCRAPER
# for special charecters like . - _ @ ! etc, you need to put
# \ (backslash) to escape
#return the first email that appears in a string
text = 'A random string where it includes yousuf1quddus@gmail.com this and that and this.'
pattern = re.compile('[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+')

result = pattern.search(text)

print(result)


#return all emails that appears in a string
text = 'A random string bob__@gmail.com and ha.iley-m_1@company.io where it includes yousuf1quddus@gmail.com this and that and this.'
pattern = re.compile('[a-zA-Z0-9\.\_\-]+@[a-zA-Z0-9]+\.[a-zA-Z]+')

result = pattern.findall(text)

print(result)