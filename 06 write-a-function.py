# https://www.hackerrank.com/challenges/write-a-function/problem

def is_leap(year):

    # Write your logic here
    if not year % 400:
        return True
    elif not year % 100:
        return False
    elif not year % 4:
        return True
    else:
        return False


year = int(input())
print(is_leap(year))
