# -*- coding: utf-8 -*-



def get_kw_url(kw):
    """concatenate the url for searching"""

    base_url = 'http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&p=1&u=%2Fnetahtml%2FPTO%2Fsearch-bool.html&r=0&f=S&l=50&TERM1='
    last_url = '&FIELD1=&co1=AND&TERM2=&FIELD2=&d=PTXT'
    return base_url + kw + last_url
