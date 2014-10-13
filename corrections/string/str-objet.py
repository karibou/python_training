# -*- coding: iso-8859-1 -*-
"""String manipulation"""

s1 = "bonjour    tout le     monde \n"
expected = "bonjour tout le monde"


# using split / join
mots_nettoyes = []
for mot in s1.split():
    mots_nettoyes.append(mot)
s2 = ' '.join(mots_nettoyes)

assert expected == s2

# shorter version
s2 = ' '.join(s1.split())

assert expected == s2


def xml_escape(chaine):
    '''escape ', ", &, < and > by html entities'''
    return (chaine.replace('&', '&amp;')
            .replace('<', '&lt;').replace(">", "&gt;")
            .replace("'", "&#39;").replace('"', "&quot;"))

assert xml_escape('<hello & > \'"hop"') == '&lt;hello &amp; &gt; &#39;&quot;hop&quot;'
