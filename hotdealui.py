from webcatch import getData

answer = input("핫딜 크롤링을 시작할까요? (실행취소 : n) : ")

if answer == 'n':
    exit()

result = getData()

for str in result:
    print(str)