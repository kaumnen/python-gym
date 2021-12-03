with open('input.txt', 'r') as f:
    data = f.read().splitlines()



def star_one(data):
    gamma_list = [0 for x in range(12)]
    gamma = ''

    for i in data:
        for j in range(12):
            gamma_list[j] += 1 if int(i[j]) == 1 else -1

    for n in range(12):
        gamma += '0' if gamma_list[n] <= 0 else '1'
        epsilon = int(gamma, 2) ^ 0b111111111111

    return int(gamma, 2) * epsilon

print(star_one(data))
