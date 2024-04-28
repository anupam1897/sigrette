from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='Sigrette',
    version='v1.0.0',
    author='anupam1897',
    author_email='anupam1897@gmail.com',
    description='Flask App for testing and learning devops',
    packages=find_packages(),
    install_requires=requirements
)
