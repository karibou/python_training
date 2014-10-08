
import sys


def parse_file(the_file):
    capteur = {}
    Index=0

    f = open(the_file,'r')

    for line in f:
        line = line.strip()
        if not line:
            continue
        if Index == 0:
            c1, c2, c3, c4 = line.split("\t")
            capteur[c1]=[]
            capteur[c2]=[]
            capteur[c3]=[]
            capteur[c4]=[]
        else:
            v1, v2, v3, v4 = line.split("\t")
            capteur[c1].append(v1.strip())
            capteur[c2].append(v2.strip())
            capteur[c3].append(v3.strip())
            capteur[c4].append(v4.strip())
        Index = Index + 1
        print "{}".format(capteur)
    f.close()

parse_file(sys.argv[1])
