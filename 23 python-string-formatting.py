# https://www.hackerrank.com/challenges/python-string-formatting/problem

def num_reps(num, width):
    print(f'{num:>{width}} {oct(num)[2:]:>{width}} {
          hex(num)[2:].upper():>{width}} {bin(num)[2:]:>{width}}')


def print_formatted(number):
    # your code goes here
    width = len(bin(number)[2:])

    for ind in range(number):
        num_reps(ind+1, width)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
