import sys
sys.stdin = open('input1.txt')

# 주로 인풋은 간선(E), 정점(V) 정보를 같이 줌
# 인접 배열을 저장할 때는 간선의 정보를 이용해서 저장하면 됨
# 인접 배열을 초기화할 때는 정점 정보를 이용하면 됨

V, E = map(int, input().split())
edge_list = list(map(int, input().split()))

# 정점 번호를 그대로 index 로 사용하기 위해 +1을 함
adj_list = [[] for _ in range(V+1)]


for idx in range(E):
    start = edge_list[idx*2]
    end = edge_list[idx*2+1]

    adj_list[start].append(end)
    adj_list[end].append(start)

for i in range(V+1):
    print(adj_list[i])