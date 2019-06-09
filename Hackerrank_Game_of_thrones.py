import math
import os
import random
import re
import sys

# Complete the gameOfThrones function below.

def gameOfThrones(s):
    dic_1 ={}
    counter = 0
    for key in s:
        keys = dic_1.keys()
        if key in keys:
            dic_1[key] += 1
        else:
            dic_1[key] = 1
    if len(s)%2==0:
        for key in dic_1.keys():
            if dic_1[key]%2!=0:
                return("NO")
        return("YES")
    else:
        for key in dic_1.keys():
            if dic_1[key]%2!=0:
                counter+=1
        if counter ==1:
            return"YES"
        else:
            return"NO"



       
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
