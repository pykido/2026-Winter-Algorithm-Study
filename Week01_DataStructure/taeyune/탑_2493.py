import sys
input = sys.stdin.readline

N = int(input())
height = list(map(int, input().split()))

result = []
stack = []
for i in range(N):
    while len(stack) != 0 and height[i] >= stack[-1][0] :
        stack.pop()

    if len(stack) == 0 :
        result.append(0)
        stack.append((height[i], i + 1))
    else :
        result.append(stack[-1][1])
        stack.append((height[i], i + 1))


for i in range(N) :
    print(result[i], end = " ")


