# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:22:35 2019

@author: Mayank Jain
"""

"""
Code Challenge
  Name: 
    weeks
  Filename: 
    weeks.py
  Problem Statement:
    Write a program that adds missing days to existing tuple of days
  Input: 
    ('Monday', 'Wednesday', 'Thursday', 'Saturday')
  Output:
    ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
"""
tuple1 = ('Monday', 'Wednesday', 'Thursday', 'Saturday')
tuple2 = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

list1 = list(tuple1)
list2 = list(tuple2)


for item in list2:
    if item not in list1:
        list1.insert(list2.index(item),item)

print(list1)

tuple3 = tuple(list1)
print(tuple3)


