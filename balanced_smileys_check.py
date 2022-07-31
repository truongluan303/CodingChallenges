LEFT = {"(", "[", "{"}
RIGHT = {")", "]", "}"}

PAREN_MAP = {"(": ")", "{": "}", "[": "]"}


def is_balanced_smiley(s: str) -> bool:

    icons_removed = s.replace(":)", "").replace(":(", "")

    return is_balanced_paren(s) or is_balanced_paren(icons_removed)


def is_balanced_paren(s: str) -> bool:

    stack = list()

    for c in s:

        if c in LEFT:
            stack.append(c)

        elif c in RIGHT:

            if len(stack) == 0:
                return False

            left = stack.pop()

            if PAREN_MAP[left] != c:
                return False

    return len(stack) == 0


def main() -> None:

    s = ["(())", "()()", ":)", ":((", "(:)", "(i am sad :()", "([]:)", ":)())"]
    out = [True, True, True, False, True, True, True, False]

    for i in range(len(s)):
        if is_balanced_smiley(s[i]) != out[i]:
            print("\nFAILED")
            return

    print("\nPASSED")


if __name__ == "__main__":
    main()
