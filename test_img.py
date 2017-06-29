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
	try:
		imgage_obj = img()
	except:
		pytest.fail("Unexpected Error in instantiation.")

def test_instantiation():
	assert func_instantiation() == 0
