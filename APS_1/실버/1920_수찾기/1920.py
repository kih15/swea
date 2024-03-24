import sys
sys.stdin = open('input.txt')

import sys
N = int(sys.stdin.readline())
AN = set(sys.stdin.readline().split())
M = int(sys.stdin.readline())
AM = list(sys.stdin.readline().split())
for i in range(len(AM)):
    if AM[i] in AN:
        print(1)
    else:
        print(0)
