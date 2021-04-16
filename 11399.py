<<<<<<< HEAD
import sys
r=sys.stdin.readline
n = int(r())
p_list = sorted(list(map(int, r().split())))
dp = [p_list[0]]
for p in p_list[1:]:
        dp.append(dp[-1]+p)
=======
import sys
r=sys.stdin.readline
n = int(r())
p_list = sorted(list(map(int, r().split())))
dp = [p_list[0]]
for p in p_list[1:]:
        dp.append(dp[-1]+p)
>>>>>>> 88d5abf5fdf1224584809c4f7ffbcfc6b01b5095
print(sum(dp))