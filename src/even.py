# -*- coding: utf-8 -*-
"""
Created on Tue May 15 13:45:54 2018

@author: laetitialachat
"""

def isEven(number):
    if isinstance(number, str) and float(number)%2==0.0:
        return True
    elif isinstance(number, (int,float)) and float(number)%2==0.0:
        return True
    return False