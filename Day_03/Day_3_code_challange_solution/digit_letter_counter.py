# -*- coding: utf-8 -*-
"""
Created on Thu May  9 22:09:33 2019

@author: Mayank Jain
"""

"""
Code Challenge
  Name: 
    Digit Letter Counter
  Filename: 
    digit_letter_counter.py
  Problem Statement:
    Write a Python program that accepts a string from User and calculate the number of digits and letters.
  Hint:
    Store the letters and Digits as keys in the dictionary  
  Input: 
    Python 3.2
  Output:
    Digits 2
    Letters 6 
"""

str1 = input("enter the string")
print(str1)
dict1 = {}
digit = 1
letters = 0 
for item in str1:
    if item == " ":
        digit = digit+1
    else:
        letters = letters + 1
dict1["digits"] = digit
dict1["letter"] = letters
print(dict1)