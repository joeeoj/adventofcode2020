from typing import List


def file_to_dicts(fname: str = 'input.txt') -> List[dict]:
    # wayyy easier way to split into each passport group
    with open(fname) as f:
        groups = f.read().split('\n\n')

    passports = []
    for group in groups:
        d = dict([g.split(':') for g in group.split()])
        passports.append(d)
    return passports


if __name__ == '__main__':
    passports = file_to_dicts()
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']  # cid not required
    ans = sum([set(p) >= set(required_fields) for p in passports])  # superset
    print(ans)
