class Fish:
    def __init__(self, energy):
        self.energy = energy

    def __str__(self):
        return f"{self.energy}"

    def day_passed(self):
        self.energy -= 1


def read_data(file):
    with open(file, 'r') as f:
        return [int(x) for x in f.readline().split(',')]


def main():
    init_fish_energy = read_data("input.txt")
    sea = list(map(Fish, init_fish_energy))
    for _ in range(80):
        born_fish = []
        for fish in sea:
            fish.day_passed()
            if fish.energy < 0:
                born_fish.append(Fish(8))
                fish.energy = 6
        sea.extend(born_fish)
    print(f"There's now {len(sea)} lanternfish in the sea.")



if __name__ == '__main__':
    main()
