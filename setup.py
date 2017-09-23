#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'lxml',
    'beautifulsoup4',
    'requests',
    'requests[socks]',
    'pysocks',
    'gevent',
    'stem'
]

setup_requirements = [
    # TODO(SekouD): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'Sphinx',
    'docutils',
    'pytest',
    'pytest-cov',
    'Click>=6.0',
    'lxml',
    'beautifulsoup4',
    'requests',
    'requests[socks]',
    'pysocks',
    'gevent',
    'stem'
]

setup(
    name='lyricsmaster',
    version='2.4.0',
    description="LyricsMaster is a library for downloading lyrics from multiple lyrics providers. LyricWiki and other lyrics provider are available",
    long_description=readme + '\n\n' + history,
    author="SekouD",
    author_email='sekoud.python@gmail.com',
    url='https://github.com/SekouD/lyricsmaster',
    packages=find_packages(include=['lyricsmaster']),
    entry_points={
        'console_scripts': [
            'lyricsmaster=lyricsmaster.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='lyricsmaster',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Communications',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
