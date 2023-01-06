import sqlite3

con = sqlite3.connect('countries_db.sqlite')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS languages(
    id INTEGER PRIMARY KEY UNIQUE NOT NULL,
    title STRING
)
''')

cur.execute('''INSERT INTO languages(title) VALUES
    ("English"),
    ("Russian"),
    ("Chinese")
''')

cur.execute('''CREATE TABLE IF NOT EXISTS flags(
    id INTEGER PRIMARY KEY UNIQUE NOT NULL,
    img_path STRING
)
''')

cur.execute('''INSERT INTO flags(img_path) VALUES
    ("data/Russian_flag.png"),
    ("data/USA_flag.png"),
    ("data/China_flag.png"),
    ("data/UK_flag.png")
''')

cur.execute('''CREATE TABLE IF NOT EXISTS countries(
    id INTEGER PRIMARY KEY UNIQUE NOT NULL,
    title STRING,
    language INTEGER,
    year INTEGER,
    flag INTEGER,
    FOREIGN KEY (language) REFERENCES languages(id),
    FOREIGN KEY (flag) REFERENCES flags(id)
)
''')

cur.execute('''INSERT INTO countries(title, language, year, flag) VALUES
    ("Россия", 2, 1991, 1),
    ("Китай", 3, 1949, 3),
    ("США", 1, 1800, 2),
    ("Великобритания", 1, 1707, 4)
''')

con.commit()
con.close()
