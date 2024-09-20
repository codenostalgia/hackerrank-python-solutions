# https://www.hackerrank.com/challenges/itertools-permutations/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations


def find_permutation(string, size):
    perm = list(permutations(string, size))
    perm.sort()

    for p in perm:
        print(''.join(p))


if __name__ == '__main__':
    string, size = tuple(input().split())
    size = int(size)
    find_permutation(string, size)
