def password_checker(line):
    min_max, char, password = line.split(' ')
    min_count, max_count = [int(i) for i in min_max.split('-')]
    char = char.replace(':', '')

    char_count = password.count(char)

    if char_count >= min_count and char_count <= max_count:
        return True
    return False


if __name__ == '__main__':
    with open('input.txt') as f:
        data = [row.strip() for row in f.readlines()]

    correct_passwords = sum([password_checker(row) for row in data])
    print(f'{correct_passwords:,} passwords are correct out of {len(data):} total passwords')
