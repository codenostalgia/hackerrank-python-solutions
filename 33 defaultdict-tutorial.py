# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict


def check(list1, list2):

    records = defaultdict(list)

    for i, l in enumerate(list1):
        records[l].append(i+1)

    for l in list2:
        if records[l]:
            for x in records[l]:
                print(x, end=' ')
            print('')
        else:
            print("-1")


if __name__ == '__main__':

    n, m = tuple(map(int, input().split()))
    list1 = []
    list2 = []

    for _ in range(n):
        list1.append(input())

    for _ in range(m):
        list2.append(input())

    check(list1, list2)
