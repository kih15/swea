import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
female = [0] * 7
male = [0] * 7
# N: 학생수, K: 방 최대 인원수
for _ in range(N):
    S, Y = map(int, input().split())