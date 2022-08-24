# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 10:00:28 2022

@author: adamp
"""

#% Import stuff here
##import matplotlib.pyplot as plt
#%%  imports matrix operations
import numpy as np 


def nodeanalysis(x,Xmin,rangex,y,Ymin,gridspace):
    #%equation to give desired value given any parameter
    return (((x-Xmin)/gridspace)+(((y-Ymin))*rangex)/gridspace)
Xmax=10
gs=.5
rangex=(Xmax/gs)+1
xarray=np.arange(0,rangex)
length=len(xarray)
val=nodeanalysis(1,0,length,1,0,gs)
print(val)
