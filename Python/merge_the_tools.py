import textwrap
from collections import OrderedDict

def merge_the_tools(string, k):
    substrings = textwrap.wrap(string, k)
    for _ in substrings:
        _ = ''.join(OrderedDict.fromkeys(_))
        print(_)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)