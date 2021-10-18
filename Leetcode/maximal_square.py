class Solution:

	def maximal_square(self, matrix) -> int:

		if len(matrix) == 0:
			return 0

		highest = 0

		for i in range(len(matrix)):

			for j in range(len(matrix[i])):

				matrix[i][j] = int(matrix[i][j])

				if matrix[i][j] == 1:
					highest = 1


		for i in range(1, len(matrix)):

			for j in range(1, len(matrix[i])):
				
				if matrix[i][j] != 0:

					matrix[i][j] = 1 + min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])
	
					highest = max(highest, matrix[i][j])


		area = highest * highest

		return area








def main():

	matrix = [["1","0","1","0","0"],
			  ["1","0","1","1","1"],
              ["1","1","1","1","1"],
			  ["1","0","0","1","0"]]
	
	solution = Solution()

	print(solution.maximal_square(matrix))



if __name__ == "__main__":
	main()
