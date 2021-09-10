def Solution(nums) :
    for i in range(len(nums)) :
        for j in range(len(nums)) :
            if i != j and nums[i] == nums[j] :
                break
        else :
            print(nums[i], end = ' ')


def main() :
    nums = [int(x) for x in input().split()]
    Solution(nums)


if __name__ == '__main__' :
    main()
