# https://www.hackerrank.com/challenges/calendar-module/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar


def find_day(year, month, day):

    days = {
        0: 'MONDAY',
        1: 'TUESDAY',
        2: 'WEDNESDAY',
        3: 'THURSDAY',
        4: 'FRIDAY',
        5: 'SATURDAY',
        6: 'SUNDAY'}

    day = calendar.weekday(year, month, day)

    print(days[day])


if __name__ == '__main__':

    m, d, y = tuple(map(int, input().split()))
    find_day(y, m, d)
