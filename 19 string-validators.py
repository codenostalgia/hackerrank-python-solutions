# https://www.hackerrank.com/challenges/string-validators/problem

if __name__ == '__main__':

    s = input()
    output = [False for i in range(5)]

    for lett in s:
        if lett.isalnum():
            output[0] = True
        if lett.isalpha():
            output[1] = True
        if lett.isdigit():
            output[2] = True
        if lett.islower():
            output[3] = True
        if lett.isupper():
            output[4] = True

    for boo in output:
        print(boo)
