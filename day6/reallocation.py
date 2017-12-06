'''
https://adventofcode.com/2017/day/6
'''


def reallocation():
    with open("input.txt", 'r') as input:
        banks = list(map(int, input.readline().split()))
        size = len(banks)
        seen = [[]]
        steps = 0

        while banks not in seen:
            seen.append(banks[:])
            steps += 1
            max_index = banks.index(max(banks))
            max_val = banks[max_index]
            banks[max_index] = 0
            for i in range(1, max_val + 1):
                banks[(max_index + i) % size] += 1

        return seen, banks


cycles, last = reallocation()
# Part 1
print(len(cycles))
# Part 2
print(len(cycles) - cycles.index(last))
