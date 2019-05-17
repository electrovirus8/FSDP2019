# -*- coding: utf-8 -*-
"""
Created on Wed May  8 07:06:08 2019

@author: Mayank Jain
"""

# Interactive Guess the Number Game  
""" 
     Challenge 1
     The computer will think of a random number from 1 to 10 as secret number
     Then ask you ( Player ) to guess the number and store as guess number 
     Compare the guess number with the secret number
     If the player guesses the right number he wins,
     so print player wins and computer lose.
     If the player guesses the wrong number,      
     then he loses so print player lose and computer wins. 
""" 

import random 

r1 = random.randint(0,10)
print (r1)
player_input = int(input("enter the no"))
if(r1==player_input):
    print("WIN")
else:
    print("LOSS")

"""
    Challenge 2
    Print the secret number and guess number when Player loses using format function  
""" 

r1 = random.randint(0,10)
print (r1)
player_input = int(input("enter the no"))
if(r1==player_input):
    print("WIN")
else:
    print("player loses as random no is {} and palyer choose {}".format(r1,player_input))
    
"""
    Challenge 3    
    Print too HIGH or too LOW messages for bad guesses using elif    
"""
 
player_input = int(input("enter the no"))
if(r1==player_input):
    print("WIN")
elif():
    print("player loses as random no is {} and palyer choose {}".format(r1,player_input))
    

""" 
    Challenge 4    
    Let people play again and again until he guesses the right secret number 
"""
    
while(True):
    if(r1==player_input):
        print("WIN")
        break
    else:
        print("player loses as random no is {} and palyer choose {}".format(r1,player_input))
        print("PLAY AGAIN")
        player_input = int(input("enter the no"))

""" Challenge 5 Limit the number of guesses to maximum 6 tries  """ 
i=0
while(i<=7):
    if(r1==player_input):
        print("WIN")
        break
    elif(i==7):
        print("soo many unsuccessfull attempts")
        break
    else:
        print("player loses as random no is {} and palyer choose {}".format(r1,player_input))
        print("PLAY AGAIN")
        player_input = int(input("enter the no"))
    i+=1

""" Challenge 6     Print the number of tries left  """ 
i=0
while(i<=7):
    if(r1==player_input):
        print("WIN")
        break
    elif(i==7):
        print("soo many unsuccessfull attempts")
        break
    else:
        print("player loses as random no is {} and palyer choose {}".format(r1,player_input))
        print("PLAY AGAIN")
        print("playtime left {}".format(7-i))
        player_input = int(input("enter the no"))
        print()
    i+=1

"""
    FINAL
"""

r1 = random.randint(0,10)
print (r1)
player_input = int(input("enter the no"))
i=0
while(i<=7):
    if(r1==player_input):
        print("WIN")
        break
    elif(i==7):
        print("soo many unsuccessfull attempts")
        break
    else:
        if(player_input<0):
            print("TOO LOW")
        elif(player_input>11):
            print("TOO HIGH")
        print("player loses as random no is {} and palyer choose {}".format(r1,player_input))
        print("PLAY AGAIN")
        print("playtime left {}".format(7-i))
        player_input = int(input("enter the no"))
    i+=1


