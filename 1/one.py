if __name__ == '__main__':
    counter = 0
    with open("input1.txt") as numbers:
        old_num = 0
        for line in numbers.readlines():
            if old_num > 0:
                if int(line) > old_num:
                    counter += 1
                    print("growing")
                else:
                    print("shrinking")
            old_num = int(line)
    print(counter)
