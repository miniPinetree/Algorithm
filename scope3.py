import sys
from collections import Counter
r=sys.stdin.readline
n = int(r())
p = [[0]*51 for _ in range(51)]

for i in range(1,n+1):
    j=1
    for char in str(r().strip()):
        p[i][j] = int(char)
        j +=1
cnt=0
max=1
for i in range(1,n+1):
    for j in range(1,n+1):
        if p[i][j] ==1:
            cnt +=1
            p[i][j] = min(p[i][j-1],p[i-1][j],p[i-1][j-1])+1
            if p[i][j] > max:
                max = p[i][j]

cnts=[0]*(max+1)
cnts[1] = cnt

for i in range(n+1):
    for j in range(2,max+1):
        cnts[j] += p[i].count(j)

print("total: {}".format(sum(cnts)))
for i in range(1,max+1):
    print("size[{}]: {}".format(i,cnts[i]))
