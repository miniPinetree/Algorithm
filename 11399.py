import sys
r=sys.stdin.readline
n = int(r())
p_list = sorted(list(map(int, r().split())))
dp = [p_list[0]]
for p in p_list[1:]:
        dp.append(dp[-1]+p)
print(sum(dp))