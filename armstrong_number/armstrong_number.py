# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 17:59:13 2021

@author: hp
"""
#program to find out the armstrong numbers 


for i in range(100,1000):
       a=i//10
       b=a//10
       c=a%10
       a=i%10
       if a**3+b**3+c**3==i:
           print(i)
           print("number is armstrong")
 
           
def check(n):
    a=0
    org_n=n
    orginal_no=n
    Armstrong=0
    while n>0:
        a+=1
        n=n//10
    while org_n>0:
        Last_Digit = org_n % 10
        Armstrong  = Armstrong  + ((Last_Digit)**(a))
        org_n = (org_n //10)
    if orginal_no==Armstrong:
        print("true")
    else:
        print("false")

        
n=int(input())
check(n) 
    