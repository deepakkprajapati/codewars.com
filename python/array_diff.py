#!/usr/bin/env python3

# task :
'''
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]
'''
a = [1,2,2,2,2,2,2,3]
b = [2]

def array_diff(a, b):
	t=[]
	for x in a:
		if x not in b:
			t.append(x)
	return t

print(array_diff(a,b))