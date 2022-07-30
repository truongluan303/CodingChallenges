'''
Given three integers i, j, and k, a sequence sum to be the value of 
i + (i + 1) + (i + 2) + (i + 3) + ... + j + (j - 1) + (j - 2) + ... + k

Calculate the sequence sum as described
-------------------------------------------------------------------------
Example:
i = 5, j = 9, k = 6
answer: 5 + 6 + 7 + 8 + 9 + 8 + 7 + 6 = 56
'''


def get_sequence_sum(i: int, j: int, k: int) -> int:

	smaller = min(i, k)
	bigger = max(i, k)

	temp1 = get_sum(smaller, bigger)
	
	temp2 = get_sum(bigger, j) * 2
	temp2 = temp2 - j - bigger

	return (temp1 + temp2)	





def get_sum(begin: int, end: int) -> int:
	'''
	Get the sum of (begin + (begin + 1) + (begin + 2) + ... + end)
	'''
	# sum 1 -> n = (n * (n + 1) / 2)
	# ==> (sum k -> n) = (sum 1 -> n) - (sum 1 -> k-1)
	
	temp = begin

	if begin < 0:
		temp = 0
		begin *= -1

	begin *= (end * (end + 1) // 2)
	end = end * (end + 1) // 2

	return (end - begin + temp)
