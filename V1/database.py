import sqlite3

conn = sqlite3.connect('customer.db')

cursor = conn.cursor()

cursor.execute("""CREATE TABLE animes (
        id integer,
        title text,
        original_title text,
        type text,
        genres text,
        synopsis text,
        dates text,
        episodes text,
        status text,
        image text,
        score real,
        rank integer,
        popularity integer
    )
""")

cursor.execute("""CREATE TABLE mangas (
        id integer,
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