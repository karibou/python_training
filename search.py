#-*-coding: utf-8-*-
'''test'''
from optparse import OptionParser
import os
import sys
import re


def search(directory, regexp):
    res = []
    if CASEFLAG:
        expr = re.compile(regexp)
    else:
        expr = re.compile(regexp, re.I)

    for rep, _, files in os.walk(directory):
        if not files:
            continue
        for onefile in files:
            ret = re.search(expr, onefile)
            if ret:
                res.append("{}{}{}".format(rep, os.sep, onefile))
    return res


def main():
    global CASEFLAG
    parser = OptionParser(
        usage="{}: NOMDUREPERTOIRE 'regexp'".format(sys.argv[0]),
                            description=u"Une fonction similaire à find")
    parser.add_option("-i",
        "--case-sensitive",
        action="store_true",
        dest="CASEFLAG",
        default=False,
        help="Use case sensitive search")

    (options, _) = parser.parse_args()
    directory = sys.argv[1]
    regexp = sys.argv[2]
    if options.CASEFLAG:
        CASEFLAG = True
    print 'resultat', search(directory, regexp)

if __name__ == '__main__':
    CASEFLAG = False
    main()
