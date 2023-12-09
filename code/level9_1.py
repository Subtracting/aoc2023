from collections import defaultdict


filename = "inputs\level9_input.txt"


def diff(sequence):
    return [sequence[i] - sequence[i - 1] for i in range(1, len(sequence))]


with open(filename) as file:
    lines = [line.rstrip() for line in file]
    total = 0
    for line in lines:
        sequence = list(map(int, line.split(" ")))
        last = sequence[-1]
        diffs = "12"
        while len(set(diffs)) != 1:
            diffs = diff(sequence)
            sequence = diffs
            last += sequence[-1]
        total += last

print(total)
