#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 10:08:46 2021

@author: giraybalci
"""
#%%
#CHAPTER 2 examples

print("Simple print operation")
print(3)

print("Power operator")
print(5**2)

print("Division results in floating number:")
print(59/60)

print("Division results in truncated number:")
print(59//60)

print("Quotient operator:")
print(7//2)

print("Remainder:")
print(7%2)

print("Text multiplipication:")
print("Trial " * 3)

text = input("Enter a text:\n")
print(text)


#%% 
#CHAPTER 3 examples

print("Boolean expression:")
print(5 == 5)

x =  6
y = 7
print(x > y)
print(not x > y)

hours = input("Enter work hours: ")
rate = input("Enter rate: ")

try:
    hours = float(hours)
    rate = float(rate)
    salary = hours * rate
    print("Salary: ", salary)
    
except: 
    print("Error, please enter a valid number!")
    
    
#%%

page = input("Enter page: ")
print("You are at " + str(int(page)*100/247) + " percent of book.")
        
