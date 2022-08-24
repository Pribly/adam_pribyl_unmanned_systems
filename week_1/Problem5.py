# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 11:18:03 2022

@author: adamp
"""
import math
def distance(x1,y1,x2,y2):
    return (math.sqrt(pow((x1-x2),2)+pow((y1-y2),2)))
val= distance(2,1,3,2)
print(val)