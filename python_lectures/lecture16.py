# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 22:18:02 2021

@author: hp
"""

x1=int(input("enter the x center:"))
y1=int(input("enter the y center:"))
r=int(input("enter the  radius:"))
n1=int(input("enter the x point:"))
n2=int(input("enter the y point:"))
if ((n1-x1)**2+(n2-y1)**2)<r**2:
    print("point is inside the circle")    
elif ((n1-x1)**2+(n2-y1)**2)==r**2:
    print("point is on the circle")
elif ((n1-x1)**2+(n2-y1)**2)>r**2:
    print("point is outside the circle")    
    
    
    
    
    
    
my_string=input("enter your character:")
for item in my_string:
     if item.isupper()==True:
         print(item,"",item.lower())
     elif item.islower()==True:
         print(item,"",item.upper())
        
         
         
n=int(input("enter the 6 digit number:"))
a=n//1000
b=a%10
if b%2==0:
    if n%16==0:
         print("number id divible by 16")
else:
       z=n%1000
       out=z+8
       g=n%100
       y=z//10
       i=y*4+g
       if out%16==0:
           print("number is divible by 16")
       elif i%16==0:
           print("divisible by 16")
       else:
           print("not")
       
    
             
     
         
         
x=int(input("enter the number:"))
a=x%10000
b=a//1000
if b%2==0:
    print("number is even")
else:
    print("number is odd")    
    
    
    
    
n=int(input("enter the number:"))
a=str(n**2)
n=str(n)
if a.find(n)==True:
    print("number is automorphic")
else:
    print("number is not automorphic")         