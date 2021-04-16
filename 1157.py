<<<<<<< HEAD
# 3차 답안
# 시간이 가장 짧은 최종 답안

word = str(input()).upper()

frequency_of_use = []

for char in set(word): #단어 내 중복을 없애고 사용된 알파벳만 추립니다.
    frequency = word.count(char) #해당 알파벳이 단어 안에서 몇 번 쓰였는 지 계산합니다.
    frequency_of_use.append([frequency,char])
frequency_of_use.sort(reverse=True)
if len(frequency_of_use) > 1 and frequency_of_use[0][0] == frequency_of_use[1][0]:
    print('?')
else:
    print(frequency_of_use[0][1])

# ## 2차 답안
# 접근 방식
# 알파벳과 발생횟수를 key:value형태로 저장한 뒤 value값을 기준으로 내림차순 정렬한다.
# 정렬된 배열에서 발생횟수가 동일한 알파벳이 있는 지 확인하여 있다면 물음표를, 없다면 알파벳 대문자를 출력한다.


# word = str(input()).upper()

# count = {}

# for char in word:
#     if char in count:
#         count[char] += 1
#     else :
#         count[char] = 1

# sorted_count = sorted(count.items(), key = lambda x:x[1], reverse =True)


# if len(sorted_count) > 1 :
#     if sorted_count[0][1] == sorted_count[1][1]:
#         print('?')
#     else :
#         print(sorted_count[0][0])
# else :
#         print(sorted_count[0][0])

# else문을 한 번만 적었더니 sorted_count 리스트에 값이 3개 이상일 때 값이 나오지 않는 에러가 발생했다.

# for char in word:
#     print(char)
#     try: count[char]+=1
#     except: count[char]=1

# # 1차 답안
# (보완) 값이 여러 개일때 걸러내는 방식까지 고려했을 때 더 효율적인 방법을 찾고 싶어서 dictionary를 이용해 새로운 방식으로 문제를 다시 풀어보았다.
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

=======
# 3차 답안
# 시간이 가장 짧은 최종 답안

word = str(input()).upper()

frequency_of_use = []

for char in set(word): #단어 내 중복을 없애고 사용된 알파벳만 추립니다.
    frequency = word.count(char) #해당 알파벳이 단어 안에서 몇 번 쓰였는 지 계산합니다.
    frequency_of_use.append([frequency,char])
frequency_of_use.sort(reverse=True)
if len(frequency_of_use) > 1 and frequency_of_use[0][0] == frequency_of_use[1][0]:
    print('?')
else:
    print(frequency_of_use[0][1])

# ## 2차 답안
# 접근 방식
# 알파벳과 발생횟수를 key:value형태로 저장한 뒤 value값을 기준으로 내림차순 정렬한다.
# 정렬된 배열에서 발생횟수가 동일한 알파벳이 있는 지 확인하여 있다면 물음표를, 없다면 알파벳 대문자를 출력한다.


# word = str(input()).upper()

# count = {}

# for char in word:
#     if char in count:
#         count[char] += 1
#     else :
#         count[char] = 1

# sorted_count = sorted(count.items(), key = lambda x:x[1], reverse =True)


# if len(sorted_count) > 1 :
#     if sorted_count[0][1] == sorted_count[1][1]:
#         print('?')
#     else :
#         print(sorted_count[0][0])
# else :
#         print(sorted_count[0][0])

# else문을 한 번만 적었더니 sorted_count 리스트에 값이 3개 이상일 때 값이 나오지 않는 에러가 발생했다.

# for char in word:
#     print(char)
#     try: count[char]+=1
#     except: count[char]=1

# # 1차 답안
# (보완) 값이 여러 개일때 걸러내는 방식까지 고려했을 때 더 효율적인 방법을 찾고 싶어서 dictionary를 이용해 새로운 방식으로 문제를 다시 풀어보았다.
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

>>>>>>> 88d5abf5fdf1224584809c4f7ffbcfc6b01b5095
# find_alphabet_occurrence(word)