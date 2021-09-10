def Solution(diploma):
    diploma.remove(max(diploma))
    return sum(diploma)


def main() :
    files = int(input())
    diploma = list(map(int, input().strip().split()))[:files]
    print(Solution(diploma))

if __name__ == '__main__':
    main()