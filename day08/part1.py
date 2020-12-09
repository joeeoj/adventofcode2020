from collections import namedtuple
from typing import List


Operation = namedtuple('Operation', ['cmd', 'num'])
Executed = namedtuple('Executed', ['cmd', 'num', 'index'])

def operation_parser() -> List[Operation]:
    data = []
    with open('input.txt') as f:
        for row in f.readlines():
            cmd, num = row.strip().split(' ')
            data.append(Operation(cmd, int(num)))
    return data

def find_loop(data: List[Operation]) -> int:
    acc, i = 0, 0
    seen = set()

    while True:
        op = data[i]
        ex = Executed(op.cmd, op.num, i)  # includes index

        if ex in seen:
            return acc
        seen.update([ex])

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
