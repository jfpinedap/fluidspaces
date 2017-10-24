#!/usr/bin/env python3

from setuptools import setup, find_packages


def readme():
    '''Get long description from readme file'''
    with open('README.rst') as f:
        return f.read()


setup(
    name='fluidspaces',
    use_scm_version=True,
    description='Navigate i3wm named containers',
    long_description=readme(),
    author='Peter Henry',
    author_email='me@peterhenry.net',
    url='https://github.com/mosbasik/fluidspaces',
    license='MIT',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    setup_requires=[
        'pytest-runner',
        'setuptools_scm',
    ],
    tests_require=[
        'pytest',
    ],
    entry_points={
        'console_scripts': [
            'fluidspaces = fluidspaces.__main__:main',
        ],
    },
    python_requires='~=3.6',
)
