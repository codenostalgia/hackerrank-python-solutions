# https://www.hackerrank.com/challenges/designer-door-mat/problem

def upper_dashes(line_index, N):

    # (3N-3)/2-3*line_index
    str_len = 3*(int((N-1)/2)-line_index)

    return "-"*str_len


def upper_middlepart(line_index, N):
    if line_index == 0:
        return ".|."
    dots = ['..'for i in range(line_index*2)]
    main_string = '|'.join(dots)
    return ".|"+main_string+"|."


def upper_structure(N):

    # total lines in upper part
    iters = int((N-1)/2)

    # Storing, so we can use it for lower part as well
    lines = []

    for line_index in range(iters):
        dashes = upper_dashes(line_index, N)
        line = dashes+upper_middlepart(line_index, N)+dashes
        lines.append(line)

    for line in lines:
        print(line)

    return lines


def central_line(N):
    print("WELCOME".center(3*N, '-'))


def lower_structure(lines):

    # printing upper structure lines in reverse order
    for line in lines[::-1]:
        print(line)


if __name__ == "__main__":
    N, M = tuple(map(int, input().split()))
    lines = upper_structure(N)
    central_line(N)
    lower_structure(lines)
