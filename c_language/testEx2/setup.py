from distutils.core import setup, Extension

module1 = Extension('extest', sources=['testEx2.c'])

setup(name='extest',
      version='1.0',
      description='This is a test extension package',
      ext_modules=[module1])