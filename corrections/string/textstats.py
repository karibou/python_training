# -*- coding: utf-8 -*-
"""correction exercice statistique d'un texte
"""

import string


def read_file(filename):
    """read text from file"""
    stream = open(filename, 'r')
    txt = stream.read()
    stream.close()
    return txt

_TR_TABLE = string.maketrans(string.punctuation, ' '*len(string.punctuation))
def normalize_text(txt):
    """normalize text by removing punctations and normalizing spaces"""
    return ' '.join(txt.translate(_TR_TABLE).split())

def letter_count(txt):
    """count number of letters in txt """
    return len([letter for letter in txt if letter.isalpha()])

def word_count(txt):
    """count number of words in txt (expected to be normalized)"""
    return len(txt.split())

def letter_occurences(txt, case_sensitive=False):
    """return a dictionary containing letter occurences"""
    if case_sensitive:
        alphabet = string.ascii_letters
    else:
        alphabet = string.ascii_letters[:26]
        txt = txt.lower()
    letter_occurences = {}
    for letter in alphabet:
        letter_occurences[letter] = txt.count(letter)
    return letter_occurences

def compute_hist(letter_occurences):
    """return a list of columns size"""
    total = float(sum(letter_occurences.itervalues()))
    return [letter_occurences[letter]/total*100.0
            for letter in sorted(letter_occurences)]

def show_hist_vert(txt, case_sensitive=False, maxlength=60):
    """display histogram about the given text, vertically"""
    histdata = letter_occurences(txt, case_sensitive)
    hist = compute_hist(histdata)
    max_val = float(max(hist))
    coldata = []
    for letter, val in zip(sorted(histdata), hist):
        colsize = int(round(val * maxlength / max_val))
        coldata.append(letter + '-' + '|' * colsize + ' ' * (maxlength - colsize))
    for j in xrange(maxlength + 1, -1, -1):
        for i in xrange(len(hist)):
            print coldata[i][j],
        print

def show_hist_hor(txt, case_sensitive=False, maxlength=60):
    """display histogram about the given text, horizontally"""
    histdata = letter_occurences(txt, case_sensitive)
    hist = compute_hist(histdata)
    max_val = float(max(hist))
    for letter, val in zip(sorted(histdata), hist):
        print "%s : %s" % (letter, '-' * int(round(val * maxlength / max_val)))

def show_statistics(txt, txt_name,
                    case_sensitive=False, size=60, vertical=False):
    """display some statistics about a text on the standard output (ascii art
    included)

    """
    txt = normalize_text(txt)
    title = "Statistics about %r" % txt_name
    print title
    print "="*len(title)
    print
    print "Number of words: %d" % word_count(txt)
    print "Number of considered letters: %d" % letter_count(txt)
    print
    print "Letters distribution:"
    show_hist = show_hist_vert if vertical else show_hist_hor
    show_hist(txt, case_sensitive, size)


if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('-s', '--size', type= 'int', dest='size', default=40,
                      help= 'set histogram maximum size ')
    parser.add_option('-c', '--case-sensitive', action= 'store_true',
                      dest='case_sensitive',
                      help= 'case sensitive ')
    parser.add_option('-v', '--vertical', action= 'store_true',
                      dest='vertical',
                      help= 'show vertical histogramm')
    (options, args) = parser.parse_args()
    if not args:
        parser.error("You must specify input file name")
    else:
        for filepath in args:
            show_statistics(read_file(filepath), filepath,
                            case_sensitive=options.case_sensitive,
                            size=options.size, vertical=options.vertical)
