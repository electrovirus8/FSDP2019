# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:52:55 2019

@author: Mayank Jain
"""

"""
Code Challenge
  Name: 
    Supermarket
  Filename: 
    supermarket.py
  Problem Statement:
    You are the manager of a supermarket. 
    You have a list of items together with their prices that consumers bought on a particular day. 
    Your task is to print each item_name and net_price in order of its first occurrence. 
    Take Input from User  
  Hint: 
    item_name = Name of the item. 
    net_price = Quantity of the item sold multiplied by the price of each item.
    try to use new class for dictionary : OrderedDict
  Input:
    BANANA FRIES 12
    POTATO CHIPS 30
    APPLE JUICE 10
    CANDY 5
    APPLE JUICE 10
    CANDY 5
    CANDY 5
    CANDY 5
    POTATO CHIPS 30
  Output:
    BANANA FRIES 12
    POTATO CHIPS 60
    APPLE JUICE 20
    CANDY 20

"""

dirc = {"BANANA" : 25 , "POTATO" : 15 , "APPLE" : 60 , "CANDY" : 10}


dirc2 = {}

while (True):
    item_name = input ("enter name")
    if not item_name:
        break
    elif item_name not in dirc.keys():
        print("item is not in store")
    #quantity = int(input("enetr quantity"))
    elif item_name in dirc2.keys():
        temp= int(input("enter the quantity"))
        quantity = temp + dirc2[item_name]
        dirc2[item_name] = quantity
    else:
        quantity = int(input("enetr quantity"))
        dirc2[item_name] = quantity

dirc3 = {}
total=0        
for item in dirc2.keys():
   price =  dirc[item]*dirc2[item]
   total = total + dirc[item]*dirc2[item]
   dirc3[item] = price
    
print(total)
print(dirc3)






"""
d={}
while :
    input .split()
    
    if not input :
        break 
        
    x=input(:-1)
    y=input[-1]
    d[x]=d.get(x,0)+y
    
   
"""  
    




















dirc3 ={}
for item in dirc:
    while item in dirc2:
        
        dirc3[item] = 
        
    


