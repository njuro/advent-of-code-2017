'''
https://adventofcode.com/2017/day/4
'''


def passphrase(anagrams=False):
    with open("input.txt", 'r') as input:
        result = 0
        for line in input.readlines():
            words = line.split()
            processed = [''.join(sorted(s)) for s in words] if anagrams else words
            result += 1 if len(set(processed)) == len(words) else 0
        return result


# Part 1
print(passphrase())
# Part 2
print(passphrase(anagrams=True))
