# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 10:15:26 2021

@author: Leonardo
"""


def myfunction(*args, **kwargs):
    
    print(args)
    print(kwargs)
    
    
myfunction("Leo", "7", test="mykwargs!")