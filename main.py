import urllib2
import bs4
import lxml
import cssutils
import re
import helper as h


# Get a list of domains from sample.txt
domains = ['http://'+line for line in (open('sample.txt','r')).read().splitlines()]
font_dict = h.get_fonts(domains)
print font_dict 