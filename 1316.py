
n = int(input())
group_word = 0
non_group_word = 0 #반복문을 줄이기 위해 추가한 변수

for _ in range(n):
    non_group_word = 0
    word = str(input())
    if len(word) ==1: #단어가 하나의 알파벳으로 이루어져있다면 그룹문자다.
        group_word +=1
    else:
        for char in set(word): #단어를 구성하는 알파벳 종류 수만큼 반복한다.
            cnt_same_char = word.count(char) #전체 단어에 포함된 해당 알파벳 개수
            char_idx = word.index(char) #해당 알파벳 중 첫번째 알파벳이 위치한 자리

#if문의 의미
# 단어 내 해당 알파벳의 첫 위치부터 해당 알파벳의 총 개수만큼 떨어진 자리까지의 범위에서 해당 알파벳 개수를 센다.
# 그 수가 단어 내에 있어야 할 해당 알파벳의 총 개수와 일치하는 지 확인한다.
# 그 범위에 총 개수가 존재하지 않는다는 것은 떨어져 있다는 의미이므로 그룹문자가 아니다.
            if word[char_idx:char_idx+cnt_same_char].count(char) == cnt_same_char:
                continue
            else:
                non_group_word +=1
                break #단어 내 알파벳 중 그룹문자 조건에 해당하지 않는 것이 있다면 카운트한다.
        if non_group_word == 0: # 그룹문자 조건에 해당하지 않는 알파벳이 0개라면 그룹문자 개수로 카운트한다.
            group_word +=1

print(group_word)







