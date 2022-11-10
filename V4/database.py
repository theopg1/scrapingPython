import sqlite3

conn = sqlite3.connect('animangas.db')

cursor = conn.cursor()

cursor.execute("DROP TABLE animes")

cursor.execute("""CREATE TABLE animes (
        id integer PRIMARY KEY,
        title text,
        original_title text,
        type text,
        genres text,
        synopsis text,
        dates text,
        saison text,
        année text,
        episodes text,
        status text,
        image text,
        score real,
        rank integer,
        popularity integer
    )
""")

cursor.execute("DROP TABLE mangas")

cursor.execute("""CREATE TABLE mangas (
        id integer PRIMARY KEY,
        title text,
        original_title text,
        type text,
        genres text,
        synopsis text,
        dates text,
        tomes text,
        chapters text,
        status text,
        image text,
        score real,
        rank integer,
        popularity integer
    )
""")

conn.commit()

conn.close()