"""
Suppose, we want to implement a function that allows us to reverse the ordering
of songs based on their lengths, but we will be reversing each part of the playlist
in chunks.

Given a list of song lengths (as integers), mutate the list (that is, do not create
another list, use the given list) such that chunks of increasing size in the list get
reversed. The chunk size is initially 1, and increases by 1 for every chunk as we
continue through the list (view example below). The chunks do not overlap.
Chunks are only processed if they are the correct size (see example below).

Example:

Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
Output: [1, 3, 2, 6, 5, 4, 10, 9, 8, 7, 11, 12, 13]

We will only process elements that are in chunks with the correct size. So 11, 12,
13 will stay in their original positions as the chunk should be size 5 but there are
only 3 elements. You can think of leftover elements as elements that we won't
reverse since they aren't actually in a valid chunk.

If we had 1 to 15, we would get [1, 3, 2, 6, 5, 4, 10, 9, 8, 7, 15, 14, 13, 12, 11]
since we have a valid chunk with 5 elements

You should do this WITHOUT creating a new list. When reversing items you should
do it within the list itself (use an in-place approach).

Do not use Ist[::-1] or any methods that can reverse a list.

Think of a way to manipulate the given list without creating another list. You
should not have a return statement, because your function will mutate the given
list.

Example:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] can be broken up into chunks:
[(1), (2, 3), (4, 5, 6), (7, 8, 9, 10)] (these are not tuples, just groups for clarity)

"""



arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def solve(arr):
    i = j = 1
    
    while i < len(arr):
        j += 1

        last = i + j - 1
        first = i
        
        if last <= len(arr) - 1:
            while first < last:
                arr[first], arr[last] = arr[last], arr[first]
                first += 1
                last -= 1
        i += j
     
     
solve(arr)
print(arr)
