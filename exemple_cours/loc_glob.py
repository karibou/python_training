VARIABLE_GLOBALE = 1
def fonction(a, b):
    print 'globals', globals().keys()
    print 'locals', locals()
    globals()['identifiant'] = 4

fonction(2, 3)
def function2():
    print locals()
function2()

print identifiant
