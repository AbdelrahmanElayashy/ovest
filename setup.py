#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = []

setup(
    author="Myovest",
    author_email='omartalal95@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    entry_points={
        'console_scripts': [
            'myovest=myovest.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='myovest',
    name='myovest',
    packages=find_packages(include=['ovest', 'ovest.acceleration',
                                    'ovest.alert', 'ovest.alert.gbs',
                                    'ovest.alert.gsm','ovest.database']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/myovest/myovest',
    version='0.1.0',
    zip_safe=False,
    scripts=['bin/script-program.py'],
    package_data={'ovest': ['data/cap_data.txt']},
)
