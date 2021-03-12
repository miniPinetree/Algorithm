n = int(input())
coordinates = []

for _ in range(n) :
    [x,y] = list(map(int, input().split()))
    coordinates.append([y,x])

coordinates.sort()

for i in coordinates:
    print(i[1],i[0])