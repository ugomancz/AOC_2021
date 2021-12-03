if __name__ == '__main__':
    depth = 0
    distance = 0
    with open("input1.txt") as directions:
        for command in directions.readlines():
            com, value = tuple(command.split(" "))
            if com == "up":
                depth -= int(value)
            if com == "down":
                depth += int(value)
            if com == "forward":
                distance += int(value)
    print(depth*distance)
