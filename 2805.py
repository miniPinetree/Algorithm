
n,m = list(map(int, input().split()))
wood_h = list(map(int, input().split()))
low, high = 1, max(wood_h)

while low<= high:
    mid = (low+high)//2
    # 벌목된 나무의 합계들을 더한다.
    sum = 0 
    for i in wood_h:
        if (i-mid)>0:
            sum += (i-mid)

    if sum >= m:
        low = mid+1
    else:
        high = mid-1
print(high)
