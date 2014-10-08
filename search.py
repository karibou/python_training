from optparse import OptionParser
import os
import sys
import re

def search(directory,regexp):
    res = []
    expr = compile(regexp)
    for rep, dirnam, files in os.walk(directory):
        if not files:
            continue
        for onefile in files:
            if onefile == regexp:
                res.append(onefile)
    return res

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-i",
        "--case-sensitive",
        action="store_true",
        dest="case",
        default=False,
        help="Use case sensitive search")

    while True:
        try:
            (options, args) = parser.parse_args()
            break
        except ValueError:
            print "nombre d'arguments invalide"
            continue
    
    
    null, directory, regexp = sys.argv
    print "directory", directory, "regexp", regexp

    print 'resultat', search(directory, regexp)
