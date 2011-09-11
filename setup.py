# import std
import os
from os import path
import sys

# import third party

# import local
try:
    from setuptools import setup, find_packages
except ImportError:
    try:
        from ez_setup import use_setuptools
    except ImportError:
        print "can't find ez_setup"
        print "try: wget http://peak.telecommunity.com/dist/ez_setup.py"
        sys.exit(1)
    use_setuptools()
    from setuptools import setup, find_packages


# Append src directory to PYTHONPATH
sys.path.append(path.join(os.getcwd(), 'src'))

from seminode.utils.meta import __meta__

__package_data__ = [
    'README.rst',
    'Changelog',
    'License',
    'Makefile',
    'buildout.cfg'
]

setup(
    name=__meta__['name'],
    version=__meta__['version_str'],
    description=__meta__['description'],
    long_description=open('README.rst').read(),
    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
    keywords='seminode utils xml dict parser',
    author=__meta__['author'],
    author_email=__meta__['author_email'],
    url=__meta__['url'],
    download_url='',
    license=__meta__['license'],
    namespace_packages = ['seminode', 'seminode.utils'],
    package_dir = {'': 'src'},
    packages=find_packages('src', exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    package_data = {'': __package_data__},
    zip_safe=False,
    install_requires=[
       'setuptools',
    ]
)
