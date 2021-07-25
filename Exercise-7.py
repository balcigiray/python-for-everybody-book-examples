#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 00:01:42 2021

@author: giraybalci
"""


fhand = open('mbox.txt') 
count = 0

for line in fhand:
    count = count + 1
print('Line Count:', count)


#%%

fname = input("Enter a file name: ")
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

count = 0

for line in fhand:
    if line.startswith('Subject:'):
        count += 1
        
print('There were', count, 'subject lines in', fname)        


#%%
#If the file already exists, opening it in write mode clears out the old data 
#and starts fresh, so be careful! If the file doesn’t exist, a new one is created

fout = open('output.txt', 'w')

print(fout)

line1 = "This here's the wattle,\n"
fout.write(line1)
line2 = 'the emblem of our land.\n'
fout.write(line2)
fout.close()


#%%

s = '1 2\t 3\n 4'
print(s)
print(repr(s))


#%%
# Write a program to read through a file and print the contents of the file 
# (line by line) all in upper case

fhand = open("mbox-short.txt")

count = 0

for line in fhand:
    count += 1
    
    if count > 10: #for not to print everything
        break
    
    print(line.upper())
    

#%%
# Write a program to prompt for a file name, and then read
# through the file and look for lines of the form:
# X-DSPAM-Confidence: 0.8475
# When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the 
# line to extract the floating-point number on the line. Count these lines and 
# then compute the total of the spam confidence
# 90 CHAPTER 7. FILES values from these lines. When you reach the end of the file,
# print out the average spam confidence.

fname = input("Enter a file name: ")

try:
    fhand = open(fname)
except:
    print("No such file exist.")
    exit()
    
total = 0.0
count = 0.0

for line in fhand:
    if line.startswith("X-DSPAM-Confidence"):
        semicPos = line.find(":")
        
        count += 1
        number = line[semicPos+1:]
        total += float(number)

print("Total number of spam line: ", count)
print("Average spam confidence: ", total/count)

