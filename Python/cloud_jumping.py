
# return an integer representing the nergy level remaining after the game concludes
import math

def jumpingOnClouds(c, k):
    n = len(c)

    # initial energy level
    e = 100

    index = 0
    while True:
        index += k
        index %= n
        e -= 1

        if c[index] == 1:
            e -= 2

        if index == 0:
            break

    return e

if __name__ == '__main__':
    c = [0, 0, 1, 0, 0, 1, 1, 0]
    k = 2

    print(jumpingOnClouds(c, k))