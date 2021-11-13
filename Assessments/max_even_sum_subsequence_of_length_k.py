'''
Example:

arr = [4, 2, 6, 7, 8], k = 3
=> output = 18
3 numbers that sum up to the highest even value are
4 + 6 + 8 = 18

arr = [7, 7, 7], k = 1
=> output = -1
we can only pick 1 number and none of them are even.
Therefore, return -1
'''


def solution(arr, k):
    
    if len(arr) < k:
        return -1

    evens = [x for x in arr if x % 2 == 0]
    odds = [x for x in arr if x % 2 != 0]
    evens.sort(reverse=True)
    odds.sort(reverse=True)

    result = 0
    i = 0
    j = 0
    
    while k > 0:

        if k % 2 == 0:

            if i < len(evens) - 1 and j < len(odds) - 1:
                if evens[i] + evens[i + 1] <= odds[j] + odds[j + 1]:
                    result += odds[j] + odds[j + 1]
                    j += 2
                else:
                    result += evens[i] + evens[i + 1]
                    i += 2

            elif i < len(evens) - 1:
                result += evens[i] + evens[i + 1]
                i += 2

            elif i < len(odds) - 1:
                result += odds[j] + odds[j + 1]
                j += 2

            k -= 2

        else:
            if i < len(evens):
                result += evens[i]
                i += 1
                k -= 1
            else:
                return -1
        
    return result





if __name__ == "__main__":
    print(solution([4, 2, 6, 7, 8], 3))
    print(solution([7, 7, 7], 1))
    print(solution([2, 3, 4, 5, 6], 5))