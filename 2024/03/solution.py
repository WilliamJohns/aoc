import sys
from re import compile

REGEXP = compile(r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)")


def part_1(command: str) -> int:
    matches: list[str] = REGEXP.findall(command)
    total = 0
    for match in matches:
        if not match.startswith("mul"):
            continue
        a, b = map(int, match[4:-1].split(","))
        total += a * b
    return total


def part_2(command: str) -> int:
    matches: list[str] = REGEXP.findall(command)
    total = 0
    enabled = True
    for match in matches:
        if match == "do()":
            enabled = True
        elif match == "don't()":
            enabled = False
        elif enabled:
            a, b = map(int, match[4:-1].split(","))
            total += a * b
    return total


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("Example Usage: python solution.py {input_file}")

    with open(sys.argv[1]) as f:
        command = f.read().strip()

    print(f"Part 1: {part_1(command)}")
    print(f"Part 2: {part_2(command)}")
