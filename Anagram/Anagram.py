
import math
import os
import random
import re
import sys


# Complete the anagram function below.
def anagram(s):
    if len(s) % 2 == 0:
        f = list(s[:len(s)//2])
        se = list(s[len(s)//2:])
        for i in f:
            if i in se:
                se.remove(i) 
        return len(se)    
    else:
        return -1
   
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
