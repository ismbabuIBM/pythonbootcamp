#1. Use for, .split(), and if to create a Statement that will print out words that start with 's':

from operator import le
from random import randint

st = 'Print only the words that start with s in this sentence'
s_str_list = list()

for word in st.split():
    if(word.startswith('s')):
        s_str_list.append(word)

print(s_str_list)

#2. Use range() to print all the even numbers from 0 to 10.
for num in range(0, 10, 2):
    print(num)

#3. Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
odd_list = list()
odd_list = [odd_num for odd_num in range(1, 50) if odd_num%3 == 0]
print(odd_list)

#4. Go through the string below and if the length of a word is even print "even!"
word_list = list()
st = 'Print every word in this sentence that has an even number of letters'

for word in st.split():
    if(len(word)%2 == 0):
        print('Even ' + word)

#5. Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
for num in range(1, 101):
    if num%3 == 0 and num%5 ==0:
        print('FizzBuzz')
        continue
    elif num%3 == 0:
        print('Fizz')
    elif num%5 == 0:
        print('Buzz')
    else:
        print(num)

#6. Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'
my_list = [word[0] for word in st.split()]
print(my_list)

    
