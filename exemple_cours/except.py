
def input_integer2(msg):
    res = raw_input(msg)
    print 'res', res
    try:
        number = int(res)
        print 'number ok', number
    except ValueError:
        print 'pas un entier, retentez!'
        input_integer2(msg)


def input_integer(msg, limitup, limitdown):
    while True:
        res = raw_input(msg)
        print 'res', res
        try:
            number = int(res)
            check_number_limit(number, limitup, limitdown)
            break
        except ValueError:
            print 'pas un entier, retentez!'
        except OutOfLimitError as e:
            print e.message
            raise
    return number

class OutOfLimitError(Exception):
    "error when testing an arg in some limit"

def check_number_limit(number, limitup, limitdown):
    if number <= limitup and number >= limitdown:
        print 'ok, number dans la limite'
    else:
        raise OutOfLimitError('en dehors des limites ({},{}), retentez'.format(limitdown, limitup))

def ask_age():
    try:
        age = input_integer('Age ?', 120, 0)
    except KeyboardInterrupt:
        print 'ctrl-c recu => stop'
        return
    except EOFError:
        print 'ctrl-d recu => stop'
        return
    except OutOfLimitError:
        print 'recu exception OutOfLimitError'
        raise
    print 'age', age

ask_age()
