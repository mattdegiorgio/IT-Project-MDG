#General Imports and Scraping
import sys
import requests
from bs4 import BeautifulSoup
# Import for NLP
from textblob import TextBlob
import nltk
import re


#ARTICLE_URL1 = 'https://techcrunch.com/2018/02/25/gobee-bike-throws-in-the-towel-on-france/'

ARTICLE_URL = 'https://www.theverge.com/2019/6/5/18654044/amazon-prime-air-delivery-drone-new-design-safety-transforming-flight-video'

article_response = requests.get(ARTICLE_URL)

article_soup = BeautifulSoup(article_response.text, 'html.parser')

#article_body = article_soup.find('div', {'class':['c-entry-content']})

#article_text = article_body.getText().replace('\n', ' ')

article_text = article_soup.getText().replace('\n', ' ')
################### NLP

tokens = re.findall('\w+',article_text)

content = []

#changing all letters to lowercase
for word in tokens:
    content.append(word.lower())

print('First Article')
print ('amazon')
print(content.count('amazon'))
print('approval')
print(content.count('approval'))
print('prime')
print(content.count('prime'))
print('fly')
print(content.count('fly'))

