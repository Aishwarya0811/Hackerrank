
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
pairs ={}

def sockMerchant(n, ar):
    for i in ar:
        if i not in pairs.keys():
            pairs[i] = 1
        else:
            pairs[i]+=1
    counter = 0
    for value in pairs.values():
        counter+=value//2
    return counter


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    


    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()