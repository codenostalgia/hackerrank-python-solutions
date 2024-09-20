# https://www.hackerrank.com/challenges/itertools-product/problem

from itertools import product


def cartesia_product(A, B):
    for tup in list(product(A, B)):
        print(tup, end=' ')


if __name__ == '__main__':
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cartesia_product(A, B)
