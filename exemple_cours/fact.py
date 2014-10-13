def fact(n):
    if n == 0:
        return 1
    else:
        res = 1
        for i in range(1,n+1):
            res = res * i
        return res


assert fact(3) == 6, fact(3)
