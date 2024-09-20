# https://www.hackerrank.com/challenges/merge-the-tools/problem

def subsequence(word):
    dictionary = {}
    result = ""

    for letter in word:
        if letter in dictionary.keys():
            continue
        else:
            dictionary[letter] = 1
            result += letter
    return result


def merge_the_tools(string, k):
    # your code goes here
    for i in range(int(len(string)/k)):
        result = subsequence(string[i*k:(i+1)*k])
        print(result)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
