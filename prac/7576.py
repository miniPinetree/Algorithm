import sys
from collections import deque

r = sys.stdin.readline

def bfs_tomato(M,N,box):
    # 상하좌우를 의미하는 좌표 배열
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    days = -1

    while coordinates_of_ripe_tomatoes:
        for _ in range(len(coordinates_of_ripe_tomatoes)):
            x, y = coordinates_of_ripe_tomatoes.popleft()
            #익은 토마토 좌표를 목록에서 뽑아오기

            # 상하좌우에 영향을 미치는 과정
            for i in range(4):
                x2 = x + dx[i]
                y2 = y + dy[i]

                if ((0<=x2<N) and (0<=y2<M) and (box[x2][y2]==0)):
                    box[x2][y2] = box[x][y] +1
                    #영향을 받은 토마토보다 하루 더 늦게 익었음을 표시
                    coordinates_of_ripe_tomatoes.append([x2,y2])
        days +=1 
        #현재 기준 익은 토마토 for문이 끝나면 하루를 증가시킨다.
    for row in box:
        if 0 in row:
            return -1
    return days

M, N = map(int,r().split())
box, coordinates_of_ripe_tomatoes = [],deque()
for i in range(N):
    row = list(map(int, r().split()))
    for j in range(M):
        if row[j] == 1:
            coordinates_of_ripe_tomatoes.append([i,j]) #익은 토마토의 좌표 저장
    box.append(row) #한 줄씩 박스로 저장

print(bfs_tomato(M,N,box))