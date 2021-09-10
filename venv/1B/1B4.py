def Solution(n, coord):
    return coord[n//2]

def main() :
    n = int(input())
    coord = list(map(int,input().strip().split()))[:n]
    print(Solution(n, coord))


if __name__ == '__main__':
    main()
