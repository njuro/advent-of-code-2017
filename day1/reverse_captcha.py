'''
https://adventofcode.com/2017/day/1
'''


def reverse_captcha(halfway=False):
    with open("input.txt", 'r') as input:
        captcha = input.read().replace('\n', "")
        result = 0
        shift = len(captcha) / 2 if halfway else 1
        for index, n in enumerate(captcha):
            next = int((index + shift) % len(captcha))
            if n == captcha[next]:
                result += int(n)

        return result


# Part 1
print(reverse_captcha())
# Part 2
print(reverse_captcha(halfway=True))
