<<<<<<< HEAD
n = int(input())
coordinates = []

for _ in range(n) :
    [x,y] = list(map(int, input().split()))
    coordinates.append([y,x])

coordinates.sort()

for i in coordinates:
=======
n = int(input())
coordinates = []

for _ in range(n) :
    [x,y] = list(map(int, input().split()))
    coordinates.append([y,x])

coordinates.sort()

for i in coordinates:
>>>>>>> 88d5abf5fdf1224584809c4f7ffbcfc6b01b5095
    print(i[1],i[0])