# -*- coding: utf-8 -*-
from distutils.core import setup, Extension

# on déclare une extension pour distutils. Le nom du module
# que l'on passe en premier argument ('cfact') est important
# car c'est ce qui détermine le nom du fichier qui sera créé
# et donc conditionnera sous quel nom le module devra être
# importé. On doit donc avoir une cohérence entre :
#   - le nom de la bibliothèque partagée ('cfact.so')
#   - le nom de la fonction d'initialisation définie dans le
#     module d'extension C ('initcfact')
#   - le nom du module créée via Py_InitModule()

module1 = Extension('cfact',
                    sources = ['fact.c'])

setup (name = 'fact package',
       version = '1.0',
       description = 'This is a demo package',
       ext_modules = [module1])


