# -*- coding: utf-8 -*-
"""
Created on Wed May  8 07:04:18 2019

@author: Mayank Jain
"""

"""
Code Challenge
  Name: 
    Formatted String
  Filename: 
    format2.py
  Problem Statement:
    Write a program to print the output in the given format. 
    Take input from the user. 
  Hint:
    Try to serach for some function in the str class using help() and dir()
  Input:
    Welcome to Pink City Jaipur
  Output:
    Welcome*to*Pink*City*Jaipur
"""

string = input("enter the string")
print(string.replace(" ","*"))