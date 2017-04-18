from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pyCFL',
    version='0.1.0',
    description='package for reading CFL.ca API',
    long_description=readme,
    author='Andy Dyck',
    author_email='andrew@andrewdyck.com',
    url='https://github.com/NorthernLightsDataLab/pyCFL',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)