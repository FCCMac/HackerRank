# https://hackerrank.com/challenges/2d-array/problem

# Given a 6x6 array, arr, we define an hourglass in A to be a subset of values
# with indices falling in this pattern in arr's graphical representation:
# a b c
#   d
# e f g

# There are 16 hourglasses in arr, and an hourglass sum is the sum of an
# hourglass's values. Calculate the hourglass sum for every hourglass in arr,
# then print the maximum hourglass sum.

def hourglassSum(arr):

    for i in range(4):
        for j in range(4):
            sum = arr[j + 0][i + 0] + arr[j + 0][i + 1] + arr[j + 0][i + 2] + arr[j + 1][i + 1] + arr[j + 2][i + 0] + arr[j + 2][i + 1] + arr[j + 2][i + 2]

            if i == 0 and j == 0:
                max_sum = sum

            if sum > max_sum:
                max_sum = sum

    return max_sum

if __name__ == "__main__":
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    result = hourglassSum(arr)
    print(str(result) + '\n')

