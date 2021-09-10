def Solution():
    max_ele = 0
    max_cnt = 0
    ele = -1

    while ele != 0:
        ele = int(input())
        if ele > max_ele:
            max_ele, max_cnt = ele, 1
        elif ele == max_ele:
            max_cnt += 1
    return max_cnt


def main() :
    print(Solution())

if __name__ == '__main__':
    main()