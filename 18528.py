import sys
from collections import deque
n= int(sys.stdin.readline())
queue=deque()
for _ in range(n):
    command= str(sys.stdin.readline().rstrip())
    if len(command.split())>1:
        queue.append(command.split()[1])
    elif command == 'pop':
        print(queue.popleft() if queue else -1)
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        print(0 if queue else 1)
    elif command == 'front':
        print(queue[0] if queue else -1)
    elif command == 'back':
        print(queue[-1] if queue else -1)

