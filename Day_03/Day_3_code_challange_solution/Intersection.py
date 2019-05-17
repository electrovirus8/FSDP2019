# -*- coding: utf-8 -*-
"""
Created on Thu May  9 22:25:35 2019

@author: Mayank Jain
"""

"""
Code Challenge
  Name: 
    Intersection
  Filename: 
    Intersection.py
  Problem Statement:
    With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155]
    Write a program to make a list whose elements are intersection of the above given lists.  
"""
i = int(input("enter how many element"))
list1 = []
for item in range(0,i):
    element=int(input("enter the elament"))
    list1.append(element)
print(list1)

j = int(input("enter how many element"))
list2 = []
for item in range(0,j):
    element1=int(input("enter the elament"))
    list2.append(element1)
print(list2)

list3 = list1+list2