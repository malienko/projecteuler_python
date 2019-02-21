'''
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
'''

n = 0

for i in range(1, 1000):
    a = i ** i
    n = n + a

n = str(n)
print(n[-10:]) # Answer is 9110846700
