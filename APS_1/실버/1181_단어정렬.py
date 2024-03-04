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
# print(my_list)
for i in range(len(my_list)):
    lst.append(len(my_list[i]))
    lst.sort()
print(lst)
