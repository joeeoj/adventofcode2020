import re


# cid not required
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

with open('input.txt') as f:
    fields = dict()
    passports = []
    for row in f.readlines():
        curr = row.strip()
        if curr == '' and len(fields) > 0:
            passports.append(fields)
            fields = dict()
            continue

        split_row = curr.split(' ')
        for item in split_row:
            k, v = item.strip().split(':')
            fields[k] = v

# also add the very last row
passports.append(fields)

def extra_rules(d):
    if len(d.get('byr')) != 4 or int(d.get('byr')) < 1920 or int(d.get('byr')) > 2002:
        return False
    elif len(d.get('iyr')) != 4 or int(d.get('iyr')) < 2010 or int(d.get('iyr')) > 2020:
        return False
    elif len(d.get('eyr')) != 4 or int(d.get('eyr')) < 2020 or int(d.get('eyr')) > 2030:
        return False

    if 'cm' not in d.get('hgt') and 'in' not in d.get('hgt'):
        return False
    elif 'cm' in d.get('hgt'):
        hgt = int(d.get('hgt').replace('cm', ''))
        if hgt < 150 or hgt > 193:
            return False
    elif 'in' in d.get('hgt'):
        hgt = int(d.get('hgt').replace('in', ''))
        if hgt < 59 or hgt > 76:
            return False

    if re.match(r'^#([0-9|a-f]{6})$', d.get('hcl')) is None:
        return False

    eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if d.get('ecl') not in eye_colors:
        return False

    if re.match(r'^([0-9]{9})$', d.get('pid')) is None:
        return False

    return True

ans = 0
for passport in passports:
    if set(passport.keys()) >= set(required_fields) and extra_rules(passport):
        ans +=1

print(ans)
