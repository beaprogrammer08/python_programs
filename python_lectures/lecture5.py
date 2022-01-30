# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 17:42:41 2021

@author: hp
"""

my_string="hello world"

my_string[0]="k"


my_var='*'

for i in range(0,5):
    for j in range(0,i+1):
        print(my_var,end="")
    print("\n")    
for i in range(4,0,-1):
    for j in range(i,0,-1):
        print(my_var,end="")
    print("\n")    
        