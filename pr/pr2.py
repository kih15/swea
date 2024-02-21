'''
이 배열은 split() 사용
3
1 2 3
4 5 6
7 8 9
3
123
456     이 배열은 split() 사용 안함
789
'''
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)
arr2 = [[0]*N for _ in range(N)] # 2차원 배열 만들기
# arr3 처럼 하면 안됨.
# arr3 = [[0]*N]*N # 얕은 복사를 하는 효과가 있어서 이렇게 하면 안됨
print(arr2)
arr2[0][0] = 1
print(arr2)