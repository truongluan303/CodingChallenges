'''
Given an integer, if the number is a prime, return 1.
Else, return its smallest divisor greater than 1
'''


def is_prime(n):

	if n == 0:
		return 1

	if n == 1:
		return 1

	for i in range(2, n):
		if n % i == 0:
			return i

	return 1
