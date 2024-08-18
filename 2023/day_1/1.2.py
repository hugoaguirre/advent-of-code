def solution(input: str):
    numerals = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    with open(input, "r+") as fd:
        content = fd.readlines()

    content = [c.strip() for c in content]

    total = 0
    for line in content:
        calibration = ""
        # from left to right
        for i in range(len(line)):
            # check if string contains any numeral
            for k in numerals.keys():
                if line[i:].startswith(k):
                    calibration += numerals[k]
                    break
            if calibration != "":
                break

            if line[i].isdigit():
                calibration += line[i]
                break

        for i in range(len(line) - 1, -1, -1):
            for k in numerals.keys():
                if line[i:].startswith(k):
                    calibration += numerals[k]
                    break

            if len(calibration) == 2:
                break

            if line[i].isdigit():
                calibration += line[i]
                break

        total += int(calibration)
    print(total)


if __name__ == "__main__":
    solution("inputs/1.txt")
    # solution("inputs/1.test.txt")
