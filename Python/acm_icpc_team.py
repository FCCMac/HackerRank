# return an integer array (list) with two elements: the max. number of topics any team can know and the
# number of teams that can be formed that know the max. number of topics

from itertools import combinations
import collections
import operator

def acmTeam(topic):

    max = 0
    count = 0

    for team in combinations(topic, 2):
        sum = bin(int(team[0], 2) | int(team[1], 2)).count("1")
        if sum > max:
            count = 1
            max = sum
        elif sum == max:
            count += 1
    
    return max, count

if __name__ == "__main__":
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])

    topic = []
    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    print("\n".join(map(str, result)))
    print("\n")