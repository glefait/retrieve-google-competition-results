#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name='retrieve-google-competition-results',
    version='0.1.0',
    url='https://github.com/glefait/retrieve-google-competition-results',
    author="Guillem Lefait",
    author_email='guillem@datamq.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Description",
    long_description=readme,
    include_package_data=True,
    packages=['{}'.format(x) for x in find_packages('src')],
    package_dir={'': 'src'},
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'retrieve_google_competition_results=retrieve_google_competition_results.cli:main',
        ],
    },
    install_requires=[
        'click~=7.0',
        'requests'
    ],
)
