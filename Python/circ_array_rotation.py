#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):

    # use negative indexing to reorder the list
    d = deque(a)
    d.rotate(k)

    return [d[i] for i in queries]
    

if __name__ == '__main__':

    a = [1, 2, 3]
    k = 2
    queries = [0, 1, 2]

    result = circularArrayRotation(a, k, queries)

