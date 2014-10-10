from urllib2 import urlopen
import re
import sys

#    stream = urlopen('http://x-server.gmca.aps.anl.gov/cgi/WWW_form.exe')
#    html = stream.read()
#    stream.close()

def create_url(baseurl, param_dict):
    option_list='?'
    for key, param in param_dict.iteritems():
        option_list=option_list + '{}={}'.format(key,param) + '&'
    option_list = option_list.rstrip("&")
    return baseurl + option_list

def fetch_data(fullurl):
    try:
        stream = urlopen(fullurl)
        html = stream.read()
        stream.close
        return html
    except:
        print "Erreur"

def parse_result(html_data,regexp):
    m = re.search(r'{}\s*=\s*([0-9.]+)'.format(regexp), html_data)
    index = html_data.find(regexp)
    print '{} : '.format(regexp), m.groups()

if __name__ == '__main__':

    URL='http://x-server.gmca.aps.anl.gov/cgi/X0h_form.exe'
    Dict={ 'xway': 2,
                'wave': 12.4,
                'coway': 0,
                'code': 'Silicon',
                'i1': 1,
                'i2': 1,
                'i3': 1,
                'df1df2':-1,
                'modeout':1
                }

    print create_url(URL, Dict)
    Data = fetch_data(create_url(URL, Dict))
    parse_result(Data,sys.argv[1])
