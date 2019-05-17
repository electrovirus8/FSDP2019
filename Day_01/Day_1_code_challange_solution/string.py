# -*- coding: utf-8 -*-
"""
Created on Wed May  8 07:03:49 2019

@author: Mayank Jain
"""

"""
Code Challenge
  Name: 
    String Handling
  Filename: 
    string.py
  Problem Statement:
    Take first and last name in single command from the user and print  
    them in reverse order with a space between them, 
    find the index using find/index function and then print using slicing concept of the index
  Input:
      Sylvester Fernandes
  Output: 
      Fernandes Sylvester 
"""

print(input("enter the name"))
name = input("enter the name")
print (name)
index = name.find(" ")
length = len(name)
print(name[index+1:length+1] +" " + name[0:index])