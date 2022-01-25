#for loop
my_list = [1, 2, 33, 24, 242, 2424]

for item in my_list:
    print('The items in the list are: ' + str(item))

for item in my_list:
    #check for even
    if item % 2 == 0:
        print('Even numbers in the list are {}'.format(str(item)))
    else:
        print(f'Odd numbers in the list are: {item}')

sum = 0
for item in my_list:
    #sum of all numbers in the list
    sum = sum + item

print(f'The sum of items in the list are: {sum}')

my_str = 'This is Python'
store_list = list()
#string to list
for letter in my_str:
    store_list.append(letter)

print(store_list)

#tuple in for loop
tup = (1, 2, 3)
for t in tup:
    print(t)

#list of tuples in for loop
new_list = [(12, 23, 3), ('a', 'b', 'c')]


for a,b,c in new_list:
    print(a)
    print(b)
    print(c)

#dictionary in for loop
d = {'xxx':000, 'yyy':111, 'zzz':222}
for key,value in d.items():
    print(key, value)









