#############
# Apartment #
#############

# 다른 파일에서 class import 
from Apartment import Apartment
from Vile import Vile

# 파일읽기
f = open("./Apartment.txt", 'r')
N = int(f.readline())

# Apartment정보 객체로 만들어 입력받기
apartments = []
for i in range(N):    
    row=f.readline().split(' ')
    a = Apartment(row[0], int(row[1]), int(row[2].strip())) # 객체 생성
    apartments.append(a)
f.close()


# Q 가장 평수가 큰 아파트를 찾아 "xxx동 xxxx호의 x개의 방이 있는 xx평의 집입니다" 라고 출력
print('Q. 가장 큰 평수 아파트의 정보를 출력하세요.')
print("A.", max(apartments))


# magic method가 작동하는 것을 직관적으로 파악해보기 위해 for문을 이용하여 최댓값을 찾아보세요!
max_index1=0
max_index2=0

for j in range(N-1):
    if apartments[max_index1].size < apartments[j+1].size:
        max_index1 = j+1

    if apartments[max_index2] < apartments[j+1]:
        max_index2 = j+1

print("Max Index 찾기\n1. 객체 속성 비교 :",apartments[max_index1], "\n2. 매직 메소드 :",apartments[max_index2])

# 혹시 같은 인덱스가 있으면 같이 출력한다.
print("같은 인덱스 있는지 확인")
for j in range(N):
    if apartments[j] == apartments[max_index2]:
        print(apartments[j])



###########
## Vile ###
###########

# 파일읽기
f = open("Vile.txt", 'r')
N=int(f.readline())

# Vile정보 객체로 만들어 입력받기
viles = []
for i in range(N):
    row = f.readline().split(' ')
    v = Vile(row[0], int(row[1]), int(row[2].strip()), row[3]) # 객체 생성
    viles.append(v)
f.close()


# Vile에 대한 최대평수 출력은 max를 활용해보세요~!
# Q 가장 평수가 큰 주택을 찾아 "xxxx에 위치해 있는 x개의 방이 있고 마당은 없는 x평의 주택입니다." 라고 출력
print('Q. 가장 큰 평수 주택의 정보를 출력하세요.')
print("A.", max(viles))


