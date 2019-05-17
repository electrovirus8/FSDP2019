# -*- coding: utf-8 -*-
"""
Created on Wed May  8 07:02:50 2019

@author: Mayank Jain
"""

"""
Code Challenge
  Name: 
    Styling of String
  Filename: 
    style.py
  Problem Statement:
    Convert to uppercase character
    Convert to lower character 
    Convert to CamelCase or TitleCase.
  Hint: 
    Try to find some function in the str class and see its help on how to use it.
    Using dir and help functions
  Input:
    Take the name as input from the keyboard. ( SyLvEsTeR )
"""

dir (str)

help (str.title)

str1 = "mayank"
str2 = str1.upper()
str2.lower()

str1.title()