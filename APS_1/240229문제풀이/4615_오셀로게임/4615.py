import sys
sys.stdin = open('sample_input(1).txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input())
    for i in range(M):
        x, y, d = map(int, input().split())
        
