#!/usr/bin/env python3
# Find the odd int:
# task:
'''
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).


'''
def oddinit(a):
	l= []
	
	# d= {}
	# # creat an empty dictionary with k:v as num:no_of_its_occurrences
	# for foo in a:
	# 	if foo not in d:
	# 		d[foo] = a.count(foo)
	# # check if in k:v value is odd then return it 
	# for foo,bar in d.items():
	# 	if bar%2 != 0:
	# 		print(f'result is {foo}')

	# fast and efficient
	for foo in a:
		if foo not in l:
			if a.count(foo)%2 != 0:
				print(foo)
			l.append(foo)

a = [9,1,9,1,9,4,4,9,4]
oddinit(a)