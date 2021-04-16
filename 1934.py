<<<<<<< HEAD

def gcd(a,b):
    r = a%b
    while r:
        a = b
        b = r
        r = a%b
    return b

t = int(input())
rst = []
for _ in range(t):
    a, b = map(int,input().split())
    rst.append(a*b//gcd(a,b))

for r in rst:
    print(r)




=======

def gcd(a,b):
    r = a%b
    while r:
        a = b
        b = r
        r = a%b
    return b

t = int(input())
rst = []
for _ in range(t):
    a, b = map(int,input().split())
    rst.append(a*b//gcd(a,b))

for r in rst:
    print(r)




>>>>>>> 88d5abf5fdf1224584809c4f7ffbcfc6b01b5095
