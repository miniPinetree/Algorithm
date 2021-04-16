#문장 내 최빈값 알파벳 찾기
#  
input = "hello my name is sparta"

def find_alphabet_occurrence_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for char in string :
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    max_occurrence = 0
    max_alphabet_index = 0
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurence = alphabet_occurrence_array[index]
        
        if alphabet_occurence > max_occurrence:
            max_occurrence = alphabet_occurence
            max_alphabet_index = index
    
    return chr(max_alphabet_index + ord('a'))

result = find_alphabet_occurrence_alphabet(input)
print(result)