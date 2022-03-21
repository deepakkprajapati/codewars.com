#!/usr/bin/env python3

# task:
'''
You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
FuXSab5aaV7UJis
dkprahapa
'''
# hiyacej277@songsign.com,dp010
# arr = [ x for x in range(-10 25 2)]
arr = [2, 4, 0, 100, 4, 11, 2602, 36]
# arr.append(99)

def find_outlier(integers):
	listisodd  = sum(arr)%2 == 0
	
	# if s%2 == 0: # means list is odd and return should be even
	# 	for bar in integers:
	# 		if bar% 2 == 0:
	# 			return bar
	# else: # list is even and return should be odd 
	# 	for bar in integers:
	# 		if bar% 2 != 0:
	# 			return bar
	for item in arr:
		# if list is odd and current item is even then return the even
		if listisodd and  item %2 == 0:
			return item
		# if list is even (not odd) and current item is odd then return the odd
		elif not listisodd and item %2 != 0:
			return item

print(find_outlier(arr))