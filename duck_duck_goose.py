def duck_duck_goose(players, goose):
    i = 0
    count = 0
    while count <= goose:
        if count == (goose - 1):
            return players[i].name
        else:
            count += 1
            i = (i + 1) % len(players)
