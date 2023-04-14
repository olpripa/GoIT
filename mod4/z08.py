power = 1
helth_energy = [[1, 1, 5, 10], [10, 2], [1, 1, 1]]
helth_energy1 = [[1, 1, 5, 10], [10, 2], [1, 1, 1], [2, 1, 2]]


def game(helth_energy, power):
    for sp in helth_energy:
        for p in sp:
            if power >= p:
                power += p
            else:
                break
    return power

print(game(helth_energy, power))

print(game([[1, 2, 5, 10], [2, 10, 2], [1, 3, 1]], 1))
