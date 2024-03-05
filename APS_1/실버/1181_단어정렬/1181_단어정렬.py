import sys
sys.stdin = open('input.txt')

N = int(input())
my_set = set()
my_list = []
lst = []
for i in range(N):
    s = input()
    my_set.add(s)
    my_list = list(my_set)
my_list.sort()
my_list.sort(key=len)
# print(my_list)
# 알파벳을 그냥 정렬하면 abc순으로 된다..
# 글자수대로 정렬하고 싶으면 key=len을 사용하면 된다. 근데 글자수대로 정렬되고 사전순으로는 되지 않는다. 순서가 바뀜
# print(my_list)
for i in range(len(my_list)):
    print(my_list[i])

