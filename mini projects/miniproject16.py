import math
import os
import random
import re
import sys



def jumpingOnClouds(c):
    jumps = 0
    it = 0
    pos = 1
    while pos != len(c): 
        if it + 2 == len(c):
            jumps += 1
            pos += 1
            it += 1
        elif c[it + 1] == 0 and c[it + 2] == 0:
            jumps += 1
            pos += 2
            it += 2
        elif c[it + 1] == 0 and c[it + 2] != 0:
            jumps += 1
            pos += 1
            it += 1
        elif c[it + 1] != 0 and c[it + 2] == 0:
            jumps += 1
            pos += 2
            it += 2
    return jumps

            
            
        
        


n = 7

c = [0,0,0,1,0,0]
print(jumpingOnClouds(c))
