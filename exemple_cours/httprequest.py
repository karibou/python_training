from urllib2 import urlopen
import re

def create_url(base_url, paramdict):
    res = base_url + '?'
    for k, v in paramdict.iteritems():
        res += '{}={}&'.format(k, v)
    return res.strip('&')

def fetch_data(fullurl):
    f = urlopen(fullurl)
    s = f.read()
    f.close()
    return s

def get_mu0(data):
    m = re.search(r'mu0\s*=\s*([0-9.]+)', data)
    print 'groups', m.groups()
    if m:
        return m.groups()[0]

url = create_url('http://x-server.gmca.aps.anl.gov/cgi/X0h_form.exe',
                 {'xway':2, 'wave':12.4, 'coway':0, 'code':'Silicon', 'i1':1,
                  'i2':1, 'i3':1, 'df1df2':-1, 'modeout':1})
res = fetch_data(url)
print 'mu0:"{}"'.format(get_mu0(res))

