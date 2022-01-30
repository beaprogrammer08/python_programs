# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 17:09:39 2021

@author: hp
"""

n=int(input("enter the number:"))
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(n-j+1,end="")
        j=j-1
    print("\n")
    

n=int(input("enter the number:"))
for i in range(1,n+1):
    for j in range(i,0,-1):
        k=chr(ord("A")+n-j)
        print(k,end="")
        j=j-1
    print("\n")    
    
    
    
    