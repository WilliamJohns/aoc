import sys
from collections import defaultdict

Rules = dict[int, set[int]]
Update = list[int]


def is_ordered(rules: Rules, update: Update) -> bool:
    before = update[0]
    for after in update[1:]:
        if after not in rules[before]:
            return False
        before = after
    return True


def fix_order(rules: Rules, update: Update) -> Update:
    unordered: Update = list(update)
    ordered: Update = []
    while unordered:
        checking: int | None = unordered.pop(0)
        for against in unordered:
            if checking in rules[against]:
                unordered.append(checking)
                checking = None
                break
        if checking is not None:
            ordered.append(checking)
    return ordered


def part_1(rules: Rules, updates: list[Update]) -> int:
    total = 0
    for update in updates:
        if is_ordered(rules, update):
            total += update[len(update) // 2]
    return total


def part_2(rules: Rules, updates: list[Update]) -> int:
    total = 0
    for update in updates:
        if is_ordered(rules, update):
            continue
        ordered = fix_order(rules, update)
        total += ordered[len(ordered) // 2]
    return total


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("Example Usage: python solution.py {input_file}")

    rules: Rules = defaultdict(set)
    updates: list[Update] = []
    ruling = True
    with open(sys.argv[1]) as f:
        for l in map(lambda l: l.strip(), f.readlines()):
            if not l:
                ruling = False
                continue
            if ruling:
                before, after = map(int, l.split("|"))
                rules[before].add(after)
            else:
                updates.append(list(map(int, l.split(","))))

    print(f"Part 1: {part_1(rules, updates)}")
    print(f"Part 2: {part_2(rules, updates)}")
