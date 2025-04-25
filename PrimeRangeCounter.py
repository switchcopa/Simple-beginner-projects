from math import *

count = 0
min_range = 1
max_range = 5000

for num in range(min_range + 1, max_range + 1):
    isPrime = True
    for i in range(2, floor(sqrt(num)) + 1):
        if num % i == 0:
            isPrime = False 
            break 
    if isPrime: 
        count += 1 

print(count)