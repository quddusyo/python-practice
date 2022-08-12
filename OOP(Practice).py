#OOP PRACTICE
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 03:44:57 2022
OOP Concept And Inheritance Practice 
@author: yousuf
"""


'''
Write 3 classes:
    One for Pets that have name and age methods,
    One for Cat, which inherits Pets and have an speak method('MEOW!'),
    One for Dog, which inherits Pets and have an speak method('WOOF!')
'''

class Pets():
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def info(self):
        return(f"My name is {self.name} and I am {self.age} years old.")
    def speak(self):
        return("I dont know what I say T.T")
    
class Cat(Pets):
    def __init__(color):
        super.color = color
    def color(self):
        return(f"I am {self.color}")
    def speak(self):
        return("MEOW!")
    
class Dog(Pets):
    def __init__(color):
        super().color = color
    def color(self):
        return(f"I am {self.color}")
    def speak(self):
        return("WOOF!")
    
    
pet1 = Pets(25, 'Unknown Animal')

c1 = Cat(10, "Muffin", "Orange Taby")

d1 = Dog(14, "Ruff", "Brown")

print(pet1.speak())
print(c1.speak())
print(d1.speak())
print(c1.info())
print(d1.info())