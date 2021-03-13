
# 접근방식
# 부분수열은 하나의 원소로도 성립 가능하며 다른 원소와의 조합으로 이루어진다.
# 단, 이 문제에서 요구하는 것은 '증가하는 부분수열'이므로 어떤 수 a보다 큰 수가 나왔을 떄 성립 가능하다.
# 동적 계획법을 적용하여 원소별 발생 가능한 '증가하는 부분수열'의 개수를 저장하고
# 기존 원소보다 큰 수가 나오는 경우에 부분수열 발생 가능 경우의 수를 늘려줄 것이다.

def longest_common_subsequence(n):
#배열의 길이만큼 반복한다.
    for i in range(n):
        #i 이전에 나온 수들과 i번째 수를 비교한다.
        for j in range(i):
            if num_list[i] > num_list[j]:
                subsequence[i] = max(subsequence[i],subsequence[j]+1)
                # i이전에 위치한 숫자보다 i번째 수가 크다면 '증가하는 부분수열' 발생 경우의 수가 하나 더 늘어나는 것이다.
    return subsequence

n = int(input())
num_list = list(map(int,input().split()))
# 입력 값과 같은 길이로 1로 이루어진 배열을 생성한다.
# 부분 수열은 하나의 원소로도 성립되므로 모든 원소가 공통적으로 최소 1의 값을 가지기 때문이다.
subsequence = [1 for i in range(n)]

print(max(longest_common_subsequence(n)))
# 원소별 증가하는 부분수열의 개수가 저장된 배열 내에서 가장 큰 수를 출력한다.