#!/usr/bin/python3

# Create func/class to print matrix size X/X 
# Fill it with Y mines 
# Mark mines as 'x' and mark empty cells as 0

# an example result:
# [ 0,  0, 'x', 'x']
# ['x', 0,  0,   0 ]
# [ 0,  0,  0,   0 ]
# [ 0, 'x', 0,  'x']
import numpy as np
import random

def minesweeper_generator(size,mines):
    list_coordinate=[]
    index=0
    while index<mines:
        x = int(random.randrange(0,size))
        y =  int(random.randrange(0,size))
        print(x,y)
        if((x,y) not in list_coordinate):
            list_coordinate.append((x,y))
            index=index+1
    print(list_coordinate)

    print('Implement me!')
    arr=[]
    if (size*size)<mines:
        print("Mines cannot be greater then the array matrix")
    else:
            for i in range(size):
                sub_arr=[]
                for j in range(size):
                    if ((i,j) in list_coordinate):
                        sub_arr.append("x")
                    else:
                        sub_arr.append(0)
                arr.append(sub_arr)     

    return arr

if __name__ == "__main__":
    for line in minesweeper_generator(4,5):
        print(line)
