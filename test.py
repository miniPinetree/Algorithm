# 자료 입력
C = int(input())
ans = []

for _ in range(C) :
    num_list = list(map(int, input().split()))
    avg = sum(num_list[1:])/num_list[0]
    cnt = 0
    for score in num_list[1:]:
        if score > avg:
            cnt +=1
    rate = cnt/num_list[0]*100
    ans.append(rate)

for rate in ans :
    print(format(rate,'.3f')+'%')


