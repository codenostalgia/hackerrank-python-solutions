# https://www.hackerrank.com/challenges/alphabet-rangoli/problem


# e ->    j=0                              8
#         j=1                            6    10
#         j=2                       4               12
#         j=3                 2                           14
#         j=4            0                                       16

#  mid=8
#  position of e-> mid-2*j, mid+2*j


a_unicode = ord('a')


def upper_half(size, lines, mid):

    for i in range(size):
        char = a_unicode + size - i - 1
        for j, line in enumerate(lines[i:]):
            pos1 = mid-2*j
            pos2 = mid+2*j
            line[pos1] = chr(char)
            line[pos2] = chr(char)

    for line in lines:
        print("".join(line))


def lower_half(lines):
    for line in lines[:-1][::-1]:
        print("".join(line))


def print_rangoli(size):

    # width = size+(size-1)+(size+size-1)-1
    width = 4*size-3
    lines = [['-' for i in range(width)] for j in range(size)]
    mid = int(width/2)

    upper_half(size, lines, mid)
    lower_half(lines)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
