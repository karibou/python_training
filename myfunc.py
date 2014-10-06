#-*-coding: utf-8-*-

def pgcd(a, b):
    r = b % a
    if r == 0:
        return a
    else:
        return pgcd(r, b)


print pgcd(18, 42)
