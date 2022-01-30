# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 18:21:30 2021

@author: hp
"""

a="hello world"
print(a)
type(a)

a=True
type(a)

a=87359743
type(a)

a=8275.35
type(a)

a=17+2j
type(a)


a=input("enter your name:")
print(a)

a="65455"
a=int(a)
type(a)


#paridrome number



n=int(input())
original=n
reverse=0
while n>0:
    a=n%10
    reverse=reverse*10+a
    n=n//10
if original==reverse:
    print("true")
else :
    print("false")

