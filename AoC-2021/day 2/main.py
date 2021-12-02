with open('input.txt', 'r') as f:
    data = f.read().splitlines()


def star_one(data : list) -> int:
    depth = 0
    horizontal_position = 0
    for line in data:
        direction, value = line.split(' ')
        if direction == 'forward':
            horizontal_position += int(value)

        elif direction == 'down':
            depth += int(value)

        else:
            depth -= int(value)
    return horizontal_position * depth


print(star_one(data))


################################################################

def star_two(data : list) -> int:
    depth = 0
    horizontal_position = 0
    aim = 0
    for line in data:
        direction, value = line.split(' ')
        if direction == 'forward':
            horizontal_position += int(value)
            depth += aim * int(value)

        elif direction == 'down':
            aim += int(value)

        else:
            aim -= int(value)
    return horizontal_position * depth


print(star_two(data))
