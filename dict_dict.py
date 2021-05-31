x=[{"id":1,"num": [25,30,31]},
{"id":11,"num": [21,22,23]},
{"id":12,"num": [1,21,31]}]
final_list=[]
for n in x:
    #print(n["num"])
    final_list=final_list+n["num"]
print(final_list)
final_list=list(set(final_list))
print(final_list)
my_dict={}
for list_val in final_list:
    arr=[]
    for n in x:
        if list_val in n["num"]:  
            arr.append(n["id"])
    #print(arr)
    my_dict[list_val]=arr
print(my_dict)
