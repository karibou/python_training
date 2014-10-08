
import sys


class Ini(object):

    def __init__(self, thefile):
        self.init_val={}
        self.init_file=thefile
        self.d = {}
        self.section = 'global'

    def parse_file(self):
        f=open(self.init_file,'r')
        for line in f:
            line = line.strip()
            if line.startswith('#') or not line:
                continue
            if line.startswith('['):
                new_section = line.strip('[]')
                if new_section != self.section:
                    self.d[new_section] = {}
                    self.section = new_section
            else:
                name, value = line.split('=')
                name = name.strip()
                value = value.strip()

                subdict = self.d.setdefault(self.section, {})
                subdict[name] = value

                #subdict = self.d.get(self.section, {})
                #subdict[name] = value
                #self.d[self.section] = subdict
            
                print "{}".format(self.d)

