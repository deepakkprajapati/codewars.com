#!/usr/bin/env python3
# task:
'''
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
'''
def shortestword(s):
	a =min([ len(x) for x in s.split() ] )
	print(a)

shortestword("bitcoin take over the world maybe who knows perhaps")
