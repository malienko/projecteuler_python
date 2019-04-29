'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle found at https://projecteuler.net/problem=18

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
'''
import math
import random 
import numpy as np

def intersperse(list, item):
    result = [item] * (len(list) * 2 - 1)
    result[0::2] = list
    return result

line1 =  [75]
line2 =  [95,64]
line3 =  [17,47,82]
line4 =  [18,35,87,10]
line5 =  [20,4,82,47,65]
line6 =  [19,1,23,75,3,34]
line7 =  [88,2,77,73,7,63,67]
line8 =  [99,65,4,28,6,16,70,92]
line9 =  [41,41,26,56,83,40,80,70,33]
line10 = [41,48,72,33,47,32,37,16,94,29]
line11 = [53,71,44,65,25,43,91,52,97,51,14]
line12 = [70,11,33,28,77,73,17,78,39,68,17,57]
line13 = [91,71,52,38,17,14,91,43,58,50,27,29,48]
line14 = [63,66,4,68,89,53,67,30,73,16,69,87,40,31]
line15 = [4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]

lines = [line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15]
new_lines = []

for line in lines:
	line = intersperse(line,0)
	new_lines.append(line)

for line in new_lines:
	lenth_taken = (len(line))
	buffer_zeros = (29 - lenth_taken)/2
	buffer_zeros = np.zeros(int(buffer_zeros))
	arr_line = np.array(line)
	full_line_array = np.concatenate((buffer_zeros,arr_line,buffer_zeros),axis = 0)

big_array = [
[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 75,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 95,  0, 64,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 17,  0, 47,  0, 82,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 18,  0, 35,  0, 87,  0, 10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 20,  0,  4,  0, 82,  0, 47,  0, 65,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[ 0,  0,  0,  0,  0,  0,  0,  0,  0, 19,  0,  1,  0, 23,  0, 75,  0,  3,  0, 34,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[ 0,  0,  0,  0,  0,  0,  0,  0, 88,  0,  2,  0, 77,  0, 73,  0,  7,  0, 63,  0, 67,  0,  0,  0,  0,  0,  0,  0,  0],
[ 0,  0,  0,  0,  0,  0,  0, 99,  0, 65,  0,  4,  0, 28,  0,  6,  0, 16,  0, 70,  0, 92,  0,  0,  0,  0,  0,  0,  0],
[ 0,  0,  0,  0,  0,  0, 41,  0, 41,  0, 26,  0, 56,  0, 83,  0, 40,  0, 80,  0, 70,  0, 33,  0,  0,  0,  0,  0,  0],
[ 0,  0,  0,  0,  0, 41,  0, 48,  0, 72,  0, 33,  0, 47,  0, 32,  0, 37,  0, 16,  0, 94,  0, 29,  0,  0,  0,  0,  0],
[ 0,  0,  0,  0, 53,  0, 71,  0, 44,  0, 65,  0, 25,  0, 43,  0, 91,  0, 52,  0, 97,  0, 51,  0, 14,  0,  0,  0,  0],
[ 0,  0,  0, 70,  0, 11,  0, 33,  0, 28,  0, 77,  0, 73,  0, 17,  0, 78,  0, 39,  0, 68,  0, 17,  0, 57,  0,  0,  0],
[ 0,  0, 91,  0, 71,  0, 52,  0, 38,  0, 17,  0, 14,  0, 91,  0, 43,  0, 58,  0, 50,  0, 27,  0, 29,  0, 48,  0,  0],
[ 0, 63,  0, 66,  0,  4,  0, 68,  0, 89,  0, 53,  0, 67,  0, 30,  0, 73,  0, 16,  0, 69,  0, 87,  0, 40,  0, 31,  0],
[ 4,  0, 62,  0, 98,  0, 27,  0, 23,  0,  9,  0, 70,  0, 98,  0, 73,  0, 93,  0, 38,  0, 53,  0, 60,  0,  4,  0, 23]]

big_array = np.array(big_array)

incr_coordinates = [-1,1]
total_lists = []
for z in range(50000):
	x = 14
	y = 0
	grand_total = 75
	for i in range(14):
		random.shuffle(incr_coordinates)
		x += incr_list[0]
		y += 1
		grand_total = grand_total + big_array[y,x]
	total_lists.append(grand_total)

print(max(total_lists))
