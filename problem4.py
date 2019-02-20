'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def isPalindrome(k):
	k = str(k)
	if k == k[::-1]:
		return True
	else:
		return False

def findAnswer(n):
    largestPalindrome = 0
    a = 999
    while a > 99:
        b = 999
        while b >= a:
            c = a * b
            if c > largestPalindrome and isPalindrome(c):
                largestPalindrome = c
            b -= 1
        a -= 1
    return largestPalindrome

print(findAnswer(999*999))
