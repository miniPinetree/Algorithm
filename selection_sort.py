input = [4, 6, 2, 9, 1]


def selection_sort(array):
    n=len(array)
    for i in range(n-1):
        min_index = i
        for j in range(n-i): #반복횟수는 최소값을 골라낸 횟수인 i를 제외한 횟수만큼만 반복하면 된다.
            if array[i+j] < array[min_index]: #i번째 index에는 최소값이 들어가있을 것이므로 비교를 생략한다.
                min_index = i+j
        array[i], array[min_index] = array[min_index], array[i]


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!