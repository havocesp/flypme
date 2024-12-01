#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""Flyp.me

File: /setup.py
Author: Havocesp <https://github.com/havocesp/Flyp.me>
Created: 2022-05-24
"""
from setuptools import find_packages, setup

setup(
    name='flipme',
    version='0.0.2',
    packages=find_packages(exclude=['.idea*', 'build*', f'{__package__}.egg-info*', 'dist*', 'venv*']),
    url='https://github.com/havocesp/flypme',
    license='UNLICENSE',
    packages_dir={'': 'flypme'},
    # keywords=__keywords__,
    author='havocesp',
    long_description='',
    description='Flip.me site API wraper.',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    # install_requires=
)
