def Solution(street):

    shops = [i for i, x in enumerate(street) if x == 2]
    houses = [j for j, x in enumerate(street) if x == 1]
    way_point = []
    for house in houses:
        check = 9
        for shop in shops:
            road = abs(house - shop)
            if road < check:
                check = road
        way_point.append(check)
    return max(way_point)

def main() :
    street = list(map(int,input().strip().split()))[:10]
    print(Solution(street))

if __name__ == '__main__':
    main()