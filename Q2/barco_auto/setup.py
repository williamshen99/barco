from setuptools import setup, find_packages

PACKAGE_VERSION = '1.0'


# dependencies
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name='test',
      version=PACKAGE_VERSION,
      description='tests',
      keywords='No',
      author='William Shen',
      author_email='',
      packages=find_packages(exclude=['tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=requirements
      )
