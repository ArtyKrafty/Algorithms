def arrsum(nums):
    # функция суммы списка с рекурсией
    sum = 0
    if nums == []:
        return 0
    return nums[0] + arrsum(nums[1:])


if __name__ == '__main__':
    nums = [2, 4, 6]
    print(arrsum(nums))