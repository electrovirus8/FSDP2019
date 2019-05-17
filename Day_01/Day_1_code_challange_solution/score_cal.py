# -*- coding: utf-8 -*-
"""
Created on Wed May  8 07:01:08 2019

@author: Mayank Jain
"""

"""
Code Challenge
  Name: 
    Weighted Score Calculator
  Filename: 
    score_cal.py
  Problem Statement:
    Lets assume there are 3 assignments and 2 exams, each with max score of 100. 
    Respective weights are 10%, 10%, 10%, 35%, 35% . 
    Compute the weighted score based on individual assignment scores.  
  Hint: 
    weighted score = ( A1 + A2 + A3 ) *0.1 + (E1 + E2 ) * 0.35
"""

A1 = int (input("enter the marks of assignments1"))
print(A1)


A2 = int (input("enter the marks of A2"))
print(A2)

A3 = int (input("enter the marks of A3"))
print(A3)



E1 = int (input("enter the marks of E1"))
print(E1)

E2 = int (input("enter the marks of E2"))
print(E2)

weighted_score = (( A1 + A2 + A3 ) *0.1 + (E1 + E2 ) * 0.35)
print(weighted_score)
