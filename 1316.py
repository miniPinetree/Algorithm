import sys
r=sys.stdin.readline

n=int(r())
cnt=0

for _ in range(n):
    word = str(r().strip())
    char=word[0]
    g_word = True

    while g_word==True:
        start=word.index(char)
        end=word.index(char)+word.count(char)
        if word.count(char) != word[start:end].count(char):
            g_word = False
        if end >= len(word):
            break
        else: char = word[end]
    if g_word==True:
        cnt+=1

print(cnt)