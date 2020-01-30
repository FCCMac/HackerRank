# Given an integer, k, and two strings, s and t, determine whether or not you can convert s to t by performing exactly 
# k of the above operations on s. If it's possible, print Yes. Otherwise, print No.

def appendAndDelete(s, t, k):

    if len(s) + len(t) < k:
        return "Yes"

    numberOfSharedCharacters = min(len(s), len(t))
    for i in range(numberOfSharedCharacters):
        if s[i] != t[i]:
            numberOfSharedCharacters = i
            break

    delta = (len(s) - numberOfSharedCharacters) + (len(t) - numberOfSharedCharacters)

    if (delta <= k and (delta - k) % 2 == 0) or len(s) + len(t) < k:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    s = input()
    t = input()
    k = int(input())

    result = appendAndDelete(s, t, k)

    print(result + '\n')

