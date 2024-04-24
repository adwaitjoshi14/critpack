""" setup file """
from setuptools import setup

setup(name='critical',
      version='0.0.1',
      description='find critical constants',
      maintainer='Adwait Joshi',
      maintainer_email='adwaitjo@andrew.cmu.edu',
      license='MIT',
      packages=['critical'],
      package_data={'critical': ['critical.xlsx']},
      scripts=[],
      long_description='''\
find critical constants and molar volume
==============
Handy functions for a project.''')
