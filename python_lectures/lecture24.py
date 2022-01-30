# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 23:34:11 2021

@author: hp
"""

n=int(input())

for i in range(n,0,-1):
    for j in range(i,0,-1):
        if n%2==0:            
          if i%2==0:
            print(1,end="")
          else:
            print(0,end="")
        else:
            if i%2==0:
                print(0,end="")
            else:
                print(1,end="")
    print("\n")
          

    


n=int(input())
for i in range(0,n+1):
    for a in range(0,n-i):
        print(" ",end="")
    for b in range(1,i+1):
        print(b-i+n,end="")
    print("\n")
    

n=int(input())
for i in range(n,1,-1):
    for a in range(0,n-i):
        print(" ",end="")
    for b in range(1,i+1):
        print(b-i+n,end="")
    print("\n")      
for i in range(0,n+1):
    for a in range(0,n-i):
        print(" ",end="")
    for b in range(1,i+1):
        print(b-i+n,end="")   
    print("\n")
    
    
    
    
    
n=int(input("enter the number:"))
for i in range(0,n):
        for j in range(0,n):
            print(i+j+1,end="")
        print("\n")    
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    