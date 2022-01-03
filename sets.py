#set
s = set()

print(type(s))
s.add(1)
s.add('a')
s.add('[1, 3, 7]')

print(s)
print(len(s))

#list
my_list = ['a', 'c', 'a', 'b', 'a', 'c', 1, 4, 3, 1]

#cast set to list
print(set(my_list))
print(set('Mississippi'))