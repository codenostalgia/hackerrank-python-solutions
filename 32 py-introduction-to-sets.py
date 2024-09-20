# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):

    # your code goes here
    distinct_heights = set(array)
    result = sum(distinct_heights)/len(distinct_heights)
    result = round(result, 3)

    return result


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
