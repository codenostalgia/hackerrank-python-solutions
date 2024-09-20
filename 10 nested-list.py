# https://www.hackerrank.com/challenges/nested-list/problem


if __name__ == '__main__':

    n = int(input())

    data = []

    for i in range(n):
        name = input()
        score = float(input())
        data.append([name, score])

    low = 101
    slow = 101

    names = []

    for i in range(n):
        if data[i][1] < low:
            slow = low
            low = data[i][1]
        elif data[i][1] < slow and not data[i][1] == low:
            slow = data[i][1]

    for i in range(n):
        if data[i][1] == slow:
            names.append(data[i][0])

    names.sort()

    for name in names:
        print(name)
