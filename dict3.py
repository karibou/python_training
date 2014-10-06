#!/usr/bin/python

d1 = {('paris', 'population'): 2500000,
      ('paris', 'coordoonnees'): (48.51, 2.21),
      ('paris', 'superficie'): 86.9,
      ('paris', 'arrondissements'): 20,
      ('besancon', 'population'): 120000,
      ('besancon', 'coordonnes'): (47.14, 6.01),
      ('besancon', 'superficie'): 65,
}

d2 = {}

for k, v in d1.iteritems():
	d2[k[0]] = {}
	vald2 = d2.get(k[0])
	if vald2 is None:
		d2[k[0]] = {}
		vald2 = d2.get(k[0])
	vald2[k[1]] = v
#
# ou encore
#for (ville, propriete), v in d1.iteritems():
#	d2.setdefault(ville, {})[propriete] = v
# ou
#for (ville, propriete), v in d1.iteritems():
#vald2 = d2.setdefault(ville, {})
#vald2[propriete]=v
