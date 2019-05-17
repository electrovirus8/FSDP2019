# -*- coding: utf-8 -*-
"""
Created on Thu May  9 12:41:11 2019

@author: Mayank Jain
"""

"""
Code Challenge
  Name: 
    Character Frequency
  Filename: 
    frequency.py
  Problem Statement:
    This program accepts a string from User and counts the number of characters (character frequency) in the input string.  
  Input: 
    www.google.com
  Output:
    {'c': 1, 'e': 1, 'g': 2, 'm': 1, 'l': 1, 'o': 3, '.': 2, 'w': 3}
"""


dict1 = {}
str1 = input("enter the string")
print(str1)

for i in str1:
    if i in dict1.keys():
        dict1[i] = dict1[i] +1
    else:
        dict1[i] = 1

print(dict1)
dict2 = dict(sorted(dict1.items()))
print(dict2)  

      