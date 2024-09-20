# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    highest = -100
    runnerup = -100

    for x in arr:
        if x > highest:
            runnerup = highest
            highest = x
        elif x > runnerup and not x == highest:
            runnerup = x

    print(runnerup)
