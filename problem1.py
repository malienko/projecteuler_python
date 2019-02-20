allsum = 0

for i in range(1000):
	if i % 5 == 0:
		allsum = allsum + i
	elif i % 3 == 0:
		allsum = allsum + i

print(allsum)
