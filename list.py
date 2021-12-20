my_list = ['Test', 1, 80.797]
char_list = ['f', 'n', 'a', 'h', 't']
test = 'mytest'

#append
my_list.append('Hello')

#pop
my_list.pop(1)

#Lists are mutable/can be changed
a = my_list[2]
my_list[2] = a.upper()
print(my_list)

#sort
char_list.sort()
sorted_list = char_list
print(sorted_list)

#reverse
char_list.reverse()
reversed_list = char_list
print(reversed_list)

#length
print(len(my_list))

#capitalize
print(char_list[2].upper())
print(test[2].upper())

#string append
test = test + 'a';
print(test)

#change the value of list
char_list[0] = 'k'
print(char_list)

#Cannot change string value at the index position
#test[0] = 'm'
