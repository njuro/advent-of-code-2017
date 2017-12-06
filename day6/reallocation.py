'''
https://adventofcode.com/2017/day/6
'''


def reallocation(cycle=False):
    with open("input.txt", 'r') as input:
        banks = list(map(int, input.readline().split()))
        size = len(banks)
        seen = [[]]
        marker = None
        steps = 0

        while True:
            steps += 1
            max_index = banks.index(max(banks))
            max_val = banks[max_index]
            banks[max_index] = 0
            for i in range(1, max_val + 1):
                banks[(max_index + i) % size] += 1
            if banks in seen:
                if cycle:
                    if not marker:
                        marker = banks[:]
                        steps = 0
                    elif banks == marker:
                        break
                else:
                    break
            else:
                seen.append(banks[:])

        return steps


# Part 1
print(reallocation())
# Part 2
print(reallocation(cycle=True))
