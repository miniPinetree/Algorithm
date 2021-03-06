# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

M,N= map(int, input().split())
p_num = [2,3,5,7]
ans = []

for n in range(1, N):
    print(n)
    if 6*n+1 > N:
        break
    else:
        ans.append(6*n-1)
        ans.append(6*n+1)
for i in ans:
    # print(i)
    for j in p_num:
        # print(j)
        if i%j == 0:
            ans.remove(i)
# print(ans)

# for num in p_num:
#     if num >= M:
#         print(num)
# for ans in ans:
#     if ans <= N:
#         print(ans)


