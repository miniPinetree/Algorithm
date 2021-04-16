<<<<<<< HEAD
# 올바른 괄호문자열 VPS가 성립하지 않는 조건
# )가 입력되었는데 남아있는 괄호가 없다.
# 문자열이 끝났을 때 stack에 남은 괄호가 있다.

import sys
r=sys.stdin.readline

t = int(r().rstrip())
for _ in range(t):
    data = list(map(str, r().rstrip()))
    stack = []
    rst = []
    true_flag = 1
    for char in data:
        if char =='(':
            stack.append(char)
        elif char==')':
            if stack:
                stack.pop()
            else:
                true_flag = 0
                break
=======
# 올바른 괄호문자열 VPS가 성립하지 않는 조건
# )가 입력되었는데 남아있는 괄호가 없다.
# 문자열이 끝났을 때 stack에 남은 괄호가 있다.

import sys
r=sys.stdin.readline

t = int(r().rstrip())
for _ in range(t):
    data = list(map(str, r().rstrip()))
    stack = []
    rst = []
    true_flag = 1
    for char in data:
        if char =='(':
            stack.append(char)
        elif char==')':
            if stack:
                stack.pop()
            else:
                true_flag = 0
                break
>>>>>>> 88d5abf5fdf1224584809c4f7ffbcfc6b01b5095
    print("YES" if true_flag and not(stack) else "NO")