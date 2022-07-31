def generate_matrix(arr: list, vertices: list) -> None:

    mymap = dict()

    print("\n------------------------------------------------")

    print("\n\nMATRIX:\n", end="\t")
    for v in vertices:
        mymap[v] = set()
        out = v if len(v) > 1 else (" " + v)
        print(out, end="  ")
    print("\n")

    for pair in arr:
        first = pair[0]
        second = pair[1]

        mymap[first].add(second)
        mymap[second].add(first)

    for v1 in vertices:
        print(v1, end="\t")

        for v2 in vertices:
            out = 1 if v2 in mymap[v1] else 0
            print("", out, end="  ")

        print()
    print()

    print("\nADJACENT LIST:\n")
    for k, v in mymap.items():
        print(k, ":", sorted(v))
    print()


def main():

    arr = list()

    print("Enter the pairs:")
    while True:
        line = input().strip()

        if line == "":
            break

        line.replace(",", " ").replace("(", "").replace(")", "")
        pair = line.split()

        arr.append(pair)

    print("Enter the vertices:", end=" ")
    v = input().replace(",", "").split()

    generate_matrix(arr, v)


if __name__ == "__main__":
    main()
