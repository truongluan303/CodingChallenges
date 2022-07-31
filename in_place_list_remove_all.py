"""
Remove all elements that match a given target from a list (in place)
"""
from typing import Any


def remove_all(arr: list, target: Any):
    i = 0
    for j in range(len(arr)):
        if arr[j] != target:
            arr[i] = arr[j]
            i += 1
    count = len(arr) - i
    for _ in range(count):
        arr.pop()


arr = [1, 2, 3, 1, 4, 5, 1, 1, 1, 6, 1, 1, 7, 8, 9, 1, 1]
remove_all(arr, 1)
print(arr)
