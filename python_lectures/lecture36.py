# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 17:56:13 2021

@author: hp
"""



r=int(input("enter the column:"))
out=[]
for i in range(0,r):
    out.append([1]*(i+1))
for i in range(2,r):
    for j in range(1,i):
        out[i][j]=out[i-1][j-1]+out[i-1][j]
print(out)


