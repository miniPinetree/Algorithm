<<<<<<< HEAD
k = int(input())
stack = []
for _ in range(k):
    n = int(input())
    if n:
        stack.append(n)
    else:
        stack.pop()
=======
k = int(input())
stack = []
for _ in range(k):
    n = int(input())
    if n:
        stack.append(n)
    else:
        stack.pop()
>>>>>>> 88d5abf5fdf1224584809c4f7ffbcfc6b01b5095
print(sum(stack))