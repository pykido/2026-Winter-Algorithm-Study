import sys
input = sys.stdin.readline

str = input()
stack = []
result, tmp = 0, 1

for i in range(len(str)) :
    ch = str[i]

    if ch == '(' :
        tmp *= 2
        stack.append('(')
    elif ch == '[' :
        tmp *= 3
        stack.append('[')
    elif ch == ')' :
        if len(stack) == 0 or stack[-1] != '(':
            result = 0
            break
        if str[i-1] == '(' :
            result += tmp
        tmp //= 2
        stack.pop()
    elif ch == ']' :
        if len(stack) == 0 or stack[-1] != '[':
            result = 0
            break
        if str[i-1] == '[' :
            result += tmp
        tmp //= 3
        stack.pop()

if len(stack) != 0:
    result = 0

print(result)

# 곱하기 하나로 가능?
