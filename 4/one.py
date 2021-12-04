import copy

from termcolor import colored


class Bingo:
    def __init__(self, numbers):
        self.numbers = numbers
        self.marked = [[False for _ in range(5)] for _ in range(5)]

    def mark(self, value):
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers)):
                if self.numbers[i][j] == value:
                    self.marked[i][j] = True

    def win(self):
        for line in self.marked:
            if False not in line:
                return True
        for i in range(len(self.marked)):
            row_result = True
            for line in self.marked:
                row_result = row_result and line[i]
            if row_result:
                return True
        return False

    def score(self):
        result = 0
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers[i])):
                if not self.marked[i][j]:
                    result += self.numbers[i][j]
        return result

    def print(self):
        print("#" * 18)
        for i in range(len(self.numbers)):
            print("# ", end="")
            for j in range(len(self.numbers[i])):
                if self.marked[i][j]:
                    print(colored(f"{self.numbers[i][j]:02} ", color='green'), end='')
                else:
                    print(f"{self.numbers[i][j]:02} ", end='')
            print("#")
        print("#" * 18)


def main():
    with open("input.txt", "r") as data:
        draws = [int(x) for x in data.readline().split(',')]
        current_bingo = []
        bingos = []
        for line in [x.strip() for x in data.readlines()]:
            if line == '' and current_bingo:  # empty line
                bingos.append(Bingo(copy.deepcopy(current_bingo)))
                current_bingo.clear()
                continue
            elif line == '':
                continue
            current_bingo.append([int(x) for x in line.split()])
        if bingos:
            bingos.append(Bingo(copy.deepcopy(current_bingo)))

        for draw in draws:
            for bingo in bingos:
                bingo.mark(draw)
                if bingo.win():
                    print("We have a winner!")
                    bingo.print()
                    print(f"Last called number was {draw:02}")
                    print(f"The score is {bingo.score()}")
                    print(colored(f"The final score is {bingo.score() * draw}", color="green"))
                    return


if __name__ == '__main__':
    main()
