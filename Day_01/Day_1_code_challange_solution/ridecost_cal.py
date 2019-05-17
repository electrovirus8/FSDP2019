# -*- coding: utf-8 -*-
"""
Created on Wed May  8 07:00:31 2019

@author: Mayank Jain
"""


"""
Code Challenge
  Name: 
    Ride Cost Calculator
  Filename: 
    ridecost_cal.py
  Problem Statement:
    Assume you travel 80 km to and fro in a day. 
    Cost of Diesel per litre is 80 INR 
    Your vehicle Fuel Average is 18 km/litre. 
    Now calculate the cost of driving per day to office. 
  Hint: 
""" 

distance = float(input("enter total kilometres travelled"))
print(distance)
cost_of_diesel = 100
average= 18
cost_of_driving = float((distance/average)*cost_of_diesel)
print(cost_of_driving)