# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 21:40:11 2021

@author: hp
"""

a=83
b=873


print(a+b)


c=a+b

print(c)

print(a*b)
print(a**b)
print(a/b)
print(a-b)
print(a%b)
print(a*b%a)
print(a//b)

my_var="hello world"
 

my_var[0]
my_var[7]

my_var[0:9]
my_var[0:11]
my_var[-9:0]
my_var[:]
my_var[::-1]
my_var[-11:-1]
my_var[-10:-1]
my_var[-9:-1]


len(my_var)




string1=("ram and sham are brothers ")



print(string1[8:12]+string1[3:8]+string1[0:3]+string1[12:])



num=86358723958

if num%2==0:
    print("number is even")
    
    
else :
    print("number is odd ")    
    
    
day="monday"

if day=='monday': 
    print("HEAVY WORK")
elif day=="tuesday":
    print("laundry work")
elif day=="wednesday":
    print("free time")
else :
    print("invalid")
    
    
    
day=input("type day:-")
 

if  day=="monday":
    print("heavy work")
    
elif day=="saturday":
    print("hangout with friends") 
    
elif day=="sunday":
    print("free time")
    
else :
    print("work")
    
    
num=input("enter the number:")

num=int(num)

print(num)

if num%15==0:
    print("buzz frizz")
elif num%3==0:
      print("frizz")
      
elif num%5==0:
    print("buzz")      

    
    
else :
    print("not divisible ")
    
    
day=input("enter the day:")

salary=input("enter your salary :")


salary=int(salary)


if day=="sunday":
  if salary>20000:
      print("go to shopping")
  else :
      print("rest at home")
else :
    print("go to work")      
    
    
x=235

a=x//100 



b=x%10
b=b*100

c=x//10
d=c%10
d=d*10
  

print(b+d+a)






x=7348
a=x//1000
b=x%10
b=b*1000
c=x//10
d=c%10
d=d*10
e=c%100
f=e//10
f=f*100

print(a+b+d+f)