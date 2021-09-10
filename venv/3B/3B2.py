def Solution(nums):
    occured = set()
    for num in nums :
        if num in occured :
            print('YES')
        else :
            print('NO')
            occured.add(num)


def main():
    nums = list(map(int, input().strip().split()))
    Solution(nums)



if __name__ == '__main__':
    main()