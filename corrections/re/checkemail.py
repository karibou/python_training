"""tests whether an email address is valid"""

import sys
import re

reg = re.compile(r"[-\w.]+@([-\w]+\.?)+$")

def is_email_valid(email):
    """Check that the string email is a valid email address"""
    return bool(reg.match(email))


if __name__=="__main__":
    status = 0
    if len(sys.argv) > 1:
        for email in sys.argv[1:]:
            if check_email(email):
                print "'%s' : Correct" % email
            else:
                print "'%s' : Invalid" % email
                status = 1
    else:
        print 'testing mode...',
        email_ok = [
            "ludovic.aubry@logilab.fr",
            "abc123.-@toto.org",
            "qbcd@123.abc.net",
            "-qbcd@123.abc.net",
            "lksdf@qbc.org.",
            "a.b.c.d.e@qbc.org.",
            "sdoke@-.-.org",
            ]
        email_ko = [
            "azokf@..net",
            "lksdf@qbc.org:;!:;,",
            "lksdf@qbc.org:",
            "dkjfdf@sldkf...org",
            "qsd@.org",
            ";;@dot.com",
            "@dot.com",
            ]
        for email in email_ok:
            assert is_email_valid(email), "%s should be detected valid" % email
        for email in email_ko:
            assert not is_email_valid(email), "%s shouldn't be detected valid" % email
        print 'success'
    sys.exit(status)
