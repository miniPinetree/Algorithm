n = int(input())
s_num = []
for _ in range(n):
    s= int(input())
    s_num_list.append(s)

dp=[s_num_list[-1]] #반드시 밟아야하는 도착계단에서부터 계산한다.
idx = -1 # 시작점을 맨 뒤에 위치한 도착계단으로 설정한다.

while idx-3>= -len(s_num):
    opt1 = s_num[idx-1]+s_num[idx-3]
    opt2 = s_num[idx-2]
    if opt1>=opt2:
        idx -=3
        dp.append(dp[-1]+opt1)
    else opt1<opt2:
        idx-=2
        dp.append(dp[-1]+opt2)
if 
#앞 계단이 3개 미만으로 남았을때는 인덱스 오류가 날텐데 어쩌지?

