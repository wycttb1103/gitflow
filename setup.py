# -*- coding: utf-8 -*-
#ttt
# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='gitflow',
    version='0.1.0',
    description='Sample package for gitflow demo',
    long_description=readme,
    author='Yuchen Wu',
    author_email='ywu@aflac.com',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

