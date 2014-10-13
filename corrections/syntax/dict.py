# -*- coding: utf-8 -*-
"""Dictionary manipulation"""


########################################
# build a dictionary with name as key and age as value from the lists below.
####################

names = ['arthur', 'babar', 'celeste']
ages = [5, 25, 27]

# solution 1, using loop

age_by_name = {}
for prenom, age in zip(names, ages):
    age_by_name[prenom] = age

print("age_by_name:", age_by_name)

# solution 2, using dict comprehension

age_by_name_2 = {name:ages[i] for i, name in enumerate(names)}

assert age_by_name_2 == age_by_name

# solution 3, using dict constructor

age_by_name_3 = dict(zip(names, ages))

assert age_by_name_3 == age_by_name



########################################
# write a function to inverse a dictionary: key become value, supposing values
# are unique.
####################

def revert_dictionary(adict):
    result = {}
    for key, value in adict.items():
        key, value = value, key
        result[key] = value
    return result

print("reversed dict:", revert_dictionary(age_by_name))

def revert_dictionary2(adict):
    return dict((v, k) for k, v in adict.items())

assert(revert_dictionary(age_by_name) == revert_dictionary2(age_by_name))


def revert_dictionary3(adict):
    return {v: k for k, v in adict.items()}

assert(revert_dictionary(age_by_name) == revert_dictionary3(age_by_name))



########################################
# get dictionary below from d1.
#
# d2 = {'paris': {'population': 2500000,
#                 'coordonnes': (48.51, 2.21),
#                 'superficie': 86.9,
#                 'arrondissements': 20,
#                 },
#       'besancon': {'population': 120000,
#                    'coordonnes': (47.14, 6.01),
#                    'superficie': 65,
#                    },
# }
####################

d1 = {('paris', 'population'): 2500000,
      ('paris', 'coordoonnees'): (48.51, 2.21),
      ('paris', 'superficie'): 86.9,
      ('paris', 'arrondissements'): 20,
      ('besancon', 'population'): 120000,
      ('besancon', 'coordonnes'): (47.14, 6.01),
      ('besancon', 'superficie'): 65,
}


# Solution 1
d2 = {}
for (city, information), value in d1.items():
    # create city dictionary if it doesn't exist
    if city not in d2:
        d2[city] = {}
    city_dict = d2[city]
    city_dict[information] = value


from pprint import pprint # pretty print
print("d2:")
pprint(d2)

# Solution 2, using setdefault
d2_2 = {}
for (city, information), value in d1.items():
    city_dict = d2_2.setdefault(city, {})
    city_dict[information] = value

assert d2_2 == d2

# Solution 3, without intermediary dict
d2_3 = {}
for (city, information), value in d1.items():
    d2_3.setdefault(city, {})[information] = value

assert d2_3 == d2

#Solution 4: dict comprehension (Python 2.7 only)
d2_4 = {}
for ville in set([city for (city, information) in d1.keys()]):
    d2_4[ville] = {information: value for (city, information), value in d1.items()
                                      if city == ville}
