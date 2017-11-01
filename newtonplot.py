# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:47:22 2015

@author: louiscarnec
"""

from numpy import *
from matplotlib.pyplot import *

def plotofx (S=0):
    x = linspace(-6,6,200)
    
    
    y = (x**2-S)
    
    figure() 
    
    plot(x, y) 
    
    grid(True)
    
     


print plotofx(0), savefig("plot_1.pdf")
print plotofx(5), savefig("plot_2.pdf")
print plotofx(10), savefig("plot_3.pdf")