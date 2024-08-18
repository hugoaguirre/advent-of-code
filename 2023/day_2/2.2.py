def solution(input: str):
    with open(input, "r+") as fd:
        content = fd.read().strip().split("\n")

    prefix = "Game "

    total = 0
    for game in content:
        game_id, rounds = game.split(":")
        game_id = int(game_id[len(prefix) :])

        rounds = rounds.split(";")
        games = [r.split(",") for r in rounds]
        games = [[draw.strip().split(" ") for draw in g] for g in games]

        power = 1
        maxes = {"red": 0, "green": 0, "blue": 0}
        for draw in games:
            for color in draw:
                count = int(color[0])
                name = color[1]
                if count > maxes[name]:
                    maxes[name] = count

        for v in maxes.values():
            power *= v
        total += power
    print(total)


if __name__ == "__main__":
    solution("inputs/2.txt")
    # solution("inputs/2.test.txt")
