#두 집합을 합쳐가면서 정렬하는 방법
# 배열의 앞부분과 뒷부분의 두 그룹으로 나누어 각각 정렬한 후 
# 병합하는 작업을 반복하는 알고리즘입니다.


array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]

def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_array = array[:mid]
    right_array = array[mid:]
    return merge(merge_sort(left_array), merge_sort(right_array))

def merge(array1, array2):
    result = []
    array1_index = 0
    array2_index = 0
    while array1_index <len(array1) and array2_index<len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index +=1
        else:
            result.append(array2[array2_index])
            array2_index +=1
    if array1_index == len(array1):
        while array2_index < len(array2):
            result.append(array2[array2_index])
            array2_index+=1

    if array2_index == len(array2):
        while array1_index < len(array1):
            result.append(array1[array1_index])
            array1_index +=1

    return result

print(merge_sort(array_a))
# print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!