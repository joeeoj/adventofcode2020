from collections import namedtuple
from typing import List


Operation = namedtuple('Operation', ['cmd', 'num', 'index'])


def operation_parser() -> List[Operation]:
    data = []
    with open('input.txt') as f:
        for i, row in enumerate(f.readlines()):
            cmd, num = row.strip().split(' ')
            data.append(Operation(cmd, int(num), i))
    return data

def find_loop(data: List[Operation]) -> int:
    acc, i = 0, 0
    seen = set()

    while True:
        op = data[i]

        if op in seen:
            return acc
        seen.update([op])

        if op.cmd == 'acc':
            acc += op.num
            i += 1
        elif op.cmd == 'nop':
            i += 1
        elif op.cmd == 'jmp':
            i += op.num


if __name__ == '__main__':
    data = operation_parser()
    print(find_loop(data))
