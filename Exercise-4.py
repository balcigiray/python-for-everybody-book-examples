#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:13:48 2021

@author: giraybalci
"""

print(max("asdvz xzzxcgf"))

print(len("This is a trial"))

#%%

import math

print(math)

decibels = 10 * math.log10(4)
print(decibels)


#%%

import random

for i in range(5):
    r = random.random()
    print(r)
    
print(random.randint(-10, 10))

t = [4, 6, 8, 2, 9]

print(random.choice(t))


#%%

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')
    
 
def repeat_lyrics(): 
    print_lyrics() 
    print_lyrics()


repeat_lyrics()


#%%
largest = None
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest : 
        largest = itervar

    print('Loop:', itervar, largest)
print('Largest:', largest)

