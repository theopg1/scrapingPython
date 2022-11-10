import urllib
from urllib import request
import sqlite3
import bs4

class Scraping:
    "Scraping d'animes et de mangas"

    @staticmethod
    def animeScraping(id):

        conn = sqlite3.connect('animangas.db')

        cursor = conn.cursor()

        url_animes = "https://myanimelist.net/anime/" + id

        try:
            request_text = request.urlopen(url_animes).read().decode('utf-8')

            page = bs4.BeautifulSoup(request_text, "html.parser")

            #titleAnime
            if page.find('h1', {'class' : 'title-name'}) is not None :
                title = page.find('h1', {'class' : 'title-name'}).text

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

            #datesAnime
            valueToFind = "Aired:"
            if page.find('span', string=valueToFind) is not None :
                aired = page.find('span', string=valueToFind).parent.text.replace(valueToFind,"").strip()
                aired = aired.replace("to","au")

            #genres
            genres = ""
            for item in page.find('span', string="Genres:").parent.findAll('a') :
                genres = genres + item.get('title') + ", "
            genres = genres[:-2]

            #episodes
            valueToFind = "Episodes:"
            if page.find('span', string=valueToFind) is not None :
                episodes = page.find('span', string=valueToFind).parent.text.replace(valueToFind,"").strip()

            #synopsisAnime
            if page.find('p', {'itemprop' : 'description'}) is not None :
                synopsis = page.find('p', {'itemprop' : 'description'}).text.strip()

            #score
            score = page.find('div', {'class' : 'score-label'}).text.strip()

            #rank
            rank = page.find('span', {'class' : 'numbers ranked'}).find('strong').text.replace("#","").strip()

            #popularity
            popularity = page.find('span', {'class' : 'numbers popularity'}).find('strong').text.replace("#","").strip()

            #Sortie
            valueToFind = "Premiered:"
            if page.find('span', string=valueToFind) is not None :
                sortie = page.find('span', string=valueToFind).parent.text.replace(valueToFind,"").strip()
                sortieSplit = sortie.split(" ")
                saison = sortieSplit[0]
                année = sortieSplit[1]

            sql = """INSERT INTO animes VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""

            data = (id, title, originalTitle, Type, genres, synopsis, aired, saison, année, episodes, status, image, score, rank, popularity)

            cursor.execute(sql, data)

            conn.commit()

        except:
            print("ID inexistant")

        conn.close()

    @staticmethod
    def mangaScraping(id):

        conn = sqlite3.connect('animangas.db')

        cursor = conn.cursor()

        url_animes = "https://myanimelist.net/manga/" + id

        try:
        
            request_text = request.urlopen(url_animes).read().decode('utf-8')

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
                tomes = page.find('span', string=valueToFind).parent.text.replace(valueToFind,"").strip()

            #chapitres
            valueToFind = "Chapters:"
            if page.find('span', string=valueToFind) is not None :
                chapitres = page.find('span', string=valueToFind).parent.text.replace(valueToFind,"").strip()

            #synopsisManga
            if page.find('span', {'itemprop' : 'description'}) is not None :
                synopsis = page.find('span', {'itemprop' : 'description'}).text.strip()

            #score
            score = page.find('div', {'class' : 'score-label'}).text.strip()

            #rank
            rank = page.find('span', {'class' : 'numbers ranked'}).find('strong').text.replace("#","").strip()

            #popularity
            popularity = page.find('span', {'class' : 'numbers popularity'}).find('strong').text.replace("#","").strip()

            sql = """INSERT INTO mangas VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""

            data = (id, title, originalTitle, Type, genres, synopsis, published, tomes, chapitres, status, image, score, rank, popularity)

            cursor.execute(sql, data)

            conn.commit()

        except:
            print("ID inexistant")

        conn.close()