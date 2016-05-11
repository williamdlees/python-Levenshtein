.. contents ::

This version is modified for my own purposes to allow a cutoff to be specified to distance().
If the optional cutoff value is specified, 
Levenshtein distances are only returned if the two strings differ by at most the cutoff
value: otherwise a value higher than the cutoff is returned, but this will not necessarily reflect the
true distance. This is a small hack which can save time if you need to compare
a lot of strings but are only interested in close matches.

Introduction
------------

The Levenshtein Python C extension module contains functions for fast
computation of

* Levenshtein (edit) distance, and edit operations

* string similarity

* approximate median strings, and generally string averaging

* string sequence and set similarity

It supports both normal and Unicode strings.

Python 2.2 or newer is required.

StringMatcher.py is an example SequenceMatcher-like class built on the top of
Levenshtein.  It misses some SequenceMatcher's functionality, and has some
extra OTOH.

Levenshtein.c can be used as a pure C library, too.  You only have to define
NO_PYTHON preprocessor symbol (-DNO_PYTHON) when compiling it.  The
functionality is similar to that of the Python extension.  No separate docs
are provided yet, RTFS.  But they are not interchangeable:

* C functions exported when compiling with -DNO_PYTHON (see Levenshtein.h)
  are not exported when compiling as a Python extension (and vice versa)

* Unicode character type used with -DNO_PYTHON is wchar_t, Python extension
  uses Py_UNICODE, they may be the same but don't count on it

Documentation
--------------

gendoc.sh generates HTML API documentation,
you probably want a selfcontained instead of includable version, so run
in ``./gendoc.sh --selfcontained``.  It needs Levenshtein already installed
and genextdoc.py.

License
-----------

Levenshtein can be copied and/or modified under the terms of GNU General
Public License, see the file COPYING for full license text.

Original Authors
-------

* Maintainer: `Mikko Ohtamaa <http://opensourcehacker.com>`_ - I am not actively doing anything
  for this, please feel free take over PyPi and Github administration

* David Necas (Yeti) <yeti at physics.muni.cz>

Modifier
--------

Modified and named LeveshteinMaxDist by William Lees <william at lees.org.uk>




