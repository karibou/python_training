from distutils.core import setup, Extension


setup(name='monpaquet',
      ext_modules=[Extension('modc', ['ext.c'])])
