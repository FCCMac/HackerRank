import os
import datetime

def time_delta(t1, t2):
    t1 = datetime(t1)
    t2 = datetime(t2)
    return datetime.timedelta(t1, t2)
    pass

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')
    
    fptr.close()