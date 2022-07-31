def meandering_sort(arr: list) -> list:
    """
    a meandering sorted array has the form:
    [first largest, first smallest, second largest, second smallest, ...]
    """
    arr.sort()
    result = list()

    l = 0
    r = len(arr) - 1

    while l < r:
        result.append(arr[r])
        result.append(arr[l])
        l += 1
        r -= 1

    if l == r:
        result.append(arr[l])

    return result


def main():
    arr = [5, 2, 7, 8, -2, 25, 25]
    arr = meandering_sort(arr)
    print(arr)


if __name__ == "__main__":
    main()
