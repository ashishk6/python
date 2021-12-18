# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
num=9
new_list = sorted(list(filter(lambda x: (x<= num) , my_list)))
print(new_list)
arr_len=len(new_list)
i=0
j=i+1

while j < arr_len:
    
    if (new_list[i]+new_list[j] == num):
        print('*'*10)
        print(i,j)
       
        print (new_list[i],new_list[j])
        print('*'*10)
    j+=1
    if j == arr_len:
        i+=1
        j=i+1
    
