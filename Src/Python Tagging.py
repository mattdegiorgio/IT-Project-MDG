#General Imports and Scraping
import sys
import requests
from bs4 import BeautifulSoup
# Import for NLP
from textblob import TextBlob
# Import for ploting Library


WEB_PAGE_TO_SCRAPE_URL = "http://techcrunch.com/"

#requests.get('http://www.google.com')
response = requests.get(WEB_PAGE_TO_SCRAPE_URL)

#response_text = response.txt

fetched_html = response.text
fetched_html[:500]

fetched_html = ''
with open('techcrunch.html','r') as f:
    fetched_html = f.read()
fetched_html[:500]

#BeatautifulSoup(YOUR_RAW_HTML_TEXT,'html.parser')

souped_page = BeautifulSoup(fetched_html,'html.parser')
souped_page.find('title').getText()

souped_page.find('ul')
#Finite Searching
element_search = souped_page.find('ul',{'class':'river'})
#Matches Attributues
element_search.attrs

article_listings = souped_page.find_all('li',{'class':'river-block'})

print('Number of Article :',len(article_listings))
print('printing article titles \n')

for a in article_listings:
    if 'data-sharetitle' in a.attrs:
        print(a['data-sharetitle'])

## Test ##
backup_article = ''
with open('techcrunch_article.html','r') as f:
    backup_article = f.read()
ARTICLE_URL = 'https://techcrunch.com/2018/02/25/gobee-bike-throws-in-the-towel-on-france/'

article_response = requests.get(ARTICLE_URL)
article_soup = BeautifulSoup(article_response.text, 'html.parser')
article_body = article_soup.find('div',{'class':['article-entry']})
article_body

article_text = article_body.getText().replace('\n',' ')
article_text

print (article_body)

########################################
## NLP
## Test

