from termcolor import colored


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "[{}, {}]".format(self.x, self.y)

    def max_coordinate(self):
        return max(self.x, self.y)


class Line:
    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2

    def __str__(self):
        return "{} -> {}".format(self.c1, self.c2)

    def straight(self):
        return self.vertical() or self.horizontal()

    def max_x_coordinate(self):
        return max(self.c1.x, self.c2.x)

    def max_y_coordinate(self):
        return max(self.c1.y, self.c2.y)

    def horizontal(self):
        return self.c1.x != self.c2.x and self.c1.y == self.c2.y

    def vertical(self):
        return self.c1.x == self.c2.x and self.c1.y != self.c2.y

    def vertical_coordinate(self):
        if self.horizontal():
            return self.c1.y
        raise Exception(f"Line {str(self)} not horizontal")

    def horizontal_range(self):
        if self.horizontal():
            return min(self.c1.x, self.c2.x), max(self.c1.x, self.c2.x) + 1
        raise Exception(f"Line {str(self)} not horizontal")

    def horizontal_coordinate(self):
        if self.vertical():
            return self.c1.x
        raise Exception(f"Line {str(self)} not vertical")

    def vertical_range(self):
        if self.vertical():
            return min(self.c1.y, self.c2.y), max(self.c1.y, self.c2.y) + 1
        raise Exception(f"Line {str(self)} not vertical")


class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.matrix = [[0 for _ in range(height)] for _ in range(width)]

    def draw_line(self, line: Line):
        if line.straight():
            if line.horizontal():
                x = line.vertical_coordinate()
                for i in range(*line.horizontal_range()):
                    self.matrix[i][x] += 1
            if line.vertical():
                y = line.horizontal_coordinate()
                for i in range(*line.vertical_range()):
                    self.matrix[y][i] += 1

    def print(self):
        print('#' * (self.width * 3 + 3))
        for i in range(self.height):
            print("# ", end="")
            for j in range(self.width):
                if self.matrix[j][i] > 1:
                    print(colored(f"{self.matrix[j][i]:02} ", color="red"), end='')
                elif self.matrix[j][i] > 0:
                    print(colored(f"{self.matrix[j][i]:02} ", color="green"), end='')
                else:
                    print(f"{self.matrix[j][i]:02} ", end='')
            print("#")
        print('#' * (self.width * 3 + 3))

    def overlaps(self):
        counter = 0
        for i in range(self.width):
            for j in range(self.height):
                if self.matrix[i][j] > 1:
                    counter += 1
        return counter


def read_input(file):
    with open(file, 'r') as f:
        return [Line(*[Coordinate(*map(int, y.split(','))) for y in x.strip().split(" -> ")]) for x in f.readlines()]


def main():
    lines = read_input("test.txt")
    field_width, field_height = max([x.max_x_coordinate() for x in lines]) + 1, max(
        [x.max_y_coordinate() for x in lines]) + 1
    field = Field(field_width, field_height)

    for line in lines:
        field.draw_line(line)

    # field.print()
    print(f"Final score is {field.overlaps()}.")


if __name__ == '__main__':
    main()
