""" Install
"""
import os
from setuptools import setup, find_packages

PACKAGE_NAME = "surf.rdflib"
SUMMARY = (
    "surf.rdflib"
)
DESCRIPTION = (
    open("README.rst", 'r').read() + '\n\n' +
    open(os.path.join("docs", 'HISTORY.txt')).read()
)

VERSION = open('version.txt').read().strip()

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=SUMMARY,
    long_description=DESCRIPTION,
    author='Cosmin Basca',
    author_email='webadmin@eea.europa.eu',
    url='http://github.com/eea/surf.rdflib',
    license='MPL',
    packages=['surf_rdflib'],
    entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
    entry_points = {
        'surf.plugins.reader': 'rdflib = surf_rdflib.reader:ReaderPlugin',
        'surf.plugins.writer': 'rdflib = surf_rdflib.writer:WriterPlugin',
    },
    classifiers=[
      'Environment :: Console',
      'Intended Audience :: Developers',
      "Programming Language :: Python",
      'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'surf >= 1.0.0',
    ]
)
