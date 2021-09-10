def Solution(L, K, legs):

    left = []
    right = []
    mid = L // 2


    for leg in legs :
        if leg <= mid and L % 2 != 0 :
            left.append(leg)
        elif leg > mid and L % 2 != 0 and mid not in legs:
            right.append(leg)
        elif leg <= mid - 1 and L % 2 == 0 :
            left.append(leg)
        elif leg >= mid and L % 2 == 0:
            right.append(leg)


    if len(right) != 0 :
        leg_1 = max(left)
        leg_2 = min(right)
        print(max(left), min(right))
    else :
        print(max(left))

def main() :

    L, K = map(int, input().split())
    legs = list(map(int, input().strip().split()))[:K]
    Solution(L, K, legs)

if __name__ == '__main__' :
    main()

