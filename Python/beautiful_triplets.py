# https://www.hackerrank.com/challenges/beautiful-triplets/problem

# Given a sequence of integers, a, a triplet (a[i], a[j], a[k]) is beautiful if:
# a[j] - a[i] = a[k] - a[j] = d

# Given an increasing sequence of integers and the value of d, return the number
# of beautiful triplets in the sequence.

def beautifulTriplets(d, arr):
    """
    Returns the number of triplets in arr where
    i < j < k
    and
    a[j] - a[i] = a[k] - a[j] = d
    """

    beautiful_count = 0

    # if the array contains any values where the value plus d and plus 2 * d are
    # also in the array, the value is beautiful. This approach yields an average
    # time complexity of O(n ** 2) due to the "in" operator.
    for _ in range(len(arr)):
        if arr[_] + d in arr and arr[_] + 2 * d in arr:
            beautiful_count += 1

    return beautiful_count

if __name__ == "__main__":
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    print(str(result) + '\n')

