from random import randrange
nums = []

# loop를 nums 가 6개가 되는 동안

while len(nums) < 6:
    num = randrange(1, 46)

    # 중복된 값이 뽑힌다면 다시 뽑는다
    if num in nums:
        continue

    nums.append(num)

print(nums)

# 1 ~ 45 사이의 숫자를 뽑고 nums에 보관


