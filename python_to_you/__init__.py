__author__ = 'jacksonsr45@gmail.com'
__version__ = '0.1.0'

from os.path import dirname, basename, isfile, join
import sys
import glob

project_module = glob.glob(join(dirname(__file__), "*.py"))
__all__=[basename(f)[:-3] for f in project_module if isfile(f) 
            and not f.endswith('__init__.py')]