from collections import namedtuple
from typing import List, Tuple


Seat = namedtuple('Seat', ['row', 'col', 'seat_id'])

def binary_split(input_range: List[int], part) -> List[int]:
    mid = len(input_range) // 2

    if part == 'F' or part == 'L':
        return input_range[:mid]
    elif part == 'B' or part == 'R':
        return input_range[mid:]
    else:
        return None

def calc_seat_id(row, col):
    return (row * 8) + col

def parse_pass(boarding_pass: str) -> Seat:
    rows = list(range(128))
    cols = list(range(8))

    row_part = boarding_pass[:7]
    col_part = boarding_pass[7:]

    for c in row_part:
        rows = binary_split(rows, c)

    for c in col_part:
        cols = binary_split(cols, c)

    row, col = rows[0], cols[0]
    seat_id = calc_seat_id(row, col)

    return Seat(row, col, seat_id)


if __name__ == '__main__':
    with open('input.txt') as f:
        data = [row.strip() for row in f.readlines()]

    seats = [parse_pass(p) for p in data]

    seat_ids = [s.seat_id for s in seats]
    all_seat_ids = [calc_seat_id(r, c) for r in range(128) for c in range(8)]
    missing_seat_ids = set(all_seat_ids) - set(seat_ids)

    # the seats with IDs +1 and -1 from yours will be in your list
    below = set([s-1 for s in missing_seat_ids])
    above = set([s+1 for s in missing_seat_ids])

    ans = list(missing_seat_ids - above - below)[0]
    print(ans)
