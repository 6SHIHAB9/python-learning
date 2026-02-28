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
    pairs = 0
    ref = []
    for i in ar:
        count = 0
        if i not in ref:
            for j in ar:
                if j == i:
                    count += 1
            if count % 2 == 0:
                pairs += count/2
            else:
                pairs += (count - 1)/2
        ref.append(i)
        


    return int(pairs)
        
    
        
        
    

n = 9

ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

result = sockMerchant(n, ar)

print(result)