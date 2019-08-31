"""
다른 .py에서 작성한 Apartment와 Vile 모듈을 import하는 import문을 작성해주세요
ex ) from a import b
a.py에서 b class import

"""


f = open("Apartment.txt", 'r')
N=int(f.readline())

apartments=[]
for i in range(N):
    """
    apartments 리스트 안에 class append
    
    """
f.close()

# 클래스 리스트 정렬
max_index=0
# magic method가 작동하는 것을 직관적으로 파악해보기 위해 for문을 이용하여 최댓값을 찾아보세요!
for j in range(N-1):
    """
    magic method인 lt함수 활용
    최대 평수를 가진 Apartment 클래스 찾기 
    """

# 혹시 같은 인덱스가 있으면 같이 출력한다.
print(apartments[max_index])
for j in range(N):
    """"
    class magic method인 eq함수 활용
    """

# Vile에 대한 최대평수 출력은 max를 활용해보세요~!
