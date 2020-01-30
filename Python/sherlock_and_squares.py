# return the number of squares within a range of integers, inclusive of endpoints
import math

def squares(a, b):

    # creates a range of possible squares between the lowest and highest squares possible in the range. the number of squares in this range is the answer
    return len(range(math.ceil(math.sqrt(a)), math.floor(math.sqrt(b)) + 1))


if __name__ == "__main__":
    q = int(input())

    for q_itr in range(q):
        ab = input().split()
        a = int(ab[0])
        b = int(ab[1])
    
        result = squares(a, b)
        print(result)

