#!/usr/bin/env python3

# task:

'''
You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

#Examples:

Kata.getMiddle("test") should return "es"

Kata.getMiddle("testing") should return "t"

Kata.getMiddle("middle") should return "dd"

Kata.getMiddle("A") should return "A"
'''
sl = ['test', 'middle', 'a', 'testing' ]

def solution(s):
	l= len(s)
	# print(f'length of {s} is {l}')
	if l%2==0:
		return f'{s[l//2-1]}{s[l//2]}'
	else:
		return s[l//2]
	return s

for foo in sl:
	# print(f' foo is {foo}')
	print(solution(foo))