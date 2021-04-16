import sys
from collections import deque

def bfs(x,y):
    global cnt
    cnt = 0
    queue = deque([])
    queue.append([x,y])
    while queue:
        x,y=queue.popleft()
        if 0<=x<n and 0<=y<n:
            if n_map[x][y]==1:
                cnt+=1
                n_map[x][y] =0 #중복비교 방지를 위해 방문한 곳은 지도에 0으로 표시
                queue.append([x-1,y])
                queue.append([x+1,y])
                queue.append([x,y-1])
                queue.append([x,y+1])
    return cnt
        
n=int(input())
n_map = [list(map(int,input())) for _ in range(n)]
cnt=0
apt=[]
apt_complex=0

#지도에 1인 좌표에 대해 함수를 호출하는 반복문
for i in range(n):
    for j in range(n):
        if n_map[i][j]==1:
            bfs(i,j)
            apt_complex +=1
            apt.append(cnt)
apt.sort()
print(apt_complex)
print(*apt, sep='\n')

