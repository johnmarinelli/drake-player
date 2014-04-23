from distutils.core import setup, Extension

consolemanip = Extension('ConsoleManip', sources = ['consolemanip.c'])

setup(name='ConsoleManip',
	  version='1.0',
	  description='C extension for some simple console manipulation in *nix systems',
	  ext_modules=[consolemanip])

