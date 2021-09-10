def Solution(nums) :
    n = int(input())
    nums = set(range(1, n + 1))
    possible_nums = nums
    while True :
        guess = input()
        if guess == 'HELP' :
            break
        guess = {int(x) for x in guess.split()}
        answer = input()
        if answer == 'YES' :
            possible_nums &= guess
        else :
            possible_nums &= nums - guess

    print(' '.join([str(x) for x in sorted(possible_nums)]))


def main() :
    Solution(nums)


if __name__ == '__main__' :
    main()
