import time
class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def now(cls): # there is no ’self’
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)

today = Date.now()

