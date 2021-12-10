import statistics


def main():
    with open("input.txt", 'r') as f:
        data = [int(x) for x in f.readline().split(',')]
        median = int(statistics.median(data))
        print(f"Median is {median}")
        fuel_spent = sum(list(map(lambda x: abs(x - median), data)))
        print(f"Fuel needed: {fuel_spent}")


if __name__ == '__main__':
    main()
