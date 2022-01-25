my_list = list()
my_list2 = list()
my_list3 = list()
my_list4 = list()

my_list = [num for num in [24, 242,535]]
my_list2 = [num**2 for num in [23, 2, 4, 6]]
my_list3 = [num for num in [2, 4535, 353, 245, 55, 44] if num%2 == 0]
#makes a new list from existing list
print(my_list)
#makes a sqrt of num in existing list
print(my_list2)
#makes a even numbered list
print(my_list3)

#Nested for loop
for i in [2, 3, 6]:
    for j in [23, 24, 25]:
        my_list4.append(i*j)

print(my_list4)