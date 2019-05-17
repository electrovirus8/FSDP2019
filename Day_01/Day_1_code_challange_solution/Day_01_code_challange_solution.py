# -*- coding: utf-8 -*-
"""
Created on Tue May  7 11:36:47 2019

@author: Mayank Jain
"""

"""
Code Challenge
  Name: 
    Gas Mileage Calculator
  Filename: 
    mileage_cal.py
  Problem Statement:
    Assume my car travels 100 Kilometres after putting 5 litres of fuel. 
    Calculate the average of my car. 
  Hint: 
    Divide kilmeters by the litres used to get the average
solution:-
"""
Kilometres = float(input ("enter the Kilometres"))
print(Kilometres)
litres = int(input("enter the litres"))
print(litres)
avg = Kilometres/litres
print(avg) 

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

"""
Code Challenge
  Name: 
    Name Printing Checkerboard pattern
  Filename: 
    checker.py
  Problem Statement:
    Print the checkerboard pattern using escape Codes and Unicode 
    with multiple print statements and the multiplication operator 
  Hint: 
    Eight characters sequence in a line and 
    the next line should start with a space
    try to use the * operator for printing
  Input:
    No input required
  Output:
    * * * * * * * *
     * * * * * * * *
    * * * * * * * *
     * * * * * * * *
    * * * * * * * *
     * * * * * * * *
    * * * * * * * *

"""
i = 0
while(i<4):
    print("* " * 8)
    if(i==3):
        break
    print(" *" * 8)
    i=i+1


"""
Code Challenge
  Name: 
    Facorial
  Filename: 
    factorial.py
  Problem Statement:
    Find the factorial of a number. 
  Hint: 
    Factorial of 3 = 3 * 2 * 1= 6 
    Try to first find the function from math module using dir and help 
  Input:
    Take the number from the keyboard as input from the user.
"""

import math

dir (math)

math.factorial(5)

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

"""
Code Challenge
  Name: 
    Replacing of Characters
  Filename: 
    restart.py
  Problem Statement:
    In a hardcoded string RESTART, replace all the R with $ except the first occurrence and print it.
  Input:
    RESTART
  Output: 
    RESTA$T
"""
string = "AARESTARTR"

length = len(string)
index = string.find("R")

str1 = string[0:index+1]
str2 = string[index+2:length+2]
str3 = str2.replace("R","$")

string4 = str1+str3
print(string4)

print(string[0:index+1] + " " + string[index+2:length+2])

"""
Code Challenge
  Name: 
    String Handling
  Filename: 
    string.py
  Problem Statement:
    Take first and last name in single command from the user and print  
    them in reverse order with a space between them, 
    find the index using find/index function and then print using slicing concept of the index
  Input:
      Sylvester Fernandes
  Output: 
      Fernandes Sylvester 
"""

print(input("enter the name"))
name = input("enter the name")
print (name)
index = name.find(" ")
length = len(name)
print(name[index+1:length+1] +" " + name[0:index])



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

"""
Code Challenge
  Name: 
    Formatted String
  Filename: 
    format3.py
  Problem Statement:
    Write a program to print the output in the given format. 
    Take input from the user. 
  Hint:
    Try to serach for some function in the str class using help() and dir()
  Input:
    Welcome to Pink City Jaipur
  Output:
    W*e*l*c*o*m*e* *t*o* *P*i*n*k* *C*i*t*y* *J*a*i*p*u*r
"""


dir(str)
help(str.join)

string = input("enter the string")
"*".join(string)


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

        
        
        



