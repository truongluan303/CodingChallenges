class Solution:

    def climb_stairs(self, n: int) -> int:

        if n < 2:
            return n

        a = 1
        b = 2

        for i in range(2, n):
            c = a + b
            a = b
            b = c

        return b