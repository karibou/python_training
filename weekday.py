#!/usr/bin/python

days=['lundi','mardi','mercredi','jeudi','vendredi','samedi','dimanche']

for day in days:
        if day == 'samedi' or day == 'dimanche':
            continue
	print "Le jour est {}".format(day)
