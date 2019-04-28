'''
A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.
'''
import operator

attempts = ['319','680','180','690','129','620','762','689','762','318','368','710','720','710','629','168','160','689','716','731','736','729','316','729','729','710'	,'769','290','719','680','318','389','162','289','162','718','729','319','790','680','890','362','319','760','316','729','380','319','728','716']

# Checking if all numbers are present in attempts
present_numbers = [int(numbers) for numbers in sorted(set(list(''.join(attempts))))]
range_10 = [num for num in range(10)]
non_present_numbers = (list(set(range_10) - set(present_numbers))) # 4, 5 aren't present in attempts

# Convert attempts from strings to integers
attempts = list(map(int, attempts)) 

# Splitting every integer in the list into separate digits
attempts_split = []
for attempt in attempts:
	attempts_split.append([int(d) for d in str(attempt)])

# Create dictionary for numbers that appear before a given digit
before = {i:[] for i in range(10)}
for i in attempts_split:
	for j in range(10):
		for k in range(3):
			if i[k] == j:
				if k == 1:
					before[j].append(i[k-1])
				elif k == 2:
					before[j].append(i[k-1])
					before[j].append(i[k-2])

answer = {}
for i in range(10):
	answer[i] = len((set(before[i])))

# Removing numbers which weren't present in the attempts from the dictionary
for i in non_present_numbers:
	del answer[i]

# Sorting dictionary by number of digits appearing before a given digit, e.g. if 0 numbers appear before a certain digit, it's the first character in the passcode
sorted_answer = sorted(answer.items(), key=operator.itemgetter(1))

# Putting together the digits in a list
shortest_passcode = []
for i in sorted_answer:
	shortest_passcode.append(str(i[0]))
shortest_passcode = ''.join(shortest_passcode)

# Printing password
print(shortest_passcode)
