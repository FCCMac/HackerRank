# https://www.hackerrank.com/challenges/arrays-ds/problem
# Given an array, A, of n integers, print each element in reverse order as a
# single line of space-separated integers.

def reverseArray(a):
    a.reverse()
    return a


if __name__ == "__main__":

    arr = list(map(int, input().rstrip().split()))
    res = reverseArray(arr)
    print(' '.join(map(str, res)))

