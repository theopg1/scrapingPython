import argparse
import sqlite3
from scraping import Scraping
import pandas

Scrap = Scraping()

parser = argparse.ArgumentParser(description='Obtenir les informations d\'un anime')
parser.add_argument('-i', '--id', type=int, required=True, help='id de l\'anime ou du manga')

group = parser.add_mutually_exclusive_group()
group.add_argument('-m', '--manga', action='store_true', help='Choix d\'un manga')
group.add_argument('-a', '--anime', action='store_true', help='Choix d\'un anime')

args = parser.parse_args()

if __name__ == '__main__':

    conn = sqlite3.connect('customer.db')
    cursor = conn.cursor()

    id = str(args.id)

    if args.anime:

        cursor.execute("SELECT * FROM animes WHERE ID =" + id)

        if cursor.fetchone() is None :
            Scrap.animeScraping(id)

        df = pandas.read_sql_query("SELECT * FROM animes WHERE ID =" + id, conn)

        print(df.head())

    elif args.manga:

        cursor.execute("SELECT * FROM mangas WHERE ID =" + id)

        if cursor.fetchone() is None :
            Scrap.mangaScraping(id)

        df = pandas.read_sql_query("SELECT * FROM mangas WHERE ID =" + id, conn)

        print(df.head())

    else:

        print("choisissez -a ou -m  en argument pour spécifier ce type de contenue voulut")

    conn.close()

