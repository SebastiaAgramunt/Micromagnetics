import os
import sys

from setuptools import setup, find_packages

base_dir = os.path.dirname(__file__)
src_dir = os.path.join(base_dir, 'mmag')
sys.path.insert(0, src_dir)

import mmag

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def get_requirements(requirements_path='requirements.txt'):
    with open(requirements_path) as fp:
        return [x.strip() for x in fp.read().split('\n') if not x.startswith('#')]


setup(
    name='mmag',
    version=mmag.__version__,
    description='A package to run micromagnetic simulations in python',
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author='Sebastia Agramunt Puig',
    lisense='',
    author_email='sebasvinaros@gmail.com',
    packages=find_packages(where='mmag', exclude=['tests']),
    package_dir={'': 'mmag'},
    install_requires=get_requirements(),
    setup_requires=['pytest-runner', 'wheel'],
    testsp_require=get_requirements('requirements.test.txt'),
    url='https://github.com/SebastiaAgramunt/Micromagnetics',
    classifiers=[
        'Programming Language :: Python :: 3.8.0'
    ],
)