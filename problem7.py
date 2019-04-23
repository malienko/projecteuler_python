'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

import numpy as np
import math
from datetime import datetime

start = datetime.now()

top_limit = 200000
total = 0

arr = np.zeros((top_limit,1), dtype=bool)

for num in range(len(arr)):
	if total == 10001:
		break
	elif num > 1:
		for i in range(2,int(math.sqrt(num)+1)):
			if (num % i) == 0:
				break
		else:
			arr[num,0] = 1
			total = np.sum(arr[:,0], axis = 0)

largest_prime = [x[-1] for x in np.where(arr[:,0]==1)]
end = datetime.now()

print(largest_prime[-1]) # Answer: 104743

delta_time = end-start
print(delta_time) # delta_time: 0:00:03.155708
