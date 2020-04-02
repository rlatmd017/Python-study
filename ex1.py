from random import randrange
nums = []

def checkDupl(num_list, target):

    result = False

    for x in num_list:
        if x == target:
            result = True
            break

    return result


while len(nums) < 6:
    num = randrange(1, 46)

    if checkDupl(nums, num) == True:
        continue

    nums.append(num)

print(nums)