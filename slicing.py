my_str = "1234567890"

#start
print(my_str[2:]) #start includes the given index position
print(my_str[8:])

#stop
print(my_str[:5]) #stop doesn't includes the given index position

#start:stop
print(my_str[1:4])

#step
print(my_str[::2])

#start:stop:step
print(my_str[1:6:2])

#Technique to easily reverse the string in python
print(my_str[::-1])