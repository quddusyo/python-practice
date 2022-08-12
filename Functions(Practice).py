import math
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
text='the_stealth_warrior'
#text='the-stealth-warrior'


# function which returns string back as camel-case
def to_camel_case(text):
    #your code here
    return_text = ''
    N = len(text)
    i=0
    while i < N:
        if text[i].isalpha() == False:
            i+=1
            return_text = return_text + text[i].capitalize()
        else:
            return_text = return_text + text[i]
        i += 1
    text = return_text
    return text
 
# function which returns true iff isogram
def is_isogram(string):
    #your code here
    #set empty list variable
    is_isogram = []
    #set string to list of letters
    for letter in string:
        letter = letter.capitalize()
        is_isogram.append(letter)
    #set a variable of type set with the same letters as list
    isogram = set(is_isogram)
    # if they both have the same length return true
    if len(is_isogram) == len(isogram):
        return True
    #else return false
    else:
        return False

# function that determines membership as senior or open
def open_or_senior(data):
    # set list variable
    membership = []
    # go through each tuple in data
    for item in data:
    # iff age >= 55 and handicap > 7 append Senior
        if item[0] >= 55 and item[1] > 7:
            membership.append('Senior')
        # else append Open to list variable
        else:
            membership.append('Open')
    return membership

# functiom which returns true if number
# of x's == number of o'x
def xo(s):
    #set two numbers = 0, one for x and one for o
    num_x = 0
    num_o = 0
    #add 1 to x for number of x, or 1 to o for number of o
    for letter in s:
        print(letter)
        if letter == 'x' or letter == 'X':
            num_x += 1
        if letter == 'o' or letter == 'O':
            num_o += 1
    #check if the variables are equal
    print(num_x)
    print(num_o)
    if num_x != num_o:
        return False
    else:
        return True
    


def longest(a1, a2):
    # your code
    longest_possible = set(a1)|set(a2)
    longest_possible = sorted(longest_possible)
    return ''.join(longest_possible)

def solution(number):
    sum_list = []
    if number > 0:
        for num in range(number):
            if num % 3 == 0 or num % 5 == 0:
                sum_list.append(num)
                
        sum_list = sum(sum_list)
    else:
        return 0
    return sum_list

def rgb(r, g, b):
    # #your code here :)
    # #variables and dict
    # color_num = [10, 11, 12, 13, 14, 15]
    # color_letter = ['A', 'B', 'C', 'D', 'E', 'F']
    # d = {}
    
    
    # # hex of r1:
    # # 1. floor func of first digit coverted to hex
    # # 2. remainder of r/16 *16 to get second hec dig of r
    # hex_r1 =r//16
    # hex_r2 = (r%16)*16
    
    # #hex of g:
    # hex_g1 =g//16
    # hex_g2 = (g%16)*16
    
    # #hex of b:
    # hex_b1 =b//16
    # hex_b2 = (b%16)*16
    
    # # add key value pairs to dict
    # for i in range(len(color_num)):
    #     d[color_num[i]] = color_letter[i]
    
    # #logic
    # if hex_r1|hex_r2|hex_g1|hex_g2|hex_b1|hex_b2 < 10:
        
    
    # return d
    colortuple = (r, g, b)
    return ''.join(f'{i:02X}' for i in colortuple)

