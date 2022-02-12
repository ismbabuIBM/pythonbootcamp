#get even number list function
even_num_list = list()
def even_num_funtion(num_list):
    #for
    for num in num_list:
        #if-else
        if num%2==0:
            even_num_list.append(num)
        else:
            pass
    #return the final list at the end of for loop
    return even_num_list

#function call
even_num_list_new = even_num_funtion([2,24,545,34,3,7,8])
print(even_num_list)#appended list
print(even_num_list_new)#receives output from return statement