
# coding: utf-8

# 암호 해독하기

# input 받기 P와 C는 password dict에 저장
N = int(input())
password = dict()
for i in range(N):
    key_value = input().split(' ')
    password[key_value[1]] = key_value[0]

input_string = input()


# input_string 스플릿 하여 리스트 형태로 저장
input_string = input_string.split()

# password 활용하여 한칸씩 땡겨줄 단어 리스트 만들기
new_string = list()
for word in input_string:
    new_string.append(password[word])


# 알파벳을 한칸씩 앞으로하여 저장하기
result = list()

for word in new_string:
    P = list()
    for char in word:
        if char == "a":
            P.append('z')
        else:
            P.append(chr(ord(char) - 1))            
    result.append(''.join(P))


# 리스트를 스트링으로 출력
print(' '.join(result))

