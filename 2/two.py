if __name__ == '__main__':
    depth = 0
    distance = 0
    aim = 0
    with open("input1.txt") as directions:
        for command in directions.readlines():
            com, value = tuple(command.split(" "))
            if com == "up":
                aim -= int(value)
            if com == "down":
                aim += int(value)
            if com == "forward":
                distance += int(value)
                depth += aim*int(value)
    print(depth*distance)
