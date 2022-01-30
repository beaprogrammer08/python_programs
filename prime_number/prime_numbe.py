# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 14:07:04 2021

@author: hp
"""

# prime_number


x=input("enter the numbers:-")

x=int(x)
for i in range(2,x+1):
   for a in range(2,i):
        if i%a==0:
            print(i,"number is compostite")
            break
else:
      print(i,"number is prime")
      




x=input("enter the numbers:-")

x=int(x)
for a in range(2,x):
     if x%a==0:
          print(x,a,"number is compostite")
          break
else:
    print(x,"number is prime")
          