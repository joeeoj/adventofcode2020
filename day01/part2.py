import functools
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
            for n in data:
                if j == k:
                    continue
                if j == n:
                    continue
                if k == n:
                    continue

                if j + k + n == 2020:
                    return (j * k * n)
    return None


if __name__ == '__main__':
    with open('input.txt') as f:
        data = [int(i.strip()) for i in f.readlines()]

    brute_force_ans = brute_force(data)
    print(f'Brute force answer: {brute_force_ans}\n')
