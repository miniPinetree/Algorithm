import sys
from collections import deque

n, m = (sys.stdin.readline().split())
target_list = list(map(int, sys.stdin.readline().split()))
queue = deque([i+1 for i in range(int(n))])

#왼쪽으로 이동 : 맨 앞에 있던 요소는 맨 오른쪽으로 가게된다.
def moving_left(): 
    moving_queue = queue[0] 
    del queue[0]
    queue.append(moving_queue)

def moving_right():
    moving_queue = queue[-1]
    del queue[-1]
    queue.insert(0, moving_queue)

count = 0
for target_num in target_list:
    #target_num의 위치가 전체 배열의 중간점을 기준으로 왼쪽에 위치하는 지, 오른쪽에 위치하는 지에 따라
    #왼쪽으로 이동할 때 유리한 지, 오른쪽으로 이동할 때 유리한 지 판단한다.
    if queue.index(target_num) <= len(queue) //2:
        moving_left() #삭제기능도 왼쪽 이동을 하게 되므로 if문밖에 존재함.
        if queue[0] != target_num:
            count+=1
        else:
            del queue[0]
            break
    else: #오른쪽 이동이 유리한 경우
        if queue[0] != target_num:
            moving_right()
            count +=1
        else:
            del queue[0]
            break

print(count)


