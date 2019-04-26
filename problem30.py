'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 1**4 + 6**4 + 3**4 + 4**4
    8208 = 8**4 + 2**4 + 0**4 + 8**4
    9474 = 9**4 + 4**4 + 7**4 + 4**4

As 1 = 1**4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

big_sum = []
def fifthPowers(num):
	sum_nums = 0
	num = str(num)
	for i in range(len(num)):
		j = int(num[i])**5
		sum_nums += j
	if sum_nums == int(num):
		if int(num) > 1:
			big_sum.append(int(num))
	elif sum_nums != num:
		pass
	result = sum(big_sum)
	return result

for i in range(1_000_000):
	result = fifthPowers(i)

print(result) # 443839
