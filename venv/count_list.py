
def countlist(nums):
# функция подсчета списка с рекурсией
    if nums == []:
        return 0
    return 1 + countlist(nums[1:])


if __name__ == '__main__':
    nums = [2, 4, 6]
    print(countlist(nums))