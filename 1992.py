import sys
r =sys.stdin.readline

n=int(r())
video = [list(map(int,r().strip())) for _ in range(n)]

def divide(x,y,n):
    check = video[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check != video[i][j]:
                print('(', end='')
                divide(x,y,n//2)
                divide(x,y+n//2,n//2)
                divide(x+n//2,y,n//2)
                divide(x+n//2,y+n//2,n//2)
                print(')',end='')
                return
    if check==0:
        print(0,end='')
    else:
        print(1,end='')

divide(0,0,n)
print(video)