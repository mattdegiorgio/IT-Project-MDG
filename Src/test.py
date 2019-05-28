import urllib
from BeautifulSoup import BeautifulSoup
 
url="http://blog.ouseful.info"
 
data=urllib.urlopen(url)
 
soup = BeautifulSoup(data)
 
title=soup.find('title')
 
# Print the title of the page returned
print title.contents[0].strip()
 
# Scrape any link elements used for feed URL declaration
alt= soup.find('link', rel="alternate", type="application/rss+xml")
 
# The feed URL is stored in the href attribute
if alt is not None:
  print alt['href'],alt['title']