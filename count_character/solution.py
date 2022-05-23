#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    sum=0
    if len(s)==1:
        #Only single character is repeating n times
        if s=='a':
            sum=sum+n
    else:
        div=n//len(s)
        string=s*div
        string=string+s[0:(n%len(s))]
        for i in range(len(string)):
            if string[i] == 'a':
                sum=sum+1
    return(sum)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
