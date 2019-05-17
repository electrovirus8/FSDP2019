# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:27:58 2019

@author: Mayank Jain
"""


"""
Hands On 1
"""
# Create a list of number from 1 to 20 using range function. 
# Using the slicing concept print all the even and odd numbers from the list 

list1 = []
for item in range(1,21):
    list1.append(item)
print(list1) 

print(list1[0:19:2])
print(list1[1:20:2])

"""
list2 = [1,2,3,4,5]
list3 = []
for item in list2:
    list3.append(item)
list3.reverse()
"""

"""
Hands On 2
"""
# Make a function to find whether a year is a leap year or no, return True or False 

def leapyear(a):
    if(a%400==0):
        return print("is a leap year")
    elif(a%100==0):
        return print("is not a laep year")
    elif(a%4==0):
        return print("is a leap year")
    else:
        return print("not a leap year")

year1 = int(input("enter the year"))
leapyear(year1)
    
"""
Hands On 3
"""
# Make a function days_in_month to return the number of days in a specific month of a year

def days(a):
    if (a=="jan" or a=="march" or a=="may" or a=="july" or a=="agust" or a=="oct" or a=="dec"):
        return print("31")
    elif(a=="feb"):
        return print("28")
    else:
        return print("30")
month = str(input("enter the month"))
days(month)

"""
Code Challenge
  Name: 
    Vowels Finder
  Filename: 
    vowels.py
  Problem Statement:
    Remove all the vowels from the list of states  
  Hint: 
    Use nested for loops and while
  Input:
    state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
  Output:
    ['lbm', 'clfrn', 'klhm', 'flrd']
    
"""



list = ["mayank","sahil","rohit"]

state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']

vowels = "AEIOUaeiou"
list1 = []
temp=[]
for item in state_name:
    if len(temp)>0:
        temp=[]
    for i in item:
        if i not in vowels:
            temp.append(i)
    list1.append("".join(temp))
print (list1)


"""for item in state_name:
    k=0
    j=0
    lenth=len(item)
    if(j<=len):
        for i in item:
            if i not in vowels:
                list1.append(i)
            print("".join(list1))
            j+=1
    else:
        k=k+1
        continue

"""

"""
list1 = list(state_name[0])
print(list1)
for vowels in list1:
    list1.remove(vowels)
print(list1)
temp1 = "".join(list1)
print(temp1)


list1 = list(state_name[0])
print(list1)

for vowels in list1:
    list1.remove(vowels)
print(list1)

temp1 = "".join(list1)
print(temp1)

temp = str(list1)
print(temp)
type(temp)
list3 = []
list3 = list3.append(list1)
print(list3)

for item in range(0,8):
    print("*"*item)

help(list.append)

   
   """ 
   



"""
Code Challenge
  Name: 
    Pattern Builder
  Filename: 
    pattern.py
  Problem Statement:
    Write a Python program to construct the following pattern. 
    Take input from User.  
  Input: 
    5
  Output:
    Below is the output of execution of this program.
      * 
      * * 
      * * * 
      * * * * 
      * * * * * 
      * * * * 
      * * * 
      * * 
      * 
"""
"""
i = int(input("input rows"))
j = int((i/2))
for i in range(0,j+1):
    print("*"*i)
k=int(((i/2)+1)+1)
for i in range(k+1,i+2):
    print("*"*k)
    k=k-1
"""    

i = int(input("input rows"))
for i in range(0,i):
    print("*"*i)
j=i-1
while j>0:
    print("*"*j)
    j=j-1





for i in range(i-1,0,-1):









"""
Code Challenge
  Name: 
    Pallindromic Integer
  Filename: 
    pallindromic.py
  Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, 
    then you need to print True else print False.
    (Take Input from User)  
  Hint: 
      A palindromic number or numeral palindrome is a number that remains the same
      when its digits are reversed. 
      Like 16461, for example, it is "symmetrical"
      Shorter logic can be developed using any and all and List comprehension
  Input: 
    12 9 61 5 14
  Output:
    True

"""

str = "12 9 61 5 14"
list5 = str.split()
print(list5)
for i in range(0,len(list5)):
    list5[i]=int(list5[i])
print(list5)

#temp = list(list5)
#print(temp)
#temp.reverse()
#print(temp)
for i in list5:
    if(i>=0):
        temp = i
        #print(temp)
        Reverse = 0    
        while(temp > 0):    
            Reminder = temp %10    
            Reverse = (Reverse *10) + Reminder    
            temp = temp //10
        #print(Reverse)
        if (i==Reverse):
                    print("one of the no. is a pallendrom")
                    break
        else:
            continue
    else:
        print ("no no. is pallendrom or one of the no. is naeagive no.")
        break

help(str.split)

"""
str7="aba"
len(str7)
for i in range()
"""



"""
Code Challenge
  Name: 
    Pangram
  Filename: 
    pangram.py
  Problem Statement:
    Write a Python function to check whether a string is PANGRAM or not
    Take input from User and give the output as PANGRAM or NOT PANGRAM.
  Hint:
    Pangrams are words or sentences containing every letter of the alphabet at least once.
    For example: "The quick brown fox jumps over the lazy dog"  is a PANGRAM.
  Input: 
    The five boxing wizards jumps.
  Output:
    NOT PANGRAM
"""

string1 = "The quick brown fox jumps over the lazy dog"
"""
list2 =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] 
len(list2)
for item in list2:
    #print(item)
    if (item in string1):
        list2.remove(item)
