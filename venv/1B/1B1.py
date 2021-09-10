def Solution(r, i, c):

    if r != 0 and i == 0 :
        return 3
    elif r == 0 and i == 0:
        return c
    elif r !=0 and i == 4:
        return 3
    elif r == 0 and i == 4:
        return 4
    elif i == 6:
        return 0
    elif i == 1:
        return c
    elif i == 7:
        return 1
    else:
        return i

def main() :
    r = int(input())
    i = int(input())
    c = int(input())
    print(Solution(r, i, c))

if __name__ == '__main__':
    main()