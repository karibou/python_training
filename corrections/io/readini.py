import sys

def read_inifile(filename):
    result = {}
    section = 'global'
    stream = open(filename)
    for line in stream:
        line = line.strip()
        if line and line[0] != '#':
            if line[0] == '[' and line[-1] == ']':
                section = line[1:-1]
            else:
                key, value = line.split('=', 1)
                result.setdefault(section, {})[key.strip()] = value.strip()
    stream.close()
    return result


if __name__ == '__main__':
    if len(sys.argv) > 1:
        for inifile in sys.argv[1:]:
            print read_inifile(inifile)
    else:
        inifile = raw_input('specify file to read: ')
        print read_inifile(inifile)

