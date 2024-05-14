from setuptools import setup, find_packages


# TO DO: replace concrete by abstract requirements
with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(

   name='discretehelpers',
   version='0.0.1',
   description='library for discrete mathematics',
   author='Watchduck',
   author_email='no@example.com',
   license='MIT',

   packages=find_packages(),
   install_requires=required

)
