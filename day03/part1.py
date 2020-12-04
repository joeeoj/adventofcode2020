def find_tree(row, index):
    if index > len(row):
        row = row * ((index // len(row)) + 1)
    if row[index] == '#':
        return 1
    return 0


if __name__ == '__main__':
    with open('input.txt') as f:
        data = [r.strip() for r in f.readlines()]

    indices = range(0, len(data) * 3, 3)
    tree_count = 0
    for row, i in zip(data, indices):
        tree_count += find_tree(row, i)

    print(f'Total trees: {tree_count}')
