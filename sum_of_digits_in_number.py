def get_digits_sum(n):
    result = 0

    while n != 0:
        result += n % 10
        n = n // 10

    return result


def main():
    print(get_digits_sum(1239))


if __name__ == "__main__":
    main()
