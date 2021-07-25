#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 12:33:54 2021

@author: giraybalci
"""

while True:
    inp = input("Enter something: ")
    
    if inp == 'backwards':
        break
    
    l = len(inp)
    for i in range(l):
        print(inp[l-i-1])
     
print("Voila!")


#%%
#Slicing string

text = "watermelon"

l = len(text)

print(text[:l//2])
print(text[l//2:])


#%%
fruit = "melon"
print(fruit[:])


#%%
# Exercise 3: Encapsulate this code in a function named count, and generalize
# it so that it accepts the string and the letter as arguments.

def count(word, char):
    count = 0
    
    for letter in word:
        if letter == char:
            count = count + 1
    
    return count

text = "tree in a forest"
char = 't'

print(count(text, char))

print(dir(text))
help(str.capitalize)

print(text.find('e'))


#%%

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ',atpos)
print(sppos)
host = data[atpos+1:sppos]
print(host)

#%%

print('In %d years I have spotted %g %s.' % (3, 0.1, 'camels'))

#%%
# Exercise 5: Take the following Python code that stores a string:
# str = 'X-DSPAM-Confidence:0.8475'
# Use find and string slicing to extract the portion of the string after the
# colon character and then use the float function to convert the extracted string
# into a floating point number.

str = 'X-DSPAM-Confidence:0.8475'

semicPos  = str.find(':')
number = str[semicPos+1:]
print(float(number))

