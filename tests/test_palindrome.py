# -*- coding: utf-8 -*-
"""
Created on Tue May  8 17:31:47 2018

@author: laetitialachat
"""

import sys
sys.path.insert(0, r'')

from src.palindrome import isPalindrome

def test_palindrome_string():
	assert isPalindrome("abba")
	assert isPalindrome("Abba")

def test_palindrome_int():
	assert isPalindrome(121)
	assert isPalindrome(1213)==False
