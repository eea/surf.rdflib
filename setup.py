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
    open(os.path.join("docs", 'HISTORY.rst')).read()
)

VERSION = open('version.txt').read().strip()

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=SUMMARY,
    long_description=DESCRIPTION,
    author='Cosmin Basca',
    author_email='webadmin@eea.europa.eu',
    url='http://plone.org/products/surf.rdflib',
    license='MPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['surf'],
    include_package_data=True,
    zip_safe=False,
    entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
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
