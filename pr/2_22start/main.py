import sys
sys.stdin = open('input.txt', 'r') # r은 read의 약자 파일을 읽어준다.
sys.stdout = open('output.txt', 'w')

a, b = map(int, input().split())
print(a + b, a * b)

# text = int(input())
# print(text)