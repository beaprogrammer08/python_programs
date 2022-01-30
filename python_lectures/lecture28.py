# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 17:49:24 2021

@author: hp
"""
num=int(input("enter no"))
my_list=[3,4,5,6,7,8,9,10,11,12,13,14,15,16,18]
r=len(my_list)-1
l=0
while l<=r:
    m=(l+r)//2
    if my_list[m]==num:
        print(m)
        break
    elif my_list[m]>num:
        r=m-1
    

    elif my_list[m]<num:
        l=m+1
else:
    print(num,"is not in list")
    



num=int(input("enter no"))
my_list=[3,4,5,6,7,8,9,10,11,12,13,14,15,16,18]
r=len(my_list)-1
l=0
for a in my_list:
    m=(l+r)//2
    if my_list[m]==num:
        print(m)
        break
    elif my_list[m]>num:
        r=m-1
    

    elif my_list[m]<num:
        l=m+1
else:
    print("sorry")
    
my_list=[]
for a in input("enter the number:"):
    my_list.append(int(a))
print(my_list)   



num=int(input("enter no"))
my_list=[]
for b in input("enter the number:"):
    my_list.append(int(b))
my_list.sort()
r=len(my_list)-1
l=0
for a in my_list:
    m=(l+r)//2
    if my_list[m]==num:
        print(m)
        break
    elif my_list[m]>num:
        r=m-1
    

    elif my_list[m]<num:
        l=m+1
else:
    print("sorry")






my_list=[]
for a in input("enter the number:"):
    my_list.append(int(a))
my_list.sort()   
def binary_search(num):
    r=len(my_list)-1
    l=0
    for a in my_list:
        m=(l+r)//2
        if my_list[m]==num:
            print(l)
            break
        elif my_list[m]>num:
            r=m-1
    

        elif my_list[m]<num:
            l=m+1
    else:
       print("sorry")
binary_search(5)
    





































 

