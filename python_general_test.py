from typing import List


"""
Given an example for an anonymous function in python
"""
lambda_sum = lambda a, b: a + b


"""
What is the difference between a list and a tuple?
How do you decide what you should use? Give a coding example for that
"""
# A tuple is immutable while a list is not
# We use a list when we need to perform operations and change the data, and
# we use a tuple when the data is only read but not changed.

def find_coordinate(matrix, target_value):
    # in this case, we return a tuple since we don't need to perform any
    # operations and the result should be read-only
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == target_value:
                return (i, j)
    return None


"""
How would you get the frequency of an element in a list?
"""


"""
Write a function to check if a list contains 2 numbers that will add
up to a given target
"""
def has_two_sum(arr: List[int], target: int) -> bool:
    found = set()
    for element in arr:
        if element in found:
            return True
        found.add(target - element)
    return False


"""
Write a function to check if a string is a palindrome
"""
def is_palidrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
    return True



"""
Write a function to check if 2 strings are anagrams
"""
def is_anagram(s: str, t: str) -> bool:
    multiset = dict.fromkeys(s, 0)

    for ch in s:
        multiset[ch] += 1
    
    for ch in t:
        if ch not in multiset:
            return False
        multiset[ch] -= 1
        
    return all(count == 0 for count in multiset.values())
    


"""
Given a list with elements running from 1 to n.
For example, in case n = 4, the given list will be: [1, 2, 3, 4]

A list will have 1 random missing element. Find the missing element in the list
Example 1: [1, 3, 4] --> in this case, n = 4 and 2 is missing --> returns 2
Example 2: [1, 2, 3, 4, 6, 7] --> in this case, n = 7 and 5 is missing --> returns 5

An ideal solution should have O(n) time complexity and O(1) space complexity.
It is guaranteed that there is only 1 missing number in the given list.
"""
def find_one_missing(arr: List[int]) -> int:
    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] > 1:
            return arr[i] + 1
    return arr[-1] + 1


"""
What will be the value of x?

a. "get"
b. "sum"
c. "um f"
d. "sum "

"""
def get_sum(a: str, b: str) -> int:
    """This get sum function. This function takes 2 parameters and returns an integer"""
    return int(a) + int(b)

x = get_sum.__doc__[9:12]
# x should be "sum"


"""
Implement an iterator that can be iterated upon from 1 to n
"""
class MyIterator:
    def __init__(self, n: int) -> None:
        self.n = n

    def __iter__(self):
        self.cur = 0
        return self

    def __next__(self):
        if self.cur >= self.n:
            raise StopIteration
        self.cur += 1
        return self.cur


"""
What is the value of x?
"""
x = [1, 2, 3] * 3
# x will be [1, 2, 3, 1, 2, 3, 1, 2, 3]


"""
Initialize a RxC array with 0s in a "Pythonic" way (should be 1 line only)
"""
R = 5
C = 3
arr = [[0] * C] * R


"""
Write a "Pythonic" function to count the number of elements less than 10 in a given
list (should be 1 line only)
"""
def count_less_than_ten(arr: List[int]) -> int:
    return sum(value < 10 for value in arr)

c = count_less_than_ten([1, 3, 11, 15, 3, 5, 13])


"""
What is the value of x?
"""
x = {
    1: 1,
    2: 2,
    **{3: 3, 4: 4}
}
# x will be { 1:1, 2:2, 3:3, 4:4 }
