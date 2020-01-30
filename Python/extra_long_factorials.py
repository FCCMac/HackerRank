# calculate and print the factorial of a given int

def extraLongFactorials(n):

    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        return n * extraLongFactorials(n - 1)

if __name__ == '__main__':
    n = int(input())

    print(extraLongFactorials(n))

