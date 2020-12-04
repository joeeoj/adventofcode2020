# cid not required
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

with open('input.txt') as f:
    fields = []
    passports = []
    for row in f.readlines():
        curr = row.strip()
        if curr == '' and len(fields) > 0:
            passports.append(fields)
            fields = []

        split_row = curr.split(' ')
        parsed_row = [r.split(':')[0].strip() for r in split_row if r.split(':')[0].strip() != '']
        fields += parsed_row

# also add the very last row
passports.append(fields)

ans = 0
for passport in passports:
    if set(passport) >= set(required_fields):
        ans +=1

print(ans)
