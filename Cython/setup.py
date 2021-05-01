#setup.py
# from distutils.core import setup
# from Cython.Build import cythonize

# setup(ext_modules = cythonize('example_cython.pyx'))

import setuptools  # important
from distutils.core import setup
from Cython.Build import cythonize
setup(ext_modules=cythonize("sample.pyx", build_dir="build"),
                                           script_args=['build'], 
                                           options={'build':{'build_lib':'.'}})