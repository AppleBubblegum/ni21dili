from distutils.core import setup
from setuptools import find_packages
setup(name='ni21dili',
 version='0.1',
 author='DSSS',
 author_email='isa.baghirov@fau.de',
 packages=find_packages(),
 install_requires=['numpy', 'Pillow', 'ipywidgets'])