import sys

Grid = list[list[str]]
Point = tuple[int, int]
Path = list[Point]
Vector = tuple[int, int]


ALL_NEIGHBORS: list[Vector] = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
]

DIAGONALS: list[Vector] = [
    (-1, -1),
    (-1, 1),
    (1, 1),
    (1, -1),
]


def find_paths(word: str, grid: Grid, directions: list[Vector]) -> list[Path]:
    paths: list[Path] = []
    height = len(grid)
    width = len(grid[0])
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c != word[0]:
                continue

            for d in directions:
                path = [(y, x)]
                for i, ci in enumerate(word[1:]):
                    dy = y + d[0] * (i + 1)
                    dx = x + d[1] * (i + 1)
                    if not (
                        0 <= dy < height and 0 <= dx < width and grid[dy][dx] == ci
                    ):
                        continue
                    path.append((dy, dx))
                if len(path) == len(word):
                    paths.append(path)
    return paths


def part_1(grid: Grid) -> int:
    paths = find_paths("XMAS", grid, ALL_NEIGHBORS)
    return len(paths)


def part_2(grid: Grid) -> int:
    count = 0
    paths = find_paths("MAS", grid, DIAGONALS)
    centers: set[Point] = set()
    for p in paths:
        if p[1] in centers:
            count += 1
        centers.add(p[1])
    return count


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("Example Usage: python solution.py {input_file}")

    with open(sys.argv[1]) as f:
        lines = [list(l.strip()) for l in f.readlines()]

    print(f"Part 1: {part_1(lines)}")
    print(f"Part 2: {part_2(lines)}")
