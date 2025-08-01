from setuptools import setup, find_packages

with open('requirements.txt') as f:
    reqs = f.read().splitlines()

setup(
    name='wqsat_atcor',
    packages=find_packages(),
    version='0.1.0',
    description='Designed to apply atmospheric corrections to Sentinel-2 and Sentinel-3 imagery using the ACOLITE software.',
    author='CSIC',
    license='Apache License 2.0',
    install_requires=reqs)
