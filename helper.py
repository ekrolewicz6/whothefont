import urllib3
import bs4
import lxml
import cssutils
import re

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

def get_fonts(domains):
	font_dict = {}
	for domain in domains:
		req = urllib2.Request(domain, headers=hdr)
		content = urllib2.urlopen(req).read()
		soup = bs4.BeautifulSoup(content, 'lxml')
		# list(set()) ensures we remove duplicates
		fonts = list(set(re.findall('font-family:(.+?)[.;}]',soup.prettify())))
		print "%s fonts: \n" % domain
		print fonts
		no_dups = list(set(fonts))
		font_dict[domain] = no_dups
	return font_dict
