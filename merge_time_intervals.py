def merge_intervals(intervals: list) -> list:

    intervals.sort()

    stack = list()
    stack.append(intervals[0])

    for i in range(1, len(intervals)):

        last = stack[-1]

        if last[1] >= intervals[i][0]:

            last[1] = max(last[1], intervals[i][1])

            stack.pop()
            stack.append(last)

        else:
            stack.append(intervals[i])

    return stack


def main():
    intervals = [[7, 7], [2, 3], [6, 11], [1, 2]]
    print(merge_intervals(intervals))


if __name__ == "__main__":
    main()
