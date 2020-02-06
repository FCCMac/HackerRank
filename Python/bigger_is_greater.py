# http://hackerrank.com/challenges/bigger-is-greater/problem

# Given a word, create a new word by swapping some or all of its characters. This new word
# must meet two criteria:
# - It must be lexicographically greater than the first word
# - It must be the smallest word that fits the first condition
#
# Return a string that meets those criteria

def biggerIsGreater(w):
    if len(w) == 1:
        return "no answer"
    
    sorted_string = [w[-1]]
    for _ in range(-2, -(len(w) + 1), -1):
        if w[_] >= sorted_string[-1]:
            sorted_string.append(w[_])
        else:
            temp = w[_]
            for j in range(len(sorted_string)):
                if sorted_string[j] > temp:
                    sorted_string.insert(0, sorted_string[j])
                    sorted_string[j + 1] = temp
                    result = w[:_] + ''.join(sorted_string)
                    return result

    return "no answer"
    



if __name__ == "__main__":
    T = int(input())

    for T_itr in range(T):
        w = input()
        result = biggerIsGreater(w)
        print(result + '\n')

