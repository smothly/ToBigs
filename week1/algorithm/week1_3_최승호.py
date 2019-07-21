# coding: utf-8

# 파일 input 받기
f = open('phone_book.txt', mode='r', encoding='utf-8')
phone_number_list = [p.strip() for p in f.readlines()]
f.close()


# 조건 걸러내기
real_number = list()

for phone_number in phone_number_list:
    split_number = phone_number.split('-')
    # 첫번째 조건
    if int(split_number[1]) > int(split_number[2]):
        # 두번째조건
        if split_number[0] == '010':
            real_number.append(phone_number)
        
print(real_number)

# 파일 저장
f = open('new_phone_book.txt', mode='w', encoding='utf-8')
for number in real_number:
    f.write(number + '\n')
f.close()

