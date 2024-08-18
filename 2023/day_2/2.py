def solution(input: str):
    maxes = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

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

        possible = True
        for draw in games:
            for color in draw:
                count = int(color[0])
                name = color[1]
                if maxes[name] < count:
                    possible = False
                    break

            if not possible:
                break

        if possible:
            total += game_id

    print(total)


if __name__ == "__main__":
    solution("inputs/2.txt")
    # solution("inputs/2.test.txt")
