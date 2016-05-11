# Unit tests for LevenshteinMaxDist
# Based on tests from a blog by Matt Malone: https://oldfashionedsoftware.com/tag/levenshtein-distance/

import LevenshteinMaxDist as ld

def test():
  """
  It should work on empty strings
  >>> ld.distance(   "",    "")
  0
  >>> ld.distance(  "a",    "")
  1
  >>> ld.distance(   "",   "a")
  1
  >>> ld.distance("abc",    "")
  3
  >>> ld.distance(   "", "abc")
  3

  It should work on equal strings
  >>> ld.distance(   "",    "")
  0
  >>> ld.distance(  "a",   "a")
  0
  >>> ld.distance("abc", "abc")
  0

  It should work where only inserts are needed")
  >>> ld.distance(   "",   "a")
  1
  >>> ld.distance(  "a",  "ab")
  1
  >>> ld.distance(  "b",  "ab")
  1
  >>> ld.distance( "ac", "abc")
  1
  >>> ld.distance("abcdefg", "xabxcdxxefxgx")
  6

  It should work where only deletes are needed
  >>> ld.distance(  "a",    "")
  1
  >>> ld.distance( "ab",   "a")
  1
  >>> ld.distance( "ab",   "b")
  1
  >>> ld.distance("abc",  "ac")
  1
  >>> ld.distance("xabxcdxxefxgx", "abcdefg")
  6

  It should work where only substitutions are needed
  >>> ld.distance(  "a",   "b")
  1
  >>> ld.distance( "ab",  "ac")
  1
  >>> ld.distance( "ac",  "bc")
  1
  >>> ld.distance("abc", "axc")
  1
  >>> ld.distance("xabxcdxxefxgx", "1ab2cd34ef5g6")
  6

  It should work where many operations are needed
  >>> ld.distance("example", "samples")
  3
  >>> ld.distance("sturgeon", "urgently")
  6
  >>> ld.distance("levenshtein", "frankenstein")
  6
  >>> ld.distance("distance", "difference")
  5
  >>> ld.distance("java was neat", "scala is great")
  7

  It should honour the distance cutoff
  >>> ld.distance("example", "samplesasdfasdf", 3)
  4
  >>> ld.distance("sturgeon", "urgently", 2)
  3
  >>> ld.distance("abc", "abc", 4)
  0
  >>> ld.distance("", "difference", 2)
  3
  >>> ld.distance("java was neat", "scala is great", 9)
  7
  """	
	
if __name__=="__main__":
	import doctest
	doctest.testmod()