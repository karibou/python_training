# -*- coding:utf8 -*-
import os
import re


from optparse import OptionParser


def search(directory, reg=None, case=True):
# pylint: disable=C0111
    res = []
    if case:

        reg_compile = re.compile(reg, re.I)
    else:
        reg_compile = re.compile(reg)
    for _, _, filenames in os.walk(directory):
        print '_', _
        # if match de filename sur reg => append de filename sur res
        for filename in filenames:
            match = reg_compile.search(filename)
            if match:
                res.append(filename)
    return res


def main():
    parser = OptionParser(usage=u"NOMDUREPERTOIRE 'regexp'",
                          description=u'commande qui ressemble à find')
    parser.add_option('-i', '--case-insensitive',
                      action="store_false",
                       help=('precise si la recherche doit tenir compte de la'
                            'casse'),
                       dest='case_sensible',
                       default=True)
    (options, args) = parser.parse_args()
    print 'options', options
    print 'args', args
    print 'case', options.case_sensible
    rep, reg = args
    print 'resultat', search(rep, reg, options.case_sensible)


if __name__ == '__main__':
    main()
