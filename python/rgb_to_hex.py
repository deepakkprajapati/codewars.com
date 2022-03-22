#!/usr/bin/env python3
# task : RGB to HEX conversion
'''
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
'''
# fruits = ["mango" if i%3==0 else "orange" for i in range(10)]
# print(fruits)
r,g,b = 0,0,0


def solution(r,g,b):
	foo = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
	bar = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
	hexx = ''
	for _ in [r,g,b]:
		if _ >255:
			_ = 255
		if _ < 0:
			_ = 0
		print(f'item is {_}')
		q =  _ // 16
		rem =  _ % 16
		print(f'quo is {q} and rem is {rem}')
		hexx += f'{bar[foo.index(q)]}{bar[foo.index(rem)]}'
		print(f'hexx is {hexx}')
	return hexx



print(solution(r,g,b))