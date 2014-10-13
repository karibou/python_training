
import unittest
import checkmail

class MailTest(unittest.TestCase):
    def setUp(self):
        self.right_list = ["ludovic.aubry@logilab.fr",
                           "abc123.-@toto.org",
                           "qbcd@123.abc.net",
                           "a.b.c.d.e@qbc.org.",
                           "-qbcd@123.abc.net",
                           "lksdf@qbc.org.",
                           "dkjfdf.@sldkf.org",
                           "sdoke@-.-.org"]
        self.wrong_list = ["azokf@..net",
                           "lksdf@qbc.org:;!:;,",
                           "lksdf@qbc.org:",
                           "dkjfdf@sldkf...org",
                           "qsd@.org",
                           ";;@dot.com",
                           "@dot.com"]
    def test_right_mail(self):
        # Test right mail.
        for mail in self.right_list:
            self.assertTrue(checkmail.checkemail(mail),
                            " ".join([mail, "must be right."]))

    def test_wrong_mail(self):
        # Test wrong mail.
        for mail in self.wrong_list:
            self.assertFalse(checkmail.checkemail(mail),
                             " ".join([mail, "must be wrong."]))

if __name__ == "__main__":
    unittest.main()
