from optparse import OptionParser

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-n", "--name", dest="file",
            help="output filename")
    parser.add_option("-q", "--quiet",
            action="store_false",
            dest="verbose", default=True,
            help="don't print debug messages")
    (options, args) = parser.parse_args()
    output_filename = options.filename
    rbose = options.verbose
    print 'outputfilename', output_filename

