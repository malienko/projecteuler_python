'''
The 5-digit number, 16807=7**5, is also a fifth power. Similarly, the 9-digit number, 134217728=8**9, is a ninth power.
How many n-digit positive integers exist which are also an nth power?
'''

numbers = []
def powerfuldigits():
    for i in range(1,100):
        for j in range(1,1000):
            number = j**i
            if len(str(number))==i:
            	numbers.append(number)
    return numbers

result = len(powerfuldigits())
print(result)
