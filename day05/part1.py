from typing import List, Tuple


def binary_split(input_range: List[int], part) -> List[int]:
    mid = len(input_range) // 2

    if part == 'F' or part == 'L':
        return input_range[:mid]
    elif part == 'B' or part == 'R':
        return input_range[mid:]
    else:
        return None

def parse_pass(boarding_pass: str) -> Tuple[int]:
    rows = list(range(128))
    cols = list(range(8))

    row_part = boarding_pass[:7]
    col_part = boarding_pass[7:]

    for c in row_part:
        rows = binary_split(rows, c)

    for c in col_part:
        cols = binary_split(cols, c)

    row, col = rows[0], cols[0]
    seat_id = (row * 8) + col

    return (row, col, seat_id)


if __name__ == '__main__':
    with open('input.txt') as f:
        data = [row.strip() for row in f.readlines()]

    seats = [parse_pass(p) for p in data]

    ans = max([s[2] for s in seats])
    print(ans)
