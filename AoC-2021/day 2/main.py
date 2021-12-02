with open('input.txt', 'r') as f:
    data = f.read().splitlines()


def star_one(data):
    depth = 0
    horizontal_position = 0
    for line in data:

        # only forward has an 'a' in it
        if 'a' in line:
            _, value = line.split(' ')
            horizontal_position += int(value)

        # only down has a 'n' in it
        elif 'n' in line:
            _, value = line.split(' ')
            depth += int(value)

        # it has to be up in else case since there is neither 'a' or 'n' in 'up'
        else:
            _, value = line.split(' ')
            depth -= int(value)
    return horizontal_position * depth


print(star_one(data))


################################################################

def star_two(data):
    depth = 0
    horizontal_position = 0
    aim = 0
    for line in data:

        # only 'forward' has an 'a' in it
        if 'a' in line:
            _, value = line.split(' ')
            horizontal_position += int(value)
            depth += aim * int(value)

        # only 'down' has a 'n' in it
        elif 'n' in line:
            _, value = line.split(' ')
            aim += int(value)

        # it has to be up in else case since there is neither 'a' or 'n' in 'up'
        else:
            _, value = line.split(' ')
            aim -= int(value)
    return horizontal_position * depth


print(star_two(data))
