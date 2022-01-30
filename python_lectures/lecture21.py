# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 09:39:23 2021

@author: hp
"""



     
n=int(input())

for i in range (1,n+1):
    for j in range(1,i+1):
        if (j==1 and j==i):
            print(i,end="")
        elif (j==1 or j==i):
            print(i-1,end="")
        else:
            print(0,end="")
    print("\n")        
            
    
    
    
    
    

n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        if j==1:
            print(1,end="")
        elif j==i:
            print(1,end="")
        else:
            print(2,end="")   
    print("")    
     
     

     
     








     