'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

def sum_of_divisors(n):
	i = 0
	sum_of_divisors = 0
	for i in range(1,n):
		if n%i == 0:
			sum_of_divisors += i
			i = i
	return i+1, sum_of_divisors

all_tuples = []
for z in range(10_000):
	all_tuples.append(sum_of_divisors(z))

potentially_amicable_numbers = []
for tup in all_tuples:
	for tuples in all_tuples:
		if tup == tuples[::-1]:
			potentially_amicable_numbers.append(tup)

non_amicable_numbers = []

for i in potentially_amicable_numbers:
	if i[0] == i[1]:
		non_amicable_numbers.append(i)

amicable_numbers = set(potentially_amicable_numbers) - set(non_amicable_numbers)

answer = 0
for i in amicable_numbers:
	answer += i[0]

print(answer)
