'''
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

import numpy as np
import math
from datetime import datetime

start = datetime.now()

def is_prime(x):


    if x < 2:
        return False
    else:
        for n in range(2,x):
            if x % n == 0:
               return False
        return True

list_of_primes = []
top_limit = 10000
total = 0

arr = np.zeros((top_limit,1), dtype=bool)

for num in range(len(arr)):
	if num > 1:
		for i in range(2,int(math.sqrt(num)+1)):
			if (num % i) == 0:
				break
		else:
			arr[num,0] = 1

list_of_primes = np.where(arr[:,0]==1)[0]
list_of_primes = list_of_primes.tolist()

sequences = []
summations = []
most_consecutive_primes = []

for i in list_of_primes:
	for j in list_of_primes:
		ind1 = list_of_primes.index(i)
		ind2 = list_of_primes.index(j)
		k = list_of_primes[ind1:-ind2]
		if len(k) > 21:
			if len(k) > len(most_consecutive_primes):
				summation = np.sum(k)
				if summation > 900_000:
					if summation < 1_000_000:
						if is_prime(summation):
							most_consecutive_primes = k
							summations.append(summation)

if summations:
	print(max(summations)) # Answer: 997651

end = datetime.now()
delta_time = end-start
print(delta_time) # 0:00:48.028184
