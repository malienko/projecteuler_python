'''
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

# Initializing variables
sum_of_the_squares = 0 
square_of_the_sum = 0

# Sum of the Squares
for i in range(101):
	n = i**2
	sum_of_the_squares = sum_of_the_squares + n
	square_of_the_sum = square_of_the_sum + i

print("The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is " + str(square_of_the_sum**2 - sum_of_the_squares))
