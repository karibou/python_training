import requests
import re



def get_mu0(data):
    m = re.search(r'mu0\s*=\s*([0-9.]+)', data)
    print 'groups', m.groups()
    if m:
        return m.groups()[0]

res = requests.get('http://x-server.gmca.aps.anl.gov/cgi/X0h_form.exe',
                   params={'xway':2, 'wave':12.4,
                           'coway':0, 'code':'Silicon', 'i1':1,
                           'i2':1, 'i3':1, 'df1df2':-1, 'modeout':1})
print 'status:', res.status_code
print 'mu0:"{}"'.format(get_mu0(res.content))

