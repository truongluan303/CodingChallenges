
def canMakeTriangle(arr):

    result = list()
    
    for i in range(len(arr) - 2):

        a = arr[i]
        b = arr[i + 1]
        c = arr[i + 2]

        if a <= 0 or b <= 0 or c <= 0:
            result.append(0)
            continue

        if (a + b + c) > 2 * max(a, b, c):
            result.append(1)

        else:
            result.append(0)

    return result






def main():
    x = canMakeTriangle([1, 2, 2, 4])
    print(x)


if __name__ == "__main__":
    main()