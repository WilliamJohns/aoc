import sys


def is_safe(sequence: list[int]) -> bool:
    delta = 0
    for i in range(len(sequence) - 1):
        delta_i = sequence[i] - sequence[i + 1]
        if abs(delta_i) > 3 or delta_i == 0:
            return False
        if (delta < 0 and delta_i > 0) or (delta > 0 and delta_i < 0):
            return False
        delta = delta_i
    return True


def part_1(input_lines: list[str]) -> int:
    safe_count = 0
    for line in input_lines:
        if is_safe(list(map(int, line.split()))):
            safe_count += 1
    return safe_count


def part_2(input_lines: list[str]) -> str:
    safe_count = 0
    for line in input_lines:
        sequence = list(map(int, line.split()))
        for i in range(len(sequence)):
            if is_safe(sequence[:i] + sequence[i + 1 :]):
                safe_count += 1
                break
    return safe_count


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("Example Usage: python solution.py {input_file}")

    with open(sys.argv[1]) as f:
        input_lines = [l.strip() for l in f.readlines()]

    print(f"Part 1: {part_1(input_lines)}")
    print(f"Part 2: {part_2(input_lines)}")
