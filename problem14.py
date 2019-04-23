'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

def collatz_sequence(n):
	sequence = []
	sequence.append(n)
	while n != 1:
		if n%2 == 0:
			n = n/2
			sequence.append(int(n))
		else:
			n = n*3 + 1
			sequence.append(int(n))
	else:
		pass
	return sequence

def find_longest_sequence(n):
	seq = 0
	longest_sequence = []
	for i in range(1,n):
		seq = collatz_sequence(i)
		if len(seq) > len(longest_sequence):
			longest_sequence = seq
		else:
			pass
	return longest_sequence

print(find_longest_sequence(1_000_000)[0])
