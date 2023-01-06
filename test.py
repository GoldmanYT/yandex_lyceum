import sqlite3

con = sqlite3.connect('library_db.sqlite')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS genres(
    id INTEGER PRIMARY KEY UNIQUE NOT NULL,
    title STRING
)
''')

cur.execute('''INSERT INTO genres(title) VALUES
    ("Проза"),
    ("Фантастика")
''')

cur.execute('''CREATE TABLE IF NOT EXISTS authors(
    id INTEGER PRIMARY KEY UNIQUE NOT NULL,
    title STRING
)
''')

cur.execute('''INSERT INTO authors(title) VALUES
    ("Крапивин Владислав"),
    ("Пушкин Александр")
''')

cur.execute('''CREATE TABLE IF NOT EXISTS images(
    id INTEGER PRIMARY KEY UNIQUE NOT NULL,
    img_path STRING
)
''')

cur.execute('''INSERT INTO images(img_path) VALUES
    ("data/standard.png"),
    ("data/img1.png"),
    ("data/img2.png")
''')

cur.execute('''CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY UNIQUE NOT NULL,
    title STRING,
    author INTEGER,
    year INTEGER,
    genre INTEGER,
    img INTEGER,
    FOREIGN KEY (author) REFERENCES authors(id),
    FOREIGN KEY (genre) REFERENCES genres(id),
    FOREIGN KEY (img) REFERENCES images(id)
)
''')

cur.execute('''INSERT INTO books(title, author, year, genre, img) VALUES
    ("Трое с площади Карронад", 1, 1979, 1, 2),
    ("Чоки-чок, или Рыцарь Прозрачного Кота", 1, 2002, 2, 3),
    ("Повести Белкина", 2, 1830, 1, NULL)
''')

con.commit()
con.close()
