# https://www.hackerrank.com/challenges/polar-coordinates/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from cmath import phase


def polar(complexnum):
    print(abs(complex(complexnum)))
    print(phase(complex(complexnum)))


if __name__ == '__main__':
    com = input()
    polar(com)
