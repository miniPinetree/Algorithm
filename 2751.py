<<<<<<< HEAD
import sys
r = sys.stdin.readline
n = int(r())
num_list = [] 

for _ in range(n):
    num = int(r())
    num_list.append(num)

num_list.sort()

for num in num_list:
=======
import sys
r = sys.stdin.readline
n = int(r())
num_list = [] 

for _ in range(n):
    num = int(r())
    num_list.append(num)

num_list.sort()

for num in num_list:
>>>>>>> 88d5abf5fdf1224584809c4f7ffbcfc6b01b5095
    print(num)