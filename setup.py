from distutils.core import Extension, setup

setup(ext_modules=[Extension("pymyarray", ["pymyarray.c"])])
