import xml.etree.ElementTree as ET
import sqlite3

conn= sqlite3.connect('trackdb1.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artist(
   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
   name TEXT UNIQUE
);

CREATE TABLE Album(
   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
   artist_id INTEGER,
   title TEXT UNIQUE
);

CREATE TABLE Genre(
   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
   name TEXT UNIQUE
);

CREATE TABLE Track(
   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
   title TEXT UNIQUE,
   album_id INTEGER,
   genre_id INTEGER,
   len INTEGER, rating INTEGER, count INTEGER
);
''')

fname = open("Library.xml")

def lookup(d,key):
    found = False
    for child in d:
        if found: return child.text
        if child.tag =='key' and child.text == key:
            found =True
    return None

stuff = ET.parse(fname)
whole = stuff.findall('dict/dict/dict')
print('Dict count:',len(whole))
for entry in whole:
    if(lookup(entry,'Track ID')is None):continue

    name = lookup(entry,'Name')
    artist = lookup(entry,'Artist')
    album = lookup(entry,'Album')
    genre = lookup(entry,'Genre')
    len = lookup(entry,'Total Time')
    rating = lookup(entry,'Rating')
    count = lookup(entry,'Play_count')

    if name is None or artist is None or album is None or genre is None:
        continue
    print("song name:",name,"artist name:",artist,"album name:",album,",genre name:",genre,",len:",len,",rate:",rating,",count:",count)
#inserting into Artist table
    cur.execute("INSERT OR IGNORE INTO Artist(name) VALUES (?)",(artist,))
    cur.execute("SELECT id FROM Artist WHERE name = ?",(artist,))
    artist_id = cur.fetchone()[0]
#inserting album TABLE
    cur.execute("INSERT OR IGNORE INTO Album(title,artist_id) VALUES(?,?)",(album,artist_id))
    cur.execute("SELECT id FROM Album WHERE title=?",(album,))
    album_id = cur.fetchone()[0]
#inserting into Genre TABLE
    cur.execute("INSERT OR IGNORE INTO Genre(name) VALUES(?)",(genre,))
    cur.execute("SELECT id FROM Genre WHERE name =? ",(genre,))
    genre_id = cur.fetchone()[0]
#inserting into Track TABLE
    cur.execute("INSERT OR IGNORE INTO Track(title,album_id,genre_id,len,rating,count) VALUES (?,?,?,?,?,?)",(name,album_id,genre_id,len,rating,count))
    conn.commit()
print("--------------------------------------------------------------------------------------------------------------------")
sqlst = 'SELECT Track.title,Artist.name,Album.title,Genre.name FROM Track JOIN Genre JOIN Album JOIN Artist WHERE Track.genre_id = Genre.id and Track.album_id = Album.id and Album.artist_id=Artist.id ORDER BY Artist.name LIMIT 3 '
for row in cur.execute(sqlst):
    print(str(row[0]),str(row[1]),str(row[2]),str(row[3]))
cur.close()
