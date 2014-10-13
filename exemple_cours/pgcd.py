
def pgcd(a, b):
    if b < a:
        a, b = b, a
    r = b%a
    if r == 0:
        return a
    else:
        return pgcd(r, b)


assert pgcd(6, 42) == 6
assert pgcd(18, 42) == 6
assert pgcd(42, 18) == 6
