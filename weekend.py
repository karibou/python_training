#!/usr/bin/python

days=['lundi','mardi','mercredi','jeudi','vendredi','samedi','dimanche']

I=0
while I<7:
	if days[I] == 'samedi' or days[I] == 'dimanche':
            print "weekend day is {}".format(days[I])
        I+=1
