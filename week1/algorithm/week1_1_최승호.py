
# coding: utf-8

# 9를 가지고 있는 n번째 숫자 제곱하

# 입력받아 리스트형태로 저장하기
N = int(input())
num_string = input()
num_list = num_string.split(' ')


# 9가 아닌 리스트 새로 생성
not_9_list = [int(num) for num in num_list if '9' not in num]


# 잘못된 입력값일 경우 처리 (1 9가 없는 숫자가 없는 경우, 2. N번째 숫자가 없는 경우)
if len(not_9_list) == 0 or len(not_9_list) < N:
    print(999999999)
else:
    print(not_9_list[N-1] * not_9_list[N-1])

