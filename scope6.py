import sys

n,m = map(int,sys.stdin.readline().strip().split())

b = [list(map(int,sys.stdin.readline().split())) for _ in range(m)]

rst = [[0]*n for _ in range(m)]

for i in range(m):
    for j in range(n):
        if i==0:
            if j==0:
                rst[i][j]= b[i][j]
            else:
                rst[i][j]= rst[i][j-1]+b[i][j]
        elif i!=0 and j==0:
            rst[i][j]=rst[i-1][j]+b[i][j]
            
        else:
            rst[i][j]= max(rst[i-1][j],rst[i][j-1])+b[i][j]
print(max(rst[-1]))