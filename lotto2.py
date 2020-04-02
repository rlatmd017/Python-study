from random import randrange

lotto_balls = [x for x in range(1, 46)]
result = []

for x in range(6):
    extract_ball = randrange(1, 46)
    result.append(lotto_balls[extract_ball])
    del extract_ball
print(result)