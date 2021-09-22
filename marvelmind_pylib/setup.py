
from distutils.core import setup

import sys
if sys.version_info < (3, 0):
	sys.exit('Sorry, python < 3.0 is not supported')

setup(
	name = "marvelmind_pylib",
	version = '0.0.1',
	packages = [''],
	package_data = {'': ['{dynamic file}']} # add dynamic file name
)
