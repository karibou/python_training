
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
            header = line.split("\t")
            for head in header:
                capteur[head] = []
        else:
            oneline = line.split("\t")
            for index, field in enumerate(oneline):
                head = header[index]
                capteur[head].append(field.strip())
        Index = Index + 1
        print "{}".format(capteur)
    f.close()
    return(capteur)

def write_file(mesur):
    f2 = open("mesures_auto.py",'w')
    f2.write('unevariable = {}'.format(str(mesur)))
    f2.close()

mes_mesures = parse_file(sys.argv[1])
write_file(mes_mesures)
