0:[-1,0,1]
1:[0,1,2]
2:[1,2,3]
3:[2,3,4]
4:[3,4,5]

(0 1 2 3)
 >1 >1 >1

(1 2 3 4 5)
 >1>2>>1>도착

y지점에 도착하기 바로 직전의 이동거리는 반드시 1광년으로 하려 한다.

t = int(input())
for _ in range(t):
    x,y = list(map(int,input().split()))