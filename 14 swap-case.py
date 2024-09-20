# https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):

    swapped_case = ''
    for lett in s:
        if lett.isupper():
            swapped_case += lett.lower()
        else:
            swapped_case += lett.upper()
    return swapped_case


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
