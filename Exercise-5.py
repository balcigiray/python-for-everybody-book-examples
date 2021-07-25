#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 00:12:31 2021

@author: giraybalci
"""

# Exercise 1: Write a program which repeatedly reads numbers 
# until the user enters “done”. Once “done” is entered, print 
# out the total, count, and average of the numbers. If the user 
# enters anything other than a number, detect their mistake using 
# try and except and print an error message and skip to the next number.

count = 0.0
total = 0.0

while True:
    inp = input("Enter something: ")
    
    if(inp == 'done'):
        break
    
    try:
        inp = float(inp)
        total += inp
        count += 1
    
    except:
        print("not a number")

print("Total: ", total)
print("Average: ", total/count)
print("Count: ", count)        


#%%
# Exercise 2: Write another program that prompts for a list of 
# numbers as above and at the end prints out both the maximum and 
# minimum of the numbers instead of the average.

minimum = None
maximum = None

while True:
    inp = input("Enter something: ")
    
    if(inp == 'done'):
        break
    
    try:
        inp = float(inp)
        
        if minimum is None or inp < minimum:
            minimum = inp
        
        if maximum is None or inp > maximum:
            maximum = inp
    
    except:
        print("not a number")
    
print("Maximum: ", maximum)
print("Minimum: ", minimum)

