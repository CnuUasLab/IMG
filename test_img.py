#=======================================#
#										#
#	  Test file used to test this		#
#	    python build for img.py			#
#										#
# 		  Author: davidkroell		  	#
#										#
#=======================================#

import py, pytest
from img import img

def func_instantiation():
	return 0

def test_instantiation():
	assert func_instantiation() == 0
