# -*- coding: utf-8 -*-
"""
Created on Tue May  8 17:31:05 2018

@author: laetitialachat
"""

import sys
sys.path.insert(0, r'')

from src.even import *

def test_even_numerical():
	assert isEven(12)
	assert isEven(12.0)
	assert isEven(13) == False
	assert isEven(13.5) == False

"""def test_even_string():
	assert isEven("12")
	assert isEven("12.0")
	with pytest.raises(ValueError):
		isEven("abc")"""
