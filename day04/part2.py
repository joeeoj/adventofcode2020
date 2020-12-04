import re
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

def check_range(str_val: str, lower: int, upper: int) -> bool:
    return lower <= int(str_val) <= upper 

def check_height(str_val: str, unit: str, lower, upper) -> bool:
    # first check if any valid unit contained
    if 'cm' not in str_val and 'in' not in str_val:
        return False
    # then skip if not the correct measurement
    if unit not in str_val:
        return True

    val = int(str_val.replace(unit, ''))
    return check_range(val, lower, upper)

def check_regex(input_str: str, pat: str) -> bool:
    return re.match(pat, input_str) is not None

def check_membership(input_str: str, items: list) -> bool:
    return input_str in items

def extra_checks(d: dict) -> bool:
    checks = [
        check_range(d.get('byr'), 1920, 2002),
        check_range(d.get('iyr'), 2010, 2020),
        check_range(d.get('eyr'), 2020, 2030),
        check_height(d.get('hgt'), 'cm', 150, 193),
        check_height(d.get('hgt'), 'in', 59, 76),
        check_regex(d.get('hcl'), r'#([0-9|a-f]{6})$'),
        check_membership(d.get('ecl'), ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']),
        check_regex(d.get('pid'), r'^([0-9]{9})$'),
    ]

    for check in checks:
        if not check:
            return False
    return True


if __name__ == '__main__':
    passports = file_to_dicts()

    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    ans = sum([set(p) >= set(required_fields) and extra_checks(p) for p in passports])
    print(ans)
