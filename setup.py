from setuptools import setup, find_packages
import os

from distutils.core import Extension

version = '0.10.2'

extLevenstheinMaxDist = Extension('LevenshteinMaxDist',
                           sources = ['Levenshtein.c'],
                           )

setup(name='python-LevenshteinMaxDist',
      version=version,
      description="Python extension computing string distances and similarities with hack for max distance",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='string Levenshtein comparison',
      author='Mikko Ohtamaa',
      author_email='mikko@opensourcehacker.com',
      url='http://github.com/miohtama/python-Levenshtein',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=[],
      include_package_data=True,
      zip_safe=False,
      ext_modules = [extLevenstheinMaxDist],
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
