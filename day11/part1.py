from typing import Dict, List, Tuple


Seats = Dict[Tuple[int, int], str]

def list_to_dict(data: List[List[str]]) -> Seats:
    """Convert from a list of lists to a dict of tuples with row/col as the keys and the string seat
    as the value."""
    rows_cols = [(r, c) for r in range(len(data)) for c in range(len(data[0]))]
    return {(r,c): data[r][c] for r,c in rows_cols}

def get_surrounding_seats(data: Seats, row: int, col: int) -> str:
    """Given a dict of Seats and a specific row/col, return a concatenated string of all adjacent
    seats values."""
    vals = [
        (row, col-1),    # left
        (row-1, col-1),  # upper left
        (row-1, col),    # up
        (row-1, col+1),  # upper right
        (row, col+1),    # right
        (row+1, col+1),  # lower right
        (row+1, col),    # down
        (row+1, col-1),  # lower left
    ]

    return ''.join([data.get(v, '') for v in vals])

def update_seats(data: Seats) -> Seats:
    """Given a dict of Seats, iterate through and update into a new Seats dict."""
    new_data = dict()
    for (r,c), seat in data.items():
        surrounding_seats = get_surrounding_seats(data, r, c)

        # If a seat is empty (L) and there are no occupied (#) seats adjacent to it, the seat becomes occupied (#)
        if seat == 'L' and '#' not in surrounding_seats:
            new_data[(r,c)] = '#'
        # If a seat is occupied (#) and four or more seats adjacent to it are also occupied (#), the seat becomes empty (L)
        elif seat == '#' and surrounding_seats.count('#') >= 4:
            new_data[(r,c)] = 'L'
        else:
            new_data[(r,c)] = seat
    return new_data

def count_occupied(data: Seats) -> int:
    """Return the total number of occupied seats."""
    return ''.join(data.values()).count('#')


if __name__ == '__main__':
    with open('input.txt') as f:
        seat_list = f.read().split('\n')
    seat_dict = list_to_dict(seat_list)

    for i in range(1, 200):
        start = count_occupied(seat_dict)
        seat_dict = update_seats(seat_dict)
        end = count_occupied(seat_dict)

        if start == end:
            print(f'The answer is: {(end)} (on round {i})')
            break
