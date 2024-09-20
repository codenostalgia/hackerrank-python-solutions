# https://www.hackerrank.com/challenges/collections-counter/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter


def calculate_profit(shoes, desires):

    counts = Counter(shoes)
    profit = 0

    for desire in desires:
        if desire[0] in counts.keys():
            if counts[desire[0]] > 0:
                profit += desire[1]
                counts[desire[0]] = counts[desire[0]]-1
    print(profit)


if __name__ == '__main__':
    x = int(input())
    shoes = list(map(int, input().split()))
    n = int(input())
    desires = []

    for _ in range(n):
        tup = tuple(map(int, input().split()))
        desires.append(tup)

    calculate_profit(shoes, desires)
