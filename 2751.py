import sys
r = sys.stdin.readline
n = int(r())
num_list = [] 

for _ in range(n):
    num = int(r())
    num_list.append(num)

num_list.sort()

for num in num_list:
    print(num)