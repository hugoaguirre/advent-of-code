def solution(input: str):
    with open(input, "r+") as fd:
        content = fd.read().strip().split("\n")

    GEAR = "*"
    total = 0

    l = 0
    while l < len(content):
        i = 0
        line = content[l]
        while i < len(line):
            ratio = 1
            count = 0
            found_up = False
            found_down = False
            if not line[i].isdigit() and line[i] is GEAR:
                # check same line
                if i - 1 >= 0:
                    if line[i - 1].isdigit():
                        ratio *= find_digit(line, i - 1)
                        count += 1
                if i + 1 < len(line):
                    if line[i + 1].isdigit():
                        ratio *= find_digit(line, i + 1)
                        count += 1

                # check up and down
                if l - 1 >= 0:
                    if content[l - 1][i].isdigit():
                        ratio *= find_digit(content[l - 1], i)
                        found_up = True
                        count += 1
                if l + 1 < len(content):
                    if content[l + 1][i].isdigit():
                        ratio *= find_digit(content[l + 1], i)
                        found_down = True
                        count += 1

                # check diagonals
                # up left
                if l - 1 >= 0 and i - 1 >= 0:
                    if content[l - 1][i - 1].isdigit() and not found_up:
                        ratio *= find_digit(content[l - 1], i - 1)
                        count += 1
                # down left
                if l + 1 < len(content) and i - 1 >= 0:
                    if content[l + 1][i - 1].isdigit() and not found_down:
                        ratio *= find_digit(content[l + 1], i - 1)
                        count += 1
                # up right
                if l - 1 >= 0 and i + 1 < len(line):
                    if content[l - 1][i + 1].isdigit() and not found_up:
                        ratio *= find_digit(content[l - 1], i + 1)
                        count += 1
                # down right
                if l + 1 < len(content) and i + 1 < len(line):
                    if content[l + 1][i + 1].isdigit() and not found_down:
                        ratio *= find_digit(content[l + 1], i + 1)
                        count += 1

                if count == 2:
                    total += ratio
            i += 1
        l += 1

    print(f"total: {total}")


def find_digit(line: str, index: int) -> int:
    digit = line[index]

    i = index
    # left
    while i >= 0:
        if i - 1 < 0:
            break
        if not line[i - 1].isdigit():
            break

        digit = line[i - 1] + digit
        i -= 1

    # right
    i = index
    while i < len(line):
        if i + 1 >= len(line):
            break
        if not line[i + 1].isdigit():
            break

        digit = digit + line[i + 1]
        i += 1

    return int(digit)


if __name__ == "__main__":
    # solution("inputs/3.short.txt")
    # solution("inputs/3.test.txt")
    solution("inputs/3.txt")
