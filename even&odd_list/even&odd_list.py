# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 15:50:37 2021

@author: hp
"""
# even and odd list





i=input("enter the number:")
i=int(i)
even=[]
odd=[]
for a in range(1,i+1):
    if a%2==0:
        even.append(a)
    else:
        odd.append(a)

print("even=",even)
print("odd=",odd)        
        