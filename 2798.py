<<<<<<< HEAD
import sys
r= sys.stdin.readline
n,m = map(int, r().split())
card = list(map(int,r().split()))
rst = 0 

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if card[i]+card[j]+card[k] <= m:
                rst = max(rst,card[i]+card[j]+card[k])
print(rst)
=======
import sys
r= sys.stdin.readline
n,m = map(int, r().split())
card = list(map(int,r().split()))
rst = 0 

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if card[i]+card[j]+card[k] <= m:
                rst = max(rst,card[i]+card[j]+card[k])
print(rst)
>>>>>>> 88d5abf5fdf1224584809c4f7ffbcfc6b01b5095
