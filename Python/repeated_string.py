# https://www.hackerrank.com/challenges/repeated-string/problem

# Given an integer, n, find and print the number of letter 'a's in the first n
# letters of Liliah's infinite string.
import math

def repeatedString(s, n):
    """
    Returns the number of 'a's in the first n letters of a string consisting of
    infinitely repeating strings, s.
    """

    count = 0
    s_count_a = s.count('a')

    count += math.floor(n / len(s)) * s_count_a
    for _ in range(n % len(s)):
        if s[_] == 'a':
            count += 1

    return count


if __name__ == "__main__":
    s = input()
    n = int(input())

    result = repeatedString(s, n)
    print(str(result) + '\n')

