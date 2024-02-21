import sys
sys.stdin = open('input')

N = int(input()) # 2차원 리스트의 크기

# arr = []
# for _ in range(N):  # N번 반복
#     arr.append(list(map(int, input().split())))
# print(arr)

# [표현식 for _ in range(N)]
# [10*i for i in range(N)] # 임시 변수는 표현식 내부에서 사용 가능함

# arr2 = [표현식 for _ in range(N)] -> [표현식, 표현식, 표현식]
arr2 = [list(map(int, input().split())) for _ in range(N)] # -> [표현식, 표현식, list(map(int, input().split()))]
print(arr2)