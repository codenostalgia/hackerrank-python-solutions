# https://www.hackerrank.com/challenges/the-minion-game/problem

def scores(word):

    vowels = ['A', 'E', 'I', 'O', 'U']
    stuart = 0
    kevin = 0
    n = len(word)

    for i in range(n):
        if word[i] not in vowels:
            stuart += n-i
        else:
            kevin += n-i

    return stuart, kevin


def minion_game(string):

    # your code goes here
    stuart, kevin = scores(string)

    if stuart > kevin:
        print("Stuart", stuart)
    elif stuart < kevin:
        print("Kevin", kevin)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
