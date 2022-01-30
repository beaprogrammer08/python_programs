# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 23:25:51 2022

@author: hp
"""

a=int(input("enter the number:"))
b=int(input("enter the number:"))
my_list=[]
my_list2=[]
my_list1=[]
for i in range(1,a+1):
    if a%i==0:
        my_list.append(i)

for i in range(1,b+1):
    if b%i==0:
        my_list1.append(i)
for a in my_list:
    if a in my_list1:
        my_list2.append(a)
my_list2[-1]




a=int(input("enter the number:"))
b=int(input("enter the number:"))
my_list=[]
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        my_list.append(i)
my_list[-1]        



def gcd(m,n):
    if m<n:
        (m,n)=(n,m)
    if (m%n)==0:
        return(n)
    else:
        diff=m-n
        return(gcd(max(n,diff),min(n,diff)))

gcd(56,15)







def f(x):
    d=0
    while x >= 1:
        (x,d) = (x/7,d+1)
    return(d)
f(3456)



def g(m,n):
    res = 0
    while m >= n:
        (res,m) = (res+1,m/n)
    return(res)

g(375,4)

def mys(m):
  if m == 1:
    return(1)
  else:
    return(m+mys(m-1))
mys(-6)







def h(n):
    s = 0
    for i in range(2,n):
        if n%i == 0:
           s = s+i
    return(s)
h(60)-h(45)