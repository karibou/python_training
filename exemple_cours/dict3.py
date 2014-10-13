d1 = {
        ('paris', 'population'): 2500000,
        ('paris', 'coordoonnees'): (48.51, 2.21),
        ('paris', 'superficie'): 86.9,
        ('paris', 'arrondissements'): 20,
        ('besancon', 'population'): 120000,
        ('besancon', 'coordonnes'): (47.14, 6.01),
        ('besancon', 'superficie'): 65,
        }

d2 = {}

#for k, v in d1.iteritems():
for (ville, propriete), v in d1.iteritems():
    #ville = k[0]
    #propriete = k[1]
 #   vald2 = d2.get(ville)
 #   if vald2 is None:
 #       d2[ville] = {}
 #       vald2 = d2.get(ville)
    vald2 = d2.setdefault(ville, {})
    #d2.setdefault(ville, {})[propriete] = v
    vald2[propriete] = v


print d2


correction = {
        'paris': {'population': 2500000,
            'coordonnes': (48.51, 2.21),
            'superficie': 86.9,
            'arrondissements': 20,
            },
        'besancon': {'population': 120000,
            'coordonnes': (47.14, 6.01),
            'superficie': 65,
            },
        }


#assert correction.) == correction, 'pas bon %s' % d2
