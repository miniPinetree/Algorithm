<<<<<<< HEAD
# 예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다. 따라서, 다음과 같이 크로아티아 알파벳을 변경해서 입력했다.

# 크로아티아 알파벳	변경
# č	c=
# ć	c-
# dž	dz=
# đ	d-
# lj	lj
# nj	nj
# š	s=
# ž	z=
# 예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다. 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

# dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. lj와 nj도 마찬가지이다. 위 목록에 없는 알파벳은 한 글자씩 센다.

#접근방식
#크로아티아 알파벳을 배열에 저장한 뒤 for문을 돌려 입력 값 내 포함여부를 확인하였다.
# replace()를 이용하여 크로아티아 알파벳이 포함되어 있으면 임의의 알파벳인 a로 변경해주었다.
# 문제에서 요구하는 출력값은 알파벳의 개수이므로 치환하는 값 자체에 담긴 의미는 없다.
# 2~3개의 문자로 이루어진 크로아티아 알파벳이 모두 치환되면 전체 문자열의 길이를 출력한다.

#문제풀이

word = str(input())
c_alphabet = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for c in c_alphabet:
    word = word.replace(c,'a')
print(len(word))

=======
# 예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다. 따라서, 다음과 같이 크로아티아 알파벳을 변경해서 입력했다.

# 크로아티아 알파벳	변경
# č	c=
# ć	c-
# dž	dz=
# đ	d-
# lj	lj
# nj	nj
# š	s=
# ž	z=
# 예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다. 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

# dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. lj와 nj도 마찬가지이다. 위 목록에 없는 알파벳은 한 글자씩 센다.

#접근방식
#크로아티아 알파벳을 배열에 저장한 뒤 for문을 돌려 입력 값 내 포함여부를 확인하였다.
# replace()를 이용하여 크로아티아 알파벳이 포함되어 있으면 임의의 알파벳인 a로 변경해주었다.
# 문제에서 요구하는 출력값은 알파벳의 개수이므로 치환하는 값 자체에 담긴 의미는 없다.
# 2~3개의 문자로 이루어진 크로아티아 알파벳이 모두 치환되면 전체 문자열의 길이를 출력한다.

#문제풀이

word = str(input())
c_alphabet = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for c in c_alphabet:
    word = word.replace(c,'a')
print(len(word))

>>>>>>> 88d5abf5fdf1224584809c4f7ffbcfc6b01b5095
