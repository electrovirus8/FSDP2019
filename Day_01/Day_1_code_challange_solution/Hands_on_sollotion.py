# -*- coding: utf-8 -*-
"""
Created on Wed May  8 06:35:44 2019

@author: Mayank Jain
"""

# Hands On  1
# Print all the numbers from 1 to 10 using condition in while loop

i=0
while(i<=10):
    print(i)
    i+=1


# Hands On  2
#  Print all the numbers from 1 to 10 using while True loop
    
i=0
while(True):
    print(i)
    i+=1
    if(i==11):
        break
    
    
# Hands On 3
#  Print all the even numbers from 1 to 10 using condition in while loop

i=0
while(i<=10):
    if(i%2==0):
        print(i)
        i+=1
    else:
        i+=1
        continue

# Hands On 4
#  Print all the even numbers from 1 to 10 using while True loop

i=0
while(True):
    if(i%2==0):
        print(i)
    elif(i==11):
        break
    i+=1

# Hands On 5
#  Print all the odd numbers from 1 to 10 using condition in while loop

i=0
while(i<=10):
    if(i%2!=0):
        print(i)
    i+=1

# Hands On 6
#  Print all the odd numbers from 1 to 10 using while True loop

i=0
while(True):
    if(i%2!=0):
        print(i)
    elif(i==10):
        break
    i+=1


