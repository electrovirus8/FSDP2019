# -*- coding: utf-8 -*-
"""
Created on Wed May  8 07:03:21 2019

@author: Mayank Jain
"""

"""
Code Challenge
  Name: 
    Replacing of Characters
  Filename: 
    restart.py
  Problem Statement:
    In a hardcoded string RESTART, replace all the R with $ except the first occurrence and print it.
  Input:
    RESTART
  Output: 
    RESTA$T
"""
string = "AARESTARTR"

length = len(string)
index = string.find("R")

str1 = string[0:index+1]
str2 = string[index+2:length+2]
str3 = str2.replace("R","$")

string4 = str1+str3
print(string4)

print(string[0:index+1] + " " + string[index+2:length+2])
