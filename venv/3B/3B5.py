def Solution(witness, susp) :
    temp = set()


    for i in range(len(witness)) :
        if witness[i].isalpha() and len(set(witness[i])) <= 5:
            temp |= set(witness[i])
        elif witness[i].isnumeric() and len(set(witness[i])) <= 5:
            temp |= set(witness[i])
        elif witness[i].isalnum() and not witness[i].isalpha() and len(set(witness[i])) <= 5:
            temp |= set(witness[i])



    min_set = [len(set(susp[i]) & temp) for i in range(len(susp))]

    for i in range(len(min_set)):
        if min_set[i] == max(min_set):
            print(susp[i])



def main() :
    m = int(input())
    witness = [input() for _ in range(m)]
    n = int(input())
    susp = [input() for _ in range(n)]
    Solution(witness, susp)


if __name__ == '__main__' :
    main()
