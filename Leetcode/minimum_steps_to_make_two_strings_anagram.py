class Solution:

	def min_steps(self, s: str, t: str) -> int:

		bag = dict()
		difference = 0

		for c in s:

			if c not in bag:
				bag[c] = 0

			bag[c] += 1


		for c in t:

			if c not in bag:
				difference += 1

			else:
				bag[c] -= 1

				if bag[c] < 0:
					difference += 1

		return difference
