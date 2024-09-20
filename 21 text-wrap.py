# https://www.hackerrank.com/challenges/text-wrap/problem

import textwrap

'''
def wrap(string, max_width):

    n = len(string)
    start = 0
    modified_string = ''

    while start<=n-1:
        if modified_string!='':
            modified_string += '\n'
        modified_string += string[start:start+max_width]
        start += max_width

    return modified_string
'''


def wrap(string, max_width):
    mywrapper = textwrap.TextWrapper(max_width)
    return mywrapper.fill(string)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
