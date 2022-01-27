# -*- coding: utf-8 -*-
"""
Created on 1/26/2022

@author: Adrian Jimenez
"""

i = [[3,4,5,6]]
j = [num[::-1] for num in i]


'''
Problem Set 1: Problem 1
'''
s = 'azcbobobegghakl'
vowels = 0
for letter in s:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        vowels += 1
print(vowels)

'''
Problem Set 1: Problem 2 
'''
s = 'obobobbobsnboobobob'
bob = 0 
i = 0
j = 3
while j != len(s)+1:
    if s[i:j] == 'bob':
        bob += 1
        i+=1
        j+=1
    else:
        i+=1
        j+=1
print('Number of times bob occurs is: ' + (str(bob)))

'''
Problem Set 1: Problem 3 
'''
s = 'azcbobobegghakl'
res = ''
c = ''
for char in s:
    if (c == ''):
        c = char
    elif (c[-1] <= char):
        c += char
    elif (c[-1] > char):
        if (len(res) < len(c)):
            res = c
            c = char
        else:
            c = char
if (len(c) > len(res)):
    res = c
print('Longest substring in alphabetical order is: ', res)
