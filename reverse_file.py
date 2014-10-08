import sys

source="sensor.txt"


class MyFile(object):

    def __init__(self):
        self.orig="sensor.txt"
        self.target="new_sensor.txt"

    def revert(self):
        f = open(self.orig,'r')
        all_lines=f.readlines()
        f = open(self.target,'w')
        for line in reversed(all_lines):
            print "writing line : {}".format(line.strip())
            f.write(line)
        f.close()

ToRevert=MyFile()

print "Fichier a inverser : {}".format(ToRevert.orig)
ToRevert.revert()
