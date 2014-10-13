"""Compute the greatest common denominator of two numbers"""

def pgcd1(a, b):
    """Iterative version of the GCD"""
    if a > b:           # we need a>=b (so we swap them if needed)
        a, b = b, a
    while 1:            # infinite loop
        r = b % a
        if r == 0:      # eventually this will be true
            return a    # and we'll exit from the loop
        else:
            b, a = a, r # prepare for the next iteration

    return a


def pgcd2(a, b):
    """Recursive version of the GCD"""
    if a > b:
        a, b = b, a
    if a == 0:
        return b
    else:
        return pgcd2(a, b%a)


def pgcd3(a, b):
    """More compact recursive: modulo will swap the arguments for us the first
    time
    """
    if a==0:
        return b
    else:
        return pgcd3(a,b%a)

def pgcd4(a,b):
    """Even more compact iterative"""
    while a: # loop until a==0
        b, a = a, b % a
    return b


pgcd = pgcd4


if __name__ == "__main__":
    while True:
        nbres = raw_input('Enter two numbers with a space in between: ')
        if nbres:
            try:
                a, b = nbres.split()
                a = int(a)
                b = int(b)
            except:
                print "Your entry is incorrect"
                continue
            c = pgcd(a, b)
            print "gcd :",c
        else:
            print 'Bye...'
            break
