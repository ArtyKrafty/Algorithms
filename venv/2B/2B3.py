
def Solution(word):

    inverse_word = word[::-1]
    cnt = 0
    for i in range(len(word)//2):
        if word[i] != inverse_word[i]:
            cnt += 1
    return cnt

def main() :

    word = input().strip()
    print(Solution(word))

if __name__ == '__main__' :
    main()
