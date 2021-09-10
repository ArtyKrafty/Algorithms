def Solution(list_1, list_2):
    return(len(set(list_1) & set(list_2)))

def main():
    list_1 = list(map(int, input().strip().split()))
    list_2 = list(map(int, input().strip().split()))
    print(Solution(list_1, list_2))



if __name__ == '__main__':
    main()