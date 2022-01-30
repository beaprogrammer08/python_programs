# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 17:24:17 2021

@author: hp
"""

my_list=[(1,2,100),(5,6,100),(10,11,100)]
my_list1=[]
for item in my_list:
    item_1=item[0:2]+(10,)
    print(item_1)
    my_list1.append(item_1)    
    print(my_list1)






string_1="                 hello        world           python"

string2=string_1.strip()
my_list=string2.split()
print(my_list)
my_list.reverse()
string3=" ".join(my_list)
print(string3)