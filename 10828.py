<<<<<<< HEAD
import sys
n= int(sys.stdin.readline())
stack=[]
for _ in range(n):
    command= str(sys.stdin.readline().rstrip())
    if len(command.split())>1:
        stack.append(command.split()[1])
    elif command == 'pop':
        print(stack.pop() if stack else -1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        print(0 if stack else 1)
    elif command == 'top':
        print(stack[-1] if stack else -1)
        
=======
import sys
n= int(sys.stdin.readline())
stack=[]
for _ in range(n):
    command= str(sys.stdin.readline().rstrip())
    if len(command.split())>1:
        stack.append(command.split()[1])
    elif command == 'pop':
        print(stack.pop() if stack else -1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        print(0 if stack else 1)
    elif command == 'top':
        print(stack[-1] if stack else -1)
        
>>>>>>> 88d5abf5fdf1224584809c4f7ffbcfc6b01b5095
