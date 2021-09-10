
# (x1 - x0) * (y2 - y1) - (x2 - x1) * (y1 - y0)
# (x2 - x0) * (y3 - y2) - (x3 - x2) * (y2 - y0)
# (x3 - x0) * (y1 - y3) - (x1 - x3) * (y3 - y0)

def Solution(d, x, y):

    oa_ab = -1 * (d - 0) * (0 - y)
    ob_bc = (d - x) * d - (-d) * (0 - y)
    oc_ca = (0 - x) * (0 - d)

    if (oa_ab > 0 and ob_bc > 0 and oc_ca > 0) or (oa_ab < 0 and ob_bc < 0 and oc_ca < 0):
        return 0
    elif 0 in [oa_ab, oc_ca, ob_bc]:
        return 0
    if oa_ab < ob_bc and oa_ab <= oc_ca :
        return 1
    elif ob_bc <= oa_ab and ob_bc < oc_ca :
        return 2
    elif oc_ca < oa_ab and oc_ca <= ob_bc :
        return 3


def main() :
    d = int(input())
    x, y = map(int,input().split())
    print(Solution(d, x, y))


if __name__ == '__main__':
    main()