print(list2)

#len(list2)
        
if(len(list2)==0):
    print("string is PANGRAM")
else:
    print ("not a PARAGRAM") 
    
"""

string1 = "The quick brown fox jumps over the lazy dog"
string2 = "qwertyuiopasdfghjklzxcvbnm"

for char in string2:
    if char not in string1:
        flag = 0
    else:
        flag = 1
if (flag==1):
    print("is a PARAGRAM")
else:
    print("not a PARAGRAM")
    
    
    

"""
Code Challenge
  Name: 
    Bricks
  Filename: 
    bricks.py
  Problem Statement:
    We want to make a row of bricks that is target inches long. 
    We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
    Make a function that prints True if it is possible to make the exact target 
    by choosing from the given bricks or False otherwise. 
    Take list as input from user where its 1st element represents number of small bricks, 
    middle element represents number of big bricks and 3rd element represents the target.
  Input: 
    2, 2, 11
  Output:
    True
"""


#list6 = list(input("enter elements is list"))

list1 =[]
for i in range(0,5):
    element = int(input("enter the element in str"))
    list1.append(element)





input_string = input("Enter a list element separated by space ")
list  = input_string.split()

small = int(list[0])
big = int(list[1])
target = int(list[2])
   
small_val = 1
big_val = 5
x,y = divmod(target,big_val)

#print(x,y)

if (x<=big and y<=small):
    print("true")
else:
    print("false")




"""
Code Challenge
  Name: 
    Reverse Function
  Filename: 
    reverse.py
  Problem Statement:
    Define a function reverse() that computes the reversal of a string.
    Without using Python's inbuilt function
    Take input from User  
  Input: 
    I am testing
  Output:
    gnitset ma I  
"""

def reverse(a):
    str1 = []
    string = list(a)
    length = len(string)
    for item in range(0,length):
        temp = string.pop()
        str1.append(temp)
    #print(str1)
    a= "".join(str1)
    return a

reverse("hello my name is mayank")

"""
Code Challenge
  Name: 
    Translate Function
  Filename: 
    translate.py
  Problem Statement:
    Write a function translate() that will translate a text into "rövarspråket" 
    Swedish for "robber's language". 
    That is, double every consonant and place an occurrence of "o" in between. 
    Take Input from User  
  Input: 
    This is fun
  Output:
    ToThohisos isos fofunon  
"""
str3 = input("enetr teh string")
list3 = list(str3)
list4 = []
str = "AEIOUaeiou"
for item in list3:
    if item not in str:
        list4.append(item+"O"+item)
    else:
        list4.append(item)
list4 ="".join(list4)
print(list4)


"""
Code Challenge
  Name: 
    Operations Function
  Filename: 
    operation.py
  Problem Statement:
    Write following functions for list operations. Take list as input from the User
    Add(), Multiply(), Largest(), Smallest(), Sorting(), Remove_Duplicates(), Print()
    Only call Print() function to display the results in the below displayed 
    format (i.e all the functions must be called inside the print() function 
    and only the Print() is to be called in the main script)

  Input: 
    5,2,6,2,3
  Output:
    Sum = 18
    Multiply = 360
    Largest = 6
    Smallest = 2
    Sorted = [2, 2, 3, 5, 6]
    Without Duplicates = [2, 3, 5, 6]  
"""

def operation(a):
    list4 = []
    add=0
    for item in a:
        add = add+item
    list4.append(add)
       
    mul=1
    for item in a:
        mul = mul*item
    list4.append(mul)
    
    large=0
    for item in a:
        if item>large:
            large=item
    list4.append(large)
    
    small=a[0]
    for item in a:
        if item<=small:
            small=item
    list4.append(small)
    
    sorting =a.sort()
    print(sorting)
    list4.append(sorting)
    
    """dub = [sorting[0]]
    for item in sorting:
        if (sorting.index(item)==0):
            continue
        elif()
    """
    a=list(list4)
    return a

a = [5,2,6,2,3]
ans = operation(a)
print(" Sum = {} \
    Multiply = {}\
    Largest = {}\
    Smallest = {}\
    Sorted = {} ".format(ans[0] , ans[1], ans[2], ans[3],ans[4]))


"""
Code Challenge
  Name: 
    Sorting
  Filename: 
    sorting.py
  Problem Statement:
    You are required to write a program to sort the (name, age, height) 
    tuples by ascending order where name is string, age and height are numbers. 
    The tuples are input by console. The sort criteria is:
    1: Sort based on name;
    2: Then sort based on age;
    3: Then sort by score. 
    The priority is that name > age > score
  Input: 
    Tom,19,80
    John,20,90
    Jony,17,91
    Jony,17,93
    Json,21,85
  Output:
    [('John', 20, 90), ('Jony', 17, 91), ('Jony', 17, 93), ('Json', 21, 85), ('Tom', 19, 80)]
"""

list5 = []






"""
Code Challenge
  Name: 
    Centered Average
  Filename: 
    centered.py
  Problem Statement:
    Return the "centered" average of an array of integers, which we'll say is 
    the mean average of the values, except ignoring the largest and 
    smallest values in the array. 
    If there are multiple copies of the smallest value, ignore just one copy, 
    and likewise for the largest value. 
    Use int division to produce the final average. You may assume that the 
    array is length 3 or more.
    Take input from user  
  Input: 
    1, 2, 3, 4, 100
  Output:
    3
"""






        



















   
   
   