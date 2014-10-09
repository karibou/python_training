from distutils.core import setup, Extension

setup(
    name='cfact', 
    version='0.1',
    ext_modules=[Extension('cfact', ['cfact.c'])],
    )
