import urllib
import sqlite3
import bs4

conn = sqlite3.connect('customer.db')

cursor = conn.cursor()

url_animes = "https://myanimelist.net/manga/41467"
    
from urllib import request

request_text = request.urlopen(url_animes).read()

page = bs4.BeautifulSoup(request_text, "html.parser")

#titleManga
if page.find('span', {'class' : 'h1-title'}) is not None :
    title = page.find('span', {'class' : 'h1-title'}).text

#original title
valueToFind = "Japanese:"
if page.find('span', string=valueToFind) is not None :
    originalTitle = page.find('span', string=valueToFind).parent.text.replace(valueToFind,"").strip()

#image
image = page.find('div', {'class' : 'leftside'}).find('img').get("data-src")

#type
valueToFind = "Type:"
if page.find('span', string=valueToFind) is not None :
    Type = page.find('span', string=valueToFind).parent.text.replace(valueToFind,"").strip()

#status
valueToFind = "Status:"
if page.find('span', string=valueToFind) is not None :
    status = page.find('span', string=valueToFind).parent.text.replace(valueToFind,"").strip()

#datesManga
valueToFind = "Published:"
if page.find('span', string=valueToFind) is not None :
    published = page.find('span', string=valueToFind).parent.text.replace(valueToFind,"").strip()
    published = published.replace("to","au")

#genres
genres = ""
for item in page.find('span', string="Genres:").parent.findAll('a') :
    genres = genres + item.get('title') + ", "
genres = genres[:-2]

#tomes
valueToFind = "Volumes:"
if page.find('span', string=valueToFind) is not None :
    status = page.find('span', string=valueToFind).parent.text.replace(valueToFind,"").strip()

#chapitres
valueToFind = "Chapters:"
if page.find('span', string=valueToFind) is not None :
    status = page.find('span', string=valueToFind).parent.text.replace(valueToFind,"").strip()

#synopsisManga
if page.find('span', {'itemprop' : 'description'}) is not None :
    synopsis = page.find('span', {'itemprop' : 'description'}).text.strip()

#score
score = page.find('div', {'class' : 'score-label'}).text.strip()

#rank
rank = page.find('span', {'class' : 'numbers ranked'}).find('strong').text.replace("#","").strip()

#popularity
popularity = page.find('span', {'class' : 'numbers popularity'}).find('strong').text.replace("#","").strip()

conn.commit()

conn.close()