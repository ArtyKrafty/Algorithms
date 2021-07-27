
def NOD (a, b):
    if a == 0 or b == 0 :
        return max ( a , b )
    else:
        if a > b :
            return NOD ( (a - b) , b )
        else :
            return NOD ( a , (b - a) )




if __name__ == '__main__':

    a = 1071
    b = 462
    print(NOD(a, b))
