with open("input.txt", "r") as doc :
    n = int(doc.readline())
    all_nums = set(range(1, n + 1))
    temp = set()

    for line in doc :
        if "YES" in line :
            all_nums &= temp
        elif "NO" in line :
            all_nums -= temp
        elif "HELP" not in line :
            temp = set(map(int, line.split()))

print(' '.join(map(str, sorted(all_nums))))
