# -*- coding: utf-8 -*-

"""loops and tests basics"""

semaine = ['lun', 'mar', 'mer', 'jeu', 'ven', 'sam', 'dim']

########################################
# loops
####################

# solution 1
print "Les jours de la semaine sont :",
for jour in semaine:
    print jour,
    if jour == 'ven':
        break
print
print "Les jours du we sont :",
i = 5
while i <= 6:
    print semaine[i],
    i += 1
print

# solution 2
print "Les jours de la semaine sont :",
for jour in semaine[:5]:
    print jour,
print
print "Les jours du we sont :",
we = semaine[-2:]
while we:
    print we.pop(0),
print

########################################
# tests
####################

for jour in semaine:
    print jour, ":",
    if jour in semaine[0:4]:
        print "Au travail !"
    elif jour == 'ven':
        print "Chouette c'est vendredi !"
    else:
        print "Arggh, ce week-end je dois préparer une présentation pour lundi !"
