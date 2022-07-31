def count_triplets(t: int, arr: list) -> int:
    """
    count all the triplets of (a, b, c) such that:
    a < b < c and (a + b + c) <= t
    """
    count = 0

    arr.sort()

    for i in range(len(arr) - 2):

        l = i + 1
        r = len(arr) - 1

        while l < r:

            if arr[i] + arr[l] + arr[r] <= t:
                count += r - l
                l += 1

            else:
                r -= 1

    return count


def main():
    arr = [6, 1, 4, 2, 3]
    count = count_triplets(8, arr)
    print(count)


if __name__ == "__main__":
    main()
