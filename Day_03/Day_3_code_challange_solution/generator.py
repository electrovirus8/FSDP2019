# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:13:54 2019

@author: Mayank Jain
"""

"""
Code Challenge
  Name: 
    generator
  Filename: 
    generator.py
  Problem Statement:
    This program accepts a sequence of comma separated numbers from user 
    and generates a list and tuple with those numbers.  
  Input: 
    2, 4, 7, 8, 9, 12
  Output:
    List : ['2', ' 4', ' 7', ' 8', ' 9', '12'] 
    Tuple : ('2', ' 4', ' 7', ' 8', ' 9', '122')
"""

string = input("enter the string")

list = list(string)
while ("," in list):
    list.remove(",")

tuple = tuple(list)
print(tuple)
