def maxnum(nums):
    if nums == [] :
        return
    elif len(nums) == 2:
        return nums[0] if nums [0] > nums [1] else nums[1]
    sub_max = maxnum(nums[1:])
    return nums[0] if nums [0] > sub_max else sub_max



if __name__ == '__main__':
    nums = [1,10,2,5]
    print(maxnum(nums))