# return the minimum number of elements to delete from a given array to make all elements of the array equal
# ex. [1, 2, 2, 3] must become [2, 2], requiring 2 deletions

import collections

def equalizeArray(arr):
    return(collections.Counter(arr).most_common()[0][1])

if __name__ == "__main__":
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    print(str(n - result) + "\n")