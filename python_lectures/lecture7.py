# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 13:07:50 2021

@author: hp
"""

my_var="huiyiukjhuigytdchgnhn"

my_var.find("z")




my_var="************hello world****************"
my_var.strip("*")

my_var="          hello world                                       "
my_var.strip()



my_var="          hello world                                       "
my_var.rstrip()


my_var="          hello world                                       "
my_var.lstrip()


my_var="hello world"
my_var.startswith("h")

my_var="hello world"
my_var.endswith("d")

my_var="HeLLo WorlD"
my_var.swapcase()






my_string="hello world"
my_list=[]
type(my_list)

my_list=['hello world','hello world2',87259385,469,96]

len(my_list)

for i in my_list:
    print(i)
    for a in i:
        print(a)

my_list[0]
my_list[3]

my_list[-1]
my_list[-2]

my_list[0:5]
my_list[-1:-6:-1]

my_list[0]=''
print(my_list)

