my_list = [1, 2, 3, 4, 5]
i=0
j=0

while 5 > i:
    print(my_list[i])
    i = i+1

#pass continue break
while 5 > j:
    if j==0:
        pass
    j = j+1
    if j==3:
        continue
    if j==5:
        break
    print(my_list[j])
 