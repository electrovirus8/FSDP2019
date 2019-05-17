# -*- coding: utf-8 -*-
"""
Created on Thu May  9 12:00:59 2019

@author: Mayank Jain
"""

"""
Code Challenge
  Name: 
    Teen Calculator
  Filename: 
    teen_cal.py
  Problem Statement:
    Take dictionary as input from user with keys, a b c, with some integer 
    values and print their sum. However, if any of the values is a teen -- 
    in the range 13 to 19 inclusive -- then that value counts as 0, except 
    15 and 16 do not count as a teens. Write a separate helper "def 
    fix_teen(n):"that takes in an int value and returns that value fixed for
    the teen rule. In this way, you avoid repeating the teen code 3 times  
  Input: 
    {"a" : 2, "b" : 15, "c" : 13}
  Output:
    Sum = 17
"""

dirc = {}
while True:
    input_alpha = input("enter alpaha")
    if not input_alpha:
        break
   # input_value = int(input("enter the value"))
    input_alpha=input_alpha.split()
    x=str(input_alpha[:-1])
    y=int(input_alpha[-1])
    dirc[x] = y


print[dir]
   
   