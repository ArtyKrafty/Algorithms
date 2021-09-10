def Solution(x, y , z):
    return 0 if x <= 12 and y <= 12 and x!=y else 1

def main() :
    x, y , z = map(int, input().split())
    print(Solution(x, y , z))

if __name__ == '__main__':
    main()
