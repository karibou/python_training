"""sends a reminder mail to a list of addresses"""

import os
import sys
from datetime import datetime

try:
    from checkemail import check_email
except ImportError:
    check_email = None

EMAILPROG = "echo" # use mail if you really want to send a mail

def quote_string( s ):
    '''This function will put the string s between double quotes (").
    So that s can be passed safely on the command line of another program.'''
    return '"%s"' % s.replace('"', r'\"')

def sendfile(subject, email, fpath):
    command = '%s -s %s %s < %s' % (EMAILPROG, quote_string(subject), email,
                                    fpath)
    print 'Send mail using %r' % command
    os.system(command)

def main():
    from optparse import OptionParser
    parser = OptionParser(usage='''%prog [options] email... file

This program will send a file to all the different email
adresses provided on the command line.''')
    parser.add_option("-s", "--subject", dest="subject",
                      default="Reminder date: %s" % datetime.now().strftime('%x'),
                      help="email subject")
    parser.add_option("-c", "--check-email", dest="check_email",
                      action="store_true",
                      default=False,
                      help="check email validity first (if available)")
    (options, args) = parser.parse_args()
    if options.check_email and check_email is None:
        print 'ERROR: checking email functionality is not available'
        sys.exit(1)
    fpath = args.pop()
    status = 0
    for email in args:
        if options.check_email and not check_email(email):
            print 'skipping bad email', email
            status = 1
        else:
            sendfile(options.subject, email, fpath)
    sys.exit(status)


if __name__ == '__main__':
    main()
