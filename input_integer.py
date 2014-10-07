def input_integer(msg):
    res = raw_input(msg)
    print 'res', res
    return int(res)

while True:
    try:
        age = input_integer('Entrez votre age : ')
        if age >= 120:
            raise NameError
        break
    except ValueError:
        print "Format Invalide"
        continue
    except (KeyboardInterrupt, EOFError):
        print "\nInterruption demandee"
        break
    except NameError:
        print "Age impossible"
        continue
