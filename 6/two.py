def read_data(file):
    with open(file, 'r') as f:
        return [int(x) for x in f.readline().split(',')]


def main():
    init_fish = read_data("input.txt")
    sea = [0 for _ in range(9)]
    for fish in init_fish:
        sea[fish] += 1

    for i in range(256):
        newborn_fish = sea[0]
        sea[7] += sea[0]
        for j in range(len(sea) - 1):
            sea[j] = sea[j + 1]
        sea[-1] = newborn_fish
    print(f"There's now {sum(sea)} lanternfish in the sea.")


if __name__ == '__main__':
    main()
