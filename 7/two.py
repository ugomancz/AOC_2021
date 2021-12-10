import math


def distance(a: int, b: int) -> int:
    return math.ceil((abs(a - b) ** 2 + abs(a - b)) / 2)


def main():
    with open("input.txt", 'r') as f:
        data = sorted([int(x) for x in f.readline().split(',')])
        least_fuel_spent = data[-1] * len(data) * 1000
        for i in range(data[0], data[-1] + 1):
            fuel_needed = sum(list(map(lambda x: distance(x, i), data)))
            if fuel_needed < least_fuel_spent:
                least_fuel_spent = fuel_needed
        print(f"Fuel needed: {least_fuel_spent}")


if __name__ == '__main__':
    main()
