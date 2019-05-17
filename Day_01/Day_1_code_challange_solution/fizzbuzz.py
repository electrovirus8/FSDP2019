# -*- coding: utf-8 -*-
"""
Created on Wed May  8 07:05:35 2019

@author: Mayank Jain
"""

"""
Code Challenge
  Name: 
    Fizz Buzz
  Filename: 
    fizzbuzz.py
  Problem Statement:
    Write a Python program which iterates the integers from 1 to 100(included). 
    For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
    For numbers which are multiples of both three and five print "FizzBuzz". 
  User Input 
    Not required  
  Output:
    1
    2
    Fizz
    4 
    Buzz  
"""

i=1
while(i<=100):
    if(i%5==0 | i%3==0):
        print("FIZZBUZZ")
    elif(i%3==0):
        print("Fizz")
    elif(i%5==0):
        print("Buzz")
    else:
        print(i)
    i=i+1