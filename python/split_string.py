#!/usr/bin/env python3
# task : split string into pairs of two characters
'''
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
'''
s = 'abcde'
def solution(s):
	
	if len(s)%2 != 0:
		ss = s+"_"	
	#list comprehension in more readable form
	# l = []
	# for i in range(0,len(ss),2):
	# 	l.append(ss[i]+ss[i+1])
	return [ss[i]+ss[i+1] for i in range(0,len(ss),2)]	

print(solution(s))