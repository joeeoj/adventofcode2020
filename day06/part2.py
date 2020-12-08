with open('input.txt') as f:
    data = f.read().split('\n\n')

all_yeses = []
for row in data:
    group = row.split('\n')
    unique_chars = set(row.replace('\n', ''))
    all_chars = row.replace('\n', '')
    total = len(group)
    all_yeses.append(sum([1 for c in unique_chars if all_chars.count(c) == total]))

print(sum([y for y in all_yeses]))
