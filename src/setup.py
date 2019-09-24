#!/usr/bin/env python

"""
qt test app
=====

"""
from setuptools import setup, find_packages
from os.path import dirname, abspath
import os.path

PARENT_DIR = dirname(abspath(__file__))

def get_version():
    return "0.1.0"

test_deps = [
    'pytest',
    'pytest-cov',
    'pytest-flake8',
    'flake8-bugbear',
    'pytest-black',
    'pytest-asyncio',
    'pytest-benchmark',
    'pytest-profiling',
    'pytest-leaks',
    'memory_profiler',
    'pytest-xdist',
    'teamcity-messages',
    'pdbpp',
]
extras = {
    'test': test_deps,
}

setup(
    name="testcases",
    version=get_version(),
    author="Ashley Camba Garrido",
    author_email="devs@viewpointsystem.com",
    url="https://github.com/viewpointsystem/docker-tegra-qt",
    description="QT test application",
    long_description=__doc__,
    packages=find_packages(exclude=("tests", "tests.*")),
    zip_safe=False,
    license="MIT",
    tests_require=test_deps,
    extras_require=extras,
    install_requires=[
        'attrs',
        'colorlog',
        'result',
        'pkgconfig',
        'quamash',
        'dbus-next'
        ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
