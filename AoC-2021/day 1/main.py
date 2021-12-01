with open('input.txt', 'r') as f:
    data = f.read().splitlines()


def first_star(data):
    result = 0
    for i in range(len(data) - 1):
        if data[i + 1] > data[i]:
            result += 1
    return result


print(first_star(data))


################################################################

def get_three_measurements(data, index):
    try:
        return [int(data[index]), int(data[index + 1]), int(data[index + 2])]
    except IndexError:
        return [None, None, None]


def second_star(data):
    previous = sum(get_three_measurements(data, 0))
    result2 = 0
    i = 1
    while True:
        three_measurements = get_three_measurements(data, i)
        if None in three_measurements:
            break

        temp_sum = sum(three_measurements)
        if temp_sum > previous:
            result2 += 1

        previous = temp_sum
        i += 1
    return result2


print(second_star(data))
