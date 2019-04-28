'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

one_through_nine = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

ten_through_nineteen = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

hundreds = ['one hundred','two hundred','three hundred','four hundred','five hundred','six hundred','seven hundred','eight hundred','nine hundred']

one_thousand = ['one thousand']

twenty_one_through_ninety_nine = []
for number in tens:
	for digit in one_through_nine:
		twenty_one_through_ninety_nine.append(number + ' ' + digit)
one_through_ninety_nine = one_through_nine + ten_through_nineteen + tens + twenty_one_through_ninety_nine

one_hundred_and_one_through_nine_hundred_ninety_nine = []
for number in hundreds:
	for digit in one_through_ninety_nine:
		one_hundred_and_one_through_nine_hundred_ninety_nine.append(number + ' and ' + digit)
one_hundred_through_nine_hundred_ninety_nine = hundreds + one_hundred_and_one_through_nine_hundred_ninety_nine

all_numbers = one_through_ninety_nine + one_hundred_through_nine_hundred_ninety_nine + one_thousand

all_numbers = ''.join(all_numbers)
all_numbers = all_numbers.replace(" ", "")

print(len(all_numbers))
