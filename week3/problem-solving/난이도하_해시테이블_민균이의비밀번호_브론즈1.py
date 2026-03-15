# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933

# 홀수 길이 / 2 <= length <= 100 / lower / 2 < word < 14
# 비밀번호가 목록에 있으면 뒤집은 문자열도 포함
# 비밀번호의 길이 + 가운데 글자를 출력

length = int(input())
word = []
rword = []
idx = 0
# Condition

if 2 <= length and length <= 100:
    for _ in range(length):
        inword = input()
        if inword.isalpha() and len(inword) % 2 == 1 and 2 < len(inword) and len(inword) < 14:
            word.append(inword)
    
for i in range(len(word)):
    if word[i][::-1] in word and len(word) == length:
        idx = int(len(word[i])/2)
        print(len(word[i]) , word[i][idx:idx+1])
        break