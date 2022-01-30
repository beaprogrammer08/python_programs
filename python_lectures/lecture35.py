# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 18:03:59 2021

@author: hp
"""

#sorting 

my_list=[2,23,34,22,1,65,54,223,21]
n=0
for i in range(0,len(my_list)):
    if my_list[n]>my_list[i]:
        my_list[i],my_list[n]=my_list[n],my_list[i]
n=1       
for j in range(1,len(my_list)):
    if my_list[n]>my_list[i]:
        my_list[j],my_list[n]=my_list[n],my_list[j]
n=2      
for j in range(2,len(my_list)):
    if my_list[n]>my_list[i]:
        my_list[j],my_list[n]=my_list[n],my_list[j]        
print(my_list) 
       
        
       
        
       
        
       

my_list=[2,23,34,22,1,65,54,223,21]
for n in range(0,len(my_list)):
    for i in range(n,len(my_list)):
        if my_list[n]>my_list[i]:
            my_list[i],my_list[n]=my_list[n],my_list[i]

print(my_list) 
              