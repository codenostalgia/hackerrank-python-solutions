# https://www.hackerrank.com/challenges/python-tuples/problem


# submit by choosing language - pypy 3

if __name__ == '__main__':
    n = int(input())
    tup = tuple(int(x) for x in input().split())
    print(hash(tup))
