# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:10:42 2021

@author: hp
"""

def getsum(x,y):
    return x+y
z=getsum(6,6)
print(z)




def getsum(x,y=10):
    return x+y
z=getsum(6,12)
print(z)



def getsum(x,y=10):# default parameters
    return x+y
z=getsum(6)
print(z)



def getsum(y=7,z=10):
    return y+z
z=getsum(6)
print(z)



x=10
def my_sum():
    x=20
    y=10
    return x+y
print(x)
z=my_sum()
print(z)
print(x)



x=10
def my_sum():
    x=20
    y=10
    print(x)
    return x+y
print(x)
z=my_sum()
print(z)
print(x)





