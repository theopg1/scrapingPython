import argparse
import sqlite3
from scraping import Scraping
import pandas
import time

Scrap = Scraping()

parser = argparse.ArgumentParser(description='Obtenir les informations d\'un anime ou d\'un manga')
parser.add_argument('-i', '--id', type=int, required=True, help='id de l\'anime ou du manga de départ')

group = parser.add_mutually_exclusive_group()
group.add_argument('-m', '--manga', action='store_true', help='Choix d\'un manga')
group.add_argument('-a', '--anime', action='store_true', help='Choix d\'un anime')

args = parser.parse_args()

if __name__ == '__main__':

    conn = sqlite3.connect('animangas.db')
    cursor = conn.cursor()

    idValue = args.id

    if args.anime:

        try:
            while True:

                id = str(idValue)

                cursor.execute("SELECT * FROM animes WHERE ID =" + id)

                if cursor.fetchone() is None :
                    Scrap.animeScraping(id)

                df = pandas.read_sql_query("SELECT * FROM animes WHERE ID =" + id, conn)

                print(df.head())

                idValue += 1

                time.sleep(3)
        
        except KeyboardInterrupt:
            pass

    elif args.manga:

        try:
            while True:

                id = str(idValue)

                cursor.execute("SELECT * FROM mangas WHERE ID =" + id)

                if cursor.fetchone() is None :
                    Scrap.mangaScraping(id)

                df = pandas.read_sql_query("SELECT * FROM mangas WHERE ID =" + id, conn)

                print(df.head())

                idValue += 1

                time.sleep(3)

        except KeyboardInterrupt:
            pass

    else:

        print("choisissez -a ou -m  en argument pour spécifier le type de contenu voulus")

    conn.close()

