<<<<<<< HEAD
n = int(input())
dp = []
r, g, b = [int(x) for x in input().split()]
dp.append((r,g,b))
for _ in range(1,n):
    r, g, b = [int(x) for x in input().split()]
    pR, pG, pB = dp[-1] #바로 이전에 저장된 (R,G,B)가 각 변수에 배분됨.
    R = r + min(pG, pB)
    G = g+min(pR,pB)
    B = b+min(pR,pG)
    dp.append((R,G,B))

print(min(dp[-1]))


=======
n = int(input())
dp = []
r, g, b = [int(x) for x in input().split()]
dp.append((r,g,b))
for _ in range(1,n):
    r, g, b = [int(x) for x in input().split()]
    pR, pG, pB = dp[-1] #바로 이전에 저장된 (R,G,B)가 각 변수에 배분됨.
    R = r + min(pG, pB)
    G = g+min(pR,pB)
    B = b+min(pR,pG)
    dp.append((R,G,B))

print(min(dp[-1]))


>>>>>>> 88d5abf5fdf1224584809c4f7ffbcfc6b01b5095
