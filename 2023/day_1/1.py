def solution(input: str):
    with open(input, "r+") as fd:
        content = fd.readlines()

    content = [c.strip() for c in content]

    total = 0
    for l in content:
        calibration = ""
        for i in l:
            if i.isdigit():
                calibration += i
                break

        for i in l[::-1]:
            if i.isdigit():
                calibration += i
                break

        total += int(calibration)

    print(total)


if __name__ == "__main__":
    solution("inputs/1.txt")
