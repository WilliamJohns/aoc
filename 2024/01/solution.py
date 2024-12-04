import sys
from collections import defaultdict


def part_1(input_lines: list[str]) -> int:
    left: list[int] = []
    right: list[int] = []
    for line in input_lines:
        l, r = map(int, line.split())
        left.append(l)
        right.append(r)
    left.sort()
    right.sort()
    total = 0
    for i in range(len(input_lines)):
        total += abs(left[i] - right[i])
    return total


def part_2(input_lines: list[str]) -> int:
    left: list[int] = []
    right: dict[int, int] = defaultdict(int)
    for line in input_lines:
        l, r = map(int, line.split())
        left.append(l)
        right[r] += 1

    total = 0
    for i in range(len(input_lines)):
        total += left[i] * right[left[i]]
    return total


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("Example Usage: python solution.py {input_file}")

    with open(sys.argv[1]) as f:
        input_lines = [l.strip() for l in f.readlines()]

    print(f"Part 1: {part_1(input_lines)}")
    print(f"Part 2: {part_2(input_lines)}")
