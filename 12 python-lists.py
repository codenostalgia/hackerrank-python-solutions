# https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':

    N = int(input())
    records = []

    for i in range(N):

        cmd, *nums = input().split()
        nums = list(map(int, nums))

        if cmd == "insert":
            records.insert(nums[0], nums[1])
        elif cmd == "print":
            print(records)
        elif cmd == "remove":
            records.remove(nums[0])
        elif cmd == "append":
            records.append(nums[0])
        elif cmd == "sort":
            records.sort()
        elif cmd == "pop":
            records.pop()
        elif cmd == "reverse":
            records.reverse()
