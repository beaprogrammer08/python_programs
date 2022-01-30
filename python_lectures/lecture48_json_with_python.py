# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 15:20:29 2022

@author: hp
"""

import json
student='''
{
    "STUDENTS":[

{
    "name":"DUPESH",
    "class":"1st year",
    "id":2110990477
},
{
    "name":"RAM",
    "class":"1st year",
    "id":2110990478
},
{
    "name":"RIYA",
    "class":"1st year",
    "id":2110990479
},
{
    "name":"RAHUL",
    "class":"1st year",
    "id":2110990475
},
{
    "name":"SHAM",
    "class":"1st year",
    "id":2110990476
}
    ]
}
'''

data=json.loads(student)
print(data)

my_list=[]
for people in data["STUDENTS"]:
    my_list.append(people['name'])
print(my_list)


for person in data["STUDENTS"]:
    del person["class"]
    
my_str=json.dumps(data) 
print(my_str)  



for person in data["STUDENTS"]:
    del person["class"]
    
my_str=json.dumps(data ,indent=2) 
print(my_str)  


for person in data["STUDENTS"]:
    del person["class"]
    
my_str=json.dumps(data ,indent=2,sort_keys=True) 
print(my_str)  
















    
