

## 접근 방식
# 알파벳과 발생횟수를 key:value형태로 저장한 뒤 value값을 기준으로 내림차순 정렬한다.
# 정렬된 배열에서 발생횟수가 동일한 알파벳이 있는 지 확인하여 있다면 물음표를, 없다면 알파벳 대문자를 출력한다.


word = str(input()).upper()

count = {}

for char in word:
    if char in count:
        count[char] += 1
    else :
        count[char] = 1

sorted_count = sorted(count.items(), key = lambda x:x[1], reverse =True)
#Tuple 형태여서 value로 가져올 수 없으므로 인덱스를 주어 발생횟수를 가져온다.

if len(sorted_count) > 1 :
    if sorted_count[0][1] == sorted_count[1][1]:
        print('?')
    else :
        print(sorted_count[0][0])
else :
        print(sorted_count[0][0])

# else문을 한 번만 적었더니 sorted_count 리스트에 값이 3개 이상일 때 값이 나오지 않는 에러가 발생했다.

# for char in word:
#     print(char)
#     try: count[char]+=1
#     except: count[char]=1

# # 처음에 풀었던 답안 
# - 값이 여러 개일때 걸러내는 방식까지 고려했을 때 더 효율적인 방법을 찾고 싶어서 dictionary를 이용해 새로운 방식으로 문제를 다시 풀어보았다.
# word = str(input()).upper()

# def find_alphabet_occurrence(word):
#     alphabet_occurrence_array = [0]*26

#     for char in word:
#         arr_index = ord(char)-ord('A')
#         alphabet_occurrence_array[arr_index] += 1
    
#     max_occurrence = 0
#     max_alphabet_index = 0
#     for index in range(len(alphabet_occurrence_array)):
#         print(alphabet_occurrence_array.count(index))
#         alphabet_occurrence = alphabet_occurrence_array[index]

#         if alphabet_occurrence > max_occurrence:
#             max_occurrence = alphabet_occurrence
#             max_alphabet_index = index

#             # print(chr(max_alphabet_index+ord('A')))

# find_alphabet_occurrence(word)