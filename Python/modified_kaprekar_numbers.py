# https://www.hackerrank.com/challenges/kaprekar-numbers/problem

# Given two positive integers, p and q, where p < q, print the modified Kaprekar
# numbers in the range between p and q, inclusive.

def kaprekarNumbers(p, q):
    results = []

    for number in range(p, q + 1):
        d = len(str(number))
        n = number ** 2

        str_n = str(n)

        r = str_n[-d:]
        l = str_n[:-d]

        candidate_value = int(r.strip() or 0) + int(l.strip() or 0)

        if candidate_value == number:
            results.append(str(candidate_value))

    if results == []:
        print('INVALID RANGE')
    else:
        print(' '.join(results))


if __name__ == "__main__":
    p = int(input())
    q = int(input())

    kaprekarNumbers(p, q)

