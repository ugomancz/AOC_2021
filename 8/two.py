def read_lines(filename):
    with open(filename, 'r') as f:
        return [x.strip() for x in f.readlines()]


def main():
    output_lines = [x.split('|')[1].strip().split() for x in read_lines("input.txt")]
    # print(output_lines)
    digits = {2: 0, 3: 0, 4: 0, 7: 0}
    for line in output_lines:
        for digit in line:
            if len(digit) in digits:
                digits[len(digit)] += 1
    # print(digits)
    print(f"There's {sum(digits.values())} occurrences of signals for digits 1, 4, 7 and 8")


if __name__ == '__main__':
    main()
