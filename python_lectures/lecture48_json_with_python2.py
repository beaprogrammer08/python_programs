# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 21:59:25 2022

@author: hp
"""

import json 
from urllib.request import urlopen

with urlopen("https://gist.github.com/anubhavshrimal/75f6183458db8c453306f93521e93d37.js") as response:
    source=response.read()
print(source)

data=json.loads(source)
print(json.dumps(data,indent=2))