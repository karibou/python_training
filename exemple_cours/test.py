"documentation de mon module"

var = 45

def toto(a, b, c):
    """documentation de ma fonction
    """
    global var
    if True:
        var = 43
    return None

print 'resultat toto', toto(4, 5 ,6)
print 'help de toto', help(toto)
