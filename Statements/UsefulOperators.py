#range (start, stop, step)
l = list()
for num in range(1, 11, 2):
    l.append(num)
print(l)

#enumerate
name = 'Babu'
for index, letter in enumerate(name):
    print(index, letter)
    print('\n')

#zip
l1=[1, 2, 3]
l2 = ['i', 'j', 'k']
l3 = [100, 200, 300, 400, 500]

for i1, i2, i3 in zip(l1, l2, l3):
    print(i1, i2, i3)

print(list(zip(l1, l2, l3)))

#in
d = {'name1':'Test', 'name2':'Hello', 'name3':'John'}

if 'John' in d.values():
    print('John is in the list')

#min
print(min(l3))

#max
print(max(l3))

#random
from random import shuffle
#shuffle returns nothing
shuffle(l3)
print(l3)

#randomint
from random import randint
print(randint(232, 242424))

#input
num = int(input('Please enter your fav number: '))
print(num)
