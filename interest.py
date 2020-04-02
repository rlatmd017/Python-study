
# 16% 10년 10,000,000,000원 (10억원)

money = 1000
rate = 0.0075

count = 1

for x in range(1, 11):

    money = money + (money * rate)

    print(x, money)
