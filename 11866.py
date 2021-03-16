import sys
from collections import deque

r=sys.stdin.readline

n,k = map(int,r().split())
queue = deque(i for i in range(1,n+1))
rst = []
while queue:
    queue.rotate(-(k-1))
    rst.append(queue.popleft())

print('<', end='')
print(*rst, end='', sep=', ')
print('>')
