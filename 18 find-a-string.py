# https://www.hackerrank.com/challenges/find-a-string/problem


def check_if_same(str1, str2):
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    return True


def count_substring(string, sub_string):

    count = 0
    l1 = len(string)
    l2 = len(sub_string)

    if l2 > l1:
        return count

    for i in range(l1-l2+1):
        if check_if_same(string[i:i+l2], sub_string):
            count += 1

    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
