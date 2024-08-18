def solution(input: str):
    with open(input, "r+") as fd:
        content = fd.read().strip().split("\n")

    INVALID = "."
    position = 0
    coordinates = {}
    total = 0

    for line in content:
        i = 0
        while i < len(line):
            # create coordinates dict, for future references
            if not line[i].isdigit() and line[i] != INVALID:
                if position in coordinates:
                    (coordinates[position]).append(i)
                else:
                    coordinates[position] = [i]
            i += 1
        position += 1

    position = 0
    number = ""
    for line in content:
        i = 0
        while i < len(line):
            begin = -1
            end = -1
            while line[i].isdigit():
                if begin < 0:
                    begin = i
                number += line[i]
                i += 1
                if i >= len(line):
                    break

                continue

            if end < 0:
                end = i - 1

            i += 1

            if number != "":
                found = check_adjacents(position, begin, end, coordinates)
                if found:
                    total += int(number)

            number = ""
        position += 1

    print(f"total: {total}")


def check_adjacents(position, begin, end: int, coordinates: dict) -> bool:
    found = False
    # check in same line
    if position in coordinates:
        symbol_coordinates = coordinates[position]
        if begin - 1 in symbol_coordinates:
            found = True
        if end + 1 in symbol_coordinates:
            found = True

    # check one line above
    if position - 1 in coordinates:
        symbol_coordinates = coordinates[position - 1]
        for i in range(begin - 1, end + 2):
            if i in symbol_coordinates:
                found = True

    # check one line below
    if position + 1 in coordinates:
        symbol_coordinates = coordinates[position + 1]
        for i in range(begin - 1, end + 2):
            if i in symbol_coordinates:
                found = True

    return found


if __name__ == "__main__":
    # solution("inputs/3.short.txt")
    # solution("inputs/3.test.txt")
    solution("inputs/3.txt")
