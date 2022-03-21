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
# [-8700445, 8771853, 5090661, -8149067, -3972845, -5783021, -2720003, -5250345, -9424339, 8755105, 2877093, 1480085, 8939895, 3739733, -3685193, 1757573, -7711103, -1474481, 1079519, -5448157, -7994557, -3024437, -1277607, -5766009, -6795004, 346183, 8989297, -6517193, -3694973, 5211799, -4448521, -1811423]
# Expected: -6795004
# arr.append(99)

def find_outlier(integers):

	listisodd  = sum(arr)%2 == 0
	for item in arr:
		# if list is odd and current item is even then return the even
		if listisodd and  item %2 == 0:
			return item
		# if list is even (not odd) and current item is odd then return the odd
		elif not listisodd and item %2 != 0:
			return item

print(find_outlier(arr))