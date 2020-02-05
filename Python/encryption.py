# hackerrank.com/challenges/encryption/problem

# return a string composed as described in the problem statement

import math

def encryption(s):
    """
    Takes in a string, s, and outputs an encrypted string.
    """
    # clean out any spaces in the input
    s = s.replace(' ','')

    # determine size of grid
    L = len(s)
    result_groups = math.ceil(math.sqrt(L))

    # create the output string using slicing
    result = ''
    for group in range(result_groups):
        result += s[group::result_groups] + ' '

    # the way I'm doing it will always append an extra space, so I need to remove it in the return
    return result.strip()


if __name__ == "__main__":
    s = input()
    result = encryption(s)
    print(result + '\n')

