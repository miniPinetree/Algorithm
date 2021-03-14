### 접근방식

test_case = []

while True:
    n = int(input())
    if n == 0:
        break
    test_case.append(n)

def is_prime(N):
    array = [True for i in range(N+1)]

    for i in range(2,int(N**0.5)+1): #1은 소수가 아니므로 2부터 N의 제곱근까지를 범위로 한다.
    #제곱근을 대칭으로 쌍을 이루어 N의 약수가 되므로 한쪽만 계산해도 배수들이 제외된다.
        if array[i] == True: #제거되지 않은 숫자인가를 판별함.
            j = 2 #j는 제거되지 않은 가장 작은 수를 의미함.
            while i*j <= N:
                array[i*j] = False #j의 배수라면 소수가 아니기때문에 제거한다.
                j+=1 #i*j가 N을 초과할 때까지 j를 늘려가며 곱하고 그 값은 배수이므로 제거한다.
                #초과하면 for문으로 돌아가 i를 증가시키고 다시 2부터 곱한다.
    return array

prime_list = is_prime(2*max(test_case))

for n in test_case:
    num_of_prime = 0
    for i in range(n+1,2*n+1): #입력값 범위 내에서만 출력되도록 지정
        if prime_list[i] and i!=1: #1은 소수가 아니므로 제외해주는 조건
            num_of_prime +=1
    print(num_of_prime)

