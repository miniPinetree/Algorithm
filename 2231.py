<<<<<<< HEAD
n = int(input())
rst = []

for i in range(n):
    sum = i
    for char in str(i):
        sum += int(char)
    if sum == n:
        rst.append(i)
if rst:
    rst.sort()
    print(rst[0])
else:
    print(0)
=======
n = int(input())
rst = []

for i in range(n):
    sum = i
    for char in str(i):
        sum += int(char)
    if sum == n:
        rst.append(i)
if rst:
    rst.sort()
    print(rst[0])
else:
    print(0)
>>>>>>> 88d5abf5fdf1224584809c4f7ffbcfc6b01b5095
