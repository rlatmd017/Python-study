import math

# 1. 영화 데이터 정의
movie_sample = [
    (10,50,'A'),
    (20,40,'A'),
    (30,40,'A'),
    (50,40,'A'),
    (20,15,'M'),
    (30,15,'M'),
    (40,10,'M'),
    (50,0,'M')
]
#2. 비교할 영화 변수 입력장치 설정

count_kiss = int(input("키스씬 숫자를 입력하세요 : "))
count_action = int(input("액션씬 숫자를 입력하세요 : "))
target = (count_kiss, count_action)

def calcDistance(point1, point2):
    result = math.sqrt(math.pow(point1[0]-point2[0], 2)+ math.pow(point1[1]-point2[1], 2))
    return result

movie_sample.sort(key= lambda x: calcDistance(x, target))

print('target과 가장 가까운 영화 3개 : ', movie_sample[0:3])

stack_A = 0
stack_M = 0

for x in range(3):
    if movie_sample[x][2] == 'A':
        stack_A = stack_A +1
    else:
        stack_M = stack_M +1

#if movie_sample[1][2] == 'A':
    #stack_A = stack_A +1
#else:
    #stack_M = stack_M +1

#if movie_sample[2][2] == 'A':
    #stack_A = stack_A +1
#else:
    #stack_M = stack_M +1

if stack_A > stack_M:
    print('target은 Action Movie 입니다!')
else:
    print('target은 Mellow Movie 입니다!')
