f = open('/home/formateur/start/io/input/testconf.ini')

d = {}
section = 'global'
for l in f:
    l = l.strip()
    if l.startswith('#') or not l:
        continue
    if l.startswith('['):
        new_section = l.strip('[]')
        if new_section != section:
            d[new_section] = {}
            section = new_section
    else:
        name, value = l.split('=')
        name = name.strip()
        value = value.strip()

        subdict = d.setdefault(section, {})
        subdict[name] = value

        #subdict = d.get(section, {})
        #subdict[name] = value
        #d[section] = subdict


f.close()

print 'resultat: '
print d
