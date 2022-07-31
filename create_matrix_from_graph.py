def get_adjacency_list(arr: list, n: int) -> dict():

    vertex = dict()

    for i in range(n):
        vertex[i] = set()

    for pair in arr:
        first = int(pair[0])
        second = int(pair[1])

        vertex[first].add(second)
        vertex[second].add(first)

    print("ADJACENT LIST:")
    for k, v in vertex.items():
        print(k, ":", v)
    print()

    return vertex


def generate_matrix(vertex: dict, n: int):

    print("\nMATRIX:")
    print("\t", end="")
    for i in range(n):
        num = str(i) if len(str(i)) > 1 else (" " + str(i))
        print(num, end="  ")
    print("\n")

    for i in range(n):
        print(i, end="\t")
        for j in range(n):
            val = 1 if j in vertex[i] else 0
            print("", val, end="  ")
        print()
    print()


def main():

    arr = list()

    print("\nEnter The Pairs:")

    while True:
        line = input().strip()

        if line == "":
            break

        arr.append(line.split())

    print("Enter number of vertices:")
    n = int(input().strip())

    print("\n--------------------------------------------------------\n")

    vertex = get_adjacency_list(arr, n)

    generate_matrix(vertex, n)


if __name__ == "__main__":
    main()
