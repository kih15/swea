import sys
sys.stdin = open('sample_input.txt')
from collections import deque

mydeque = deque()
def perm(N):
    while N == M:
        for

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    num = N
    operator = [num+1, num-1, num*2, num-10]