class Solution:
    def binary_search (self, nums: list ,  target: int) -> int:
        nums = sorted(nums)
        guess = 0
        low = 0
        high = len ( nums ) - 1
        while low <= high :
            mid = int(((low + high) / 2))
            guess = nums [ mid ]
            if guess == target :
                return nums [ mid ]
            elif guess > target :
                high = mid - 1
            else :
                low = mid + 1
        return None


if __name__ == '__main__':

    nums = [ 1 , 3 , 5 , 7 , 0 ]
    target = 9
    print ( Solution().binary_search ( nums , target ) )

