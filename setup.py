#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from setuptools import setup, find_packages
import re

# load version form _version.py
VERSIONFILE = "pyandor/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

# module

setup(name='pyandor',
      version=verstr,
      author="Keisuke Fujii",
      author_email="fujii@me.kyoto-u.ac.jp",
      description=("Python library to control Andor Cameras"),
      license="BSD 3-clause",
      keywords="camera",
      url="http://github.com/fujiisoup/pyandor",
      packages=['pyandor'],
      package_dir={'pyandor': 'pyandor/Camera'},
      py_modules=['pyandor.__init__'],
      test_suite='tests',
      install_requires="""
        """,
      classifiers=['License :: OSI Approved :: BSD License',
                   'Natural Language :: English',
                   'Operating System :: MacOS :: MacOS X',
                   'Operating System :: Microsoft :: Windows',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python :: 3.6',
                   'Topic :: Scientific/Engineering :: Physics']
      )
