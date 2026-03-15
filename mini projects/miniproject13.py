arr = [1,2,3,4,5]

big = 0
for i in arr:
    if i > big:
        big = i
    
arr.remove(big)

sec_big = 0
for i in arr:
    if i > sec_big:
        sec_big = i

print(sec_big)