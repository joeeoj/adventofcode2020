import functools
from operator import mul
import time


def simple_timer(func):
    """Simple decorator to give a rough estimate of calculation time. Thank you to RealPython for
    the help -- https://realpython.com/primer-on-python-decorators/"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        ans = func(*args, **kwargs)
        print(f'{func.__name__!r} run in {time.perf_counter() - start:.6f}')
        return ans
        
    return wrapper

@simple_timer
def brute_force(data):
    """Loop through twice to get the answer. It ain't pretty but it works."""
    for j in data:
        for k in data:
            if j == k:
                continue
            if j + k == 2020:
                return (j * k)
    return None

@simple_timer
def complement_calc(data):
    """Loop through once to find the complements, then get the union of the complements and the
    original list to find the pairs that equal 2020. Multiply for the final result."""
    complements = set([2020 - row for row in data])
    result = set(data) & complements
    return mul(*[v for v in result])


if __name__ == '__main__':
    with open('input.txt') as f:
        data = [int(i.strip()) for i in f.readlines()]

    # quick enough
    brute_force_ans = brute_force(data)
    print(f'Brute force answer: {brute_force_ans}\n')

    # but much faster
    complement_ans = complement_calc(data)
    print(f'Complement answer: {complement_ans}')
