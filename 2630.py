import sys
r=sys.stdin.readline

n = int(r())
paper = [list(map(int,r().split())) for _ in range(n)]
cnt_white=0
cnt_blue=0
def divide(x,y,n):
    global cnt_white,cnt_blue
    color_check = paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color_check != paper[i][j]:
                divide(x,y,n//2) #좌측 상단부터 시계방향으로 진행
                divide(x,y+n//2,n//2)
                divide(x+n//2,y,n//2)
                divide(x+n//2,y+n//2,n//2)
                return
    if color_check==0: 
        cnt_white += 1
    else:
        cnt_blue+=1

divide(0,0,n)
print(cnt_white)
print(cnt_blue)
    
