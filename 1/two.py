if __name__ == '__main__':
    counter = 0
    with open("input2.txt") as numbers:
        lines = list(map(int, list(numbers.readlines())))
        new = 0
        window = lines[:3]
        old = sum(window)
        for i in range(len(lines)-3):
            window.pop(0)
            window.append(lines[i+3])
            new = sum(window)
            if new > old:
                counter += 1
            old = new
    print(counter)
