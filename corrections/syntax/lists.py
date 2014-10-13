# -*- coding: utf-8 -*-
"""Basic list manipulations"""

########################################
# list indexing
####################

semaine = ['lun', 'mar', 'mer', 'jeu', 'ven', 'sam', 'dim']

jours_semaine = semaine[:5]
assert jours_semaine == ['lun', 'mar', 'mer', 'jeu', 'ven']
jours_we = semaine[5:]
assert jours_we == ['sam', 'dim']
assert jours_we == semaine[-2:]

hiver = ['jan', 'fev', 'mar']
printemps = ['avr', 'mai', 'jui']
ete = ['juil', 'aou', 'sep']
automne = ['oct', 'nov', 'dec']

saisons = [hiver, printemps, ete, automne]

assert saisons[2] == ete
assert saisons[1][0] == 'avr'
assert saisons[1:2] == [printemps]
assert saisons[:][1] == printemps # "saisons[:]" est une copie de "saisons"


########################################
# get list2 from list1:
# list1 = [’a’, ’b’, ’c’, ’d’]
# list2 = [(0, ’a’), (1, ’b’), (2, ’c’), (3, ’d’)]
####################

list1 = ['a', 'b', 'c', 'd']

# solution 1

i = 0
list2 = []
for element in list1:
    list2.append( (i, element) )
    i += 1

print "list2:", list2

# solution 2, using enumerate

list2_2 = []
for i, element in enumerate(list1):
    list2_2.append( (i, element) )

assert list2_2 == list2

# solution 3, using enumerate and a list comprehension

list2_3 = [(i, element) for i, element in enumerate(list1)]

assert list2_3 == list2

# solution 4, using zip

list2_4 = zip(range(len(list1)), list1)

assert list2_4 == list2

# solution 5...

list2_5 = list(enumerate(list1))

assert list2_5 == list2


########################################
# get list3 from list1 and list2
# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9, 10]
# list3 = [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
####################

list1 = range(1, 6)
list2 = range(6, 11)

# solution 1

list3 = []
for i in range(len(list1)):
    list3.append( (list1[i], list2[i]) )

print 'list3:', list3

# solution 2, using a list comprehension

list3_2 = [ (list1[i], list2[i]) for i in range(len(list1))]

assert list3_2 == list3

# solution 3, using zip

list3_3 = zip(list1, list2)

assert list3_3 == list3


########################################
# get list2 and list3 from list1
# list1 = [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
# list2 = [1, 2, 3, 4, 5]
# list3 = [6, 7, 8, 9, 10]
####################

list1 = [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]

# solution 1

list2 = []
list3 = []
for e in list1:
    x, y = e
    list2.append(x)
    list3.append(y)

print "list2 : ", list2
print "list3 : ", list3


# define a generic function on the same principle

def unzip(pairs):
    """return two lists from a list of pairs"""
    resultat = ([], [])
    for x, y in pairs:
        resultat[0].append(x)
        resultat[1].append(y)
    return resultat

list2_bis, list3_bis = unzip(list1)

assert list2_bis == list2
assert list3_bis == list3

# using *args to dissociate the tuples
list2_ter, list3_ter = zip(*list1)

assert list(list2_ter) == list2
assert list(list3_ter) == list3



########################################
# get list2 and list3 from list1
# list1 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
# list2 = [22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44]
# list3 = [12, 14, 16, 18, 20, 22]
####################

list1 = range(11, 23)

# list2, solution 1

list2 = []
for element in list1:
    list2.append(2 * element)

print "list2:", list2

# list2, solution 2 using a list comprehension

list2_2 = [2*element for element in list1]

assert list2_2 == list2

# list3, solution 1

list3 = []
for element in list1:
    if element % 2 == 0:
        list3.append(element)

print "list3:", list3

# list3, solution 2 using a list comprehension

list3_2 = [x for x in list1 if not x % 2]

assert list3_2 == list3

# list3, solution 3 using slice (supposing we start from an even element)

list3_3 = list1[1::2]

assert list3_3 == list3
