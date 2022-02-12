import math
from tokenize import String
from turtle import pen

#Math and arithmetic operations
print(4 * (6 + 5))
print(4 * 6 + 5)
print(4 + 6 * 5 )

print(type(3 + 1.5 + 4))

print('The square root is: ' + str(math.sqrt(10)))
print('The square is: ' + str(math.pow(10, 2)))

s = 'hello'
# Print out 'e' using indexing
print(s[1])
# Reverse the string using slicing
print(s[::-1])
# Given the string hello, give two methods of producing the letter 'o' using indexing.
print(s[-1])
print(s[4])

l = list()
l.append(0)
l.append(0)
l.append(0)
print(l)

l1 = [0] * 3
print(l1)

list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye' 
print(list3)

#sort the list
list4 = [5,3,4,6,1]
print(sorted(list4))

#Using keys and indexing, grab the 'hello' from the following dictionaries:
d = {'simple_key':'hello'}
# Grab 'hello'
print(d['simple_key'])
print(d.values)

d = {'k1':{'k2':'hello'}}
# Grab 'hello'
print(d['k1']['k2'])

# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
#Grab hello
print(d['k1'][0]['nest_key'][1][0])

# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

#How do you create a tuple?
t = ('a', 'b', 'c')
print(type(t))

#Use a set to find the unique values of the list below:

list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))

#What is the boolean output of the cell block below?

# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
print(l_one[2][0] >= l_two[2]['k1'])

#string slicing
str1 = 'New Text'
print(str1[::-1])
print(str1[4::])

#list slicing
new_list = [23, 24, 354, 355]
print(new_list[::-1])
print(new_list[0::2])