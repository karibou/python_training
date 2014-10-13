# -*- coding: utf-8 -*-
"""exception handling"""

class OutOfBound(Exception):
    """Exception raised when some value is out of bounds"""
    def __init__(self, msg, value):
        Exception.__init__(self)
        self.msg = msg
        self.value = value


def input_integer(question, minv=None, maxv=None):
    """display a question, wait for user answer, convert it to an integer and
    return it.

    Raise `OutOfBound` if input is out of bounds
    """
    # display the question and wait for an answer
    value = raw_input(question)
    try:
        # transform it into an integer
        intv = int(value)
    except ValueError:
        # not an integer, display error message and try again
        print 'Please type an integer'
        intv = input_integer(question)
    if minv is not None and intv < minv:
        raise OutOfBound("should be >= %s" % minv, intv)
    if maxv is not None and intv > maxv:
        raise OutOfBound("should be <= %s" % maxv, intv)
    return intv


if __name__ == '__main__':
    try:
        age = input_integer('How old are you?', 0, 150)
        print 'You are %i years old' % age
    except KeyboardInterrupt:
        pass
    except OutOfBound as ex:
        print(ex.msg)
        print(ex.value)
