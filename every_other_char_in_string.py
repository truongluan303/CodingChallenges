"""
Implement a Python function that takes a string and returns a string containing
every other character from original string (e.g., “house” -> “hue”).
"""


def remove_every_other_char(s: str) -> str:

    result = ""

    for i in range(0, len(s), 2):
        result += s[i]

    return result


def main() -> None:
    print(remove_every_other_char("house"))
    print(remove_every_other_char("abcdef"))
    print(remove_every_other_char("1.2.3.4.5.6.7.8.9"))


if __name__ == "__main__":
    main()
