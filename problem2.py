'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

# Initializing values
a = 1
b = 2
c = a + b

result = 0

# Stopping counting when numbers in the sequence hit 4000000
while c < 4000000:
	a = b
	b = c
	c = a + b
	if c % 2 == 0:
		result = result + c

result = result + 2 # from the initial b = 2
print("The sum of all even numbers under 4000000 in the Fibonacci sequence is " + str(result))
