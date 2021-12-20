my_str = "I am"

#Format String
print(my_str + ' {}'.format('Jim'))
print('This is new {} {}'.format('to', 'me'))
print('I am going to {l}'.format(l='london'))
print('I am going to {1} {2} {0}'.format('New york', 'London', 'Paris'))

#F String
name = 'test'
num = 25
print(f'My name is {name} : {num}')

#Floating point interpetation
result = 100/797
print(result)
print('The floating point result is: {r:1.4f}'.format(r = result))



