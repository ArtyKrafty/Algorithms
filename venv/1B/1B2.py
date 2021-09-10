def Solution(N, i, j):
    return min((j - i) % N, ((i - j) % N)) - 1

def main() :
    N, i , j = map(int, input().split())
    print(Solution(N, i, j))

if __name__ == '__main__':
    main()