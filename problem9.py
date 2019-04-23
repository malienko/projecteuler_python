'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

def find_pythagoeran_triplet(n):
	a = b = c = 1
	for i in range(n):
		a = i
		a_squared = a ** 2
		for i in range(n):
			b = i
			b_squared = b ** 2
			c_squared = a_squared + b_squared
			if c_squared > 0:
				if (c_squared**0.5).is_integer():
					c = c_squared**0.5
					c = int(c)
					triplet = a + b + c
					triplet = int(triplet)
					if triplet == 1000:
						if a < b < c :
							print(str(a) + " + " + str(b) + " + " + str(c) + " = " + str(triplet))
							product = a * b * c
	return product

product = find_pythagoeran_triplet(999) 

print(product) # Answer: 31875000
