input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    n=len(array)
    for i in range(1,n):
        for j in range(i): 
            if array[i-j-1] > array[i-j]: 
                array[i-j-1], array[i-j] = array[i-j], array[i-j-1]
            else:
                break #array[i-j-1] > array[i-j] 경우는 고려할 필요가 없다. 이미 왼쪽의 숫자들은 정렬이 완료되었기 때문에 앞의 숫자들과도 비교할 필요가 없다.
    return


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!