# -*- coding: utf-8 -*-
"""
Created on Thu May  9 21:32:58 2019

@author: Mayank Jain
"""

"""
Code Challenge
  Name: 
    Duplicate
  Filename: 
    duplicate.py
  Problem Statement:
    With a given list [12,24,35,24,88,120,155,88,120,155]
    Write a program to print this list after removing all duplicate values 
    with original order reserved  
"""

i = int(input("enter how many element"))
list1 = []
for item in range(0,i):
    element = int(input("enter the element"))
    list1.append(element)
print(list1)

set1 = set(list1)
print(set1)
