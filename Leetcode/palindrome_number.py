class Solution:

    def is_palindrome(self, x: int) -> bool:

        if x < 0:
            return False

        reverse = 0
        
        copy = x

        while copy > 0:

            temp = copy % 10

            copy = copy // 10

            reverse = reverse * 10 + temp

        return reverse == x