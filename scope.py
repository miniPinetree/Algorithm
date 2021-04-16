import sys
r=sys.stdin.readline
n = int(r())

s=[]
e=[]
for _ in range(n):
    time = list(map(str, r().strip().split("~")))
    s.append(time[0])
    e.append(time[1])

s.sort()
e.sort()

if  s[n-1][0:2] > e[0][1:3]:
    print(-1)
elif s[n-1][0:2] == e[0][1:3] and s[n-1][3:]>e[0][4:]:
    print(-1)
else:
    print(s[n-1]+"~"+e[0])
