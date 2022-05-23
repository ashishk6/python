#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    arr=ar
    temp_dict={}
    for i in range(n):
        if arr[i] in temp_dict:
            temp_dict[arr[i]]=temp_dict[arr[i]]+1
        else:
            temp_dict[arr[i]]=1
    print(temp_dict)
    # sum of pairs of socks
    sum=0
    for i in temp_dict.values():
        #print(i)
        sum=sum+i//2
    return(sum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
