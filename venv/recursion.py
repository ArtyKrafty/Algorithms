#рекурсия базовый + рекурсивный вызов

def countdown(i):
    print (i)
    if i <= 1:
        return
    else:
        countdown(i-1)

countdown(3)

#рекурсия - факториал
def factorial(n):

    if n == 1:
        return 1
    else:
        return n * factorial ( n - 1 )
# грубое решение без рекурсии
print(factorial(3))
def brut_fact (n):
    res = []
    answer = 1
    while len(res) != n:
        for i in range(1, n+1):
            res.append(i)
    for nums in res:
        answer *= nums
    return answer

print(brut_fact(4))