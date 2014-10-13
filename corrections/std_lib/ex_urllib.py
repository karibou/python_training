#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib, urllib2
import re
from pprint import pprint


BASEURL = 'http://x-server.gmca.aps.anl.gov/cgi/X0h_form.exe'
PROXY = 'http://127.0.0.1:8000' # could be used for adv_fetch_data

def create_url(base_url, paramdict):
    url_values = urllib.urlencode(paramdict)
    return base_url + '?' + url_values

def fetch_data(full_url):
    f = urllib.urlopen(full_url)
    content = f.readlines()
    f.close()
    return content

def adv_fetch_data(full_url, proxy=None):
    """This function accept a proxy URL as second argument
    """
    if proxy is None:
        proxies = {}
    else:
        proxies = {'http': proxy}
    proxy_handler = urllib2.ProxyHandler(proxies)
    opener = urllib2.build_opener(proxy_handler)
    f = opener.open(full_url)
    content = f.read()
    f.close()
    return content

def parse_result(content):
    for line in content:
        if line.startswith('Absorption factor'):
            line = line.strip()
            mu0 = float(line.split('=')[-1])
    return mu0

def adv_parse_result(content):
    searchstring = re.compile(
    r"""
    rho\=\s*(?P<rho>(\d+).(\d+))
    .*
    a1\=\s*(?P<uc_a>(\d+).(\d+))
    .*
    a2\=\s*(?P<uc_b>(\d+).(\d+))
    .*
    a3\=\s*(?P<uc_c>(\d+).(\d+))
    .*
    a4\=\s*(?P<uc_alpha>(\d+).(\d+))
    .*
    a5\=\s*(?P<uc_beta>(\d+).(\d+))
    .*
    a6\=\s*(?P<uc_gamma>(\d+).(\d+))
    .*
    wave\=\s*(?P<wavelength>(\d+).(\d+)*)
    .*
    energy\=\s*(?P<energy>(\d+).(\d+)*)
    .*
    xr0\=\s*(?P<chi_r0>-?(\d+).(\d+)E-\d+)
    .*
    xi0\=\s*(?P<chi_i0>-?(\d+).(\d+)E-\d+)
    .*
    mu0\=\s*(?P<mu_0>(\d+).(\d+))
    .*
    hkl\=\s*(?P<hkl>(\d+)\ (\d+)\ (\d+))
    .*
    QB\=\s*(?P<theta_Bragg>(\d+).(\d+))
    .*
    sin\(2\*QB\)\=\s*(?P<sin2thetaBragg>(\d+).(\d+))
    .*
    pol=Sigma
    .*
    xrhsg\=\s*(?P<chi_rh>-?(\d+).(\d+)E-\d+)
    .*
    xihsg\=\s*(?P<chi_ih>-?(\d+).(\d+)E-\d+)
    .*
    FWHMurad_sg\=\s*(?P<width_th>(\d+).(\d+))
    """
    ,re.X|re.DOTALL)
    return searchstring.search(content).groupdict()


if __name__ == '__main__':
    param = {'xway': 2, 'coway': 0, 'modeout': 1, 'detail': 0,
             'wave': 12.4, 'code': 'Silicon',
             'i1': 1, 'i2': 1, 'i3': 1, 'df1df2': 2}
    full_url = create_url(BASEURL, param)
    content = fetch_data(full_url)
    print "mu0: ", parse_result(content)

    adv_content = adv_fetch_data(full_url)
    resultdict = adv_parse_result(adv_content)
    pprint(resultdict)
