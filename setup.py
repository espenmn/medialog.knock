# -*- coding: utf-8 -*-
"""
This module contains  medialog.knock
"""
import os
from setuptools import setup, find_packages


version = '0.1'


setup(name='medialog.knock',
      version=version,
      description="A form",
      long_description='Form',
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='a creappy product',
      author='Espen Moe-Nilssen',
      author_email='espen at medialog no',
      url='http://github.com/espenmn/medialog.knock',
      license='gpl',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['medialog'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['collective.js.knockout',
      				'plone.api',
      				'setuptools',
      				],
      entry_points="""
      # -*- entry_points -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
