'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

# Brute Forcing

n = 20

while n % 1 != 0 or n % 2 != 0 or n % 3 != 0 or n % 4 != 0 or n % 5 != 0 or n % 6 != 0 or n % 7 != 0 or n % 8 != 0 or n % 9 != 0 or n % 10 != 0 or n % 11 != 0 or n % 12 != 0 or n % 13 != 0 or n % 14 != 0 or n % 15 != 0 or n % 16 != 0 or n % 17 != 0 or n % 18 != 0 or n % 19 != 0 or n % 20 != 0:
	n += 20

print(n) # Takes roughly 9 seconds to run
