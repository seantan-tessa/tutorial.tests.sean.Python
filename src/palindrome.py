# -*- coding: utf-8 -*-
"""
Created on Tue May 15 13:45:54 2018

@author: laetitialachat
"""

def isPalindrome(word):
    if str(word).lower()==str(word)[::-1].lower():
        return True
    return False