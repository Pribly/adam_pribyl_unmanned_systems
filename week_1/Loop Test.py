# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 09:44:53 2022

@author: adamp
"""
#% Import stuff here
import matplotlib.pyplot as plt

#%%  imports matrix operations
import numpy as np 
#%% makes list of x values from 0-10 called np
x_list= list(np.arrange(0,10))
y_list = list(np.arrange(10,20))
##basic for Loop
print("og method")
for i in range(0,len(x_list)):
    print("x is ", x_list[i],"y is ", y_list[i])
    
    
##duck typing short hand
print("\n")
print("duck typing")
for x,y in zip(x_list,y_list):
    print("x and y are: ",x,y)
    
## I need an index counter, as well as go through both x and y components
for i, (x,y) in enumerate(zip(x_list,y_list)):
    print("i,x, and y are ",i, x, y)


## HOw to plot
plt.plot(x_list,y_list)