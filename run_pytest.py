# -*- coding: utf-8 -*-
"""
Created on Tue May  8 16:28:48 2018

@author: laetitialachat
"""

import pytest

#pytest.main() #analyse tests without production of a XML file summary
pytest.main(['--junitxml=results_xml/tests_output.xml']) #analyse tests with production of a XML file summary