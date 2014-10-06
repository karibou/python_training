#!/usr/bin/python

days=['lundi','mardi','mercredi','jeudi','vendredi','samedi','dimanche']

for day in days:
        if day in days[:3]:
            print "Au Travail !"
	elif day in days[4]:
            print "Chouette c'est vendredi"
        elif day in days[5:]:
            print "Arrgh, .*"
