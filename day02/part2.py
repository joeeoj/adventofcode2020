def index_password_checker(line):
    min_max, char, password = line.split(' ')
    first_index, second_index = [int(i)-1 for i in min_max.split('-')]
    char = char.replace(':', '')

    char_count = password.count(char)

    # bitwise exclusive or
    if (password[first_index] == char) ^ (password[second_index] == char):
        return True
    return False


if __name__ == '__main__':
    with open('input.txt') as f:
        data = [row.strip() for row in f.readlines()]

    correct_passwords = sum([index_password_checker(row) for row in data])
    print(f'{correct_passwords:,} passwords are correct out of {len(data):} total passwords')
