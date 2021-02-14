import sqlite3
import json

conn = sqlite3.connect('rosdb.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS User;

CREATE TABLE Course(
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  title TEXT UNIQUE
);

CREATE TABLE User(
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  name TEXT UNIQUE
);

CREATE TABLE Member(
  Course_id INTEGER,
  User_id INTEGER,
  role INTEGER,
  PRIMARY KEY(User_id,Course_id)
)
''')

fname = open("roster_data.json").read()
json_data = json.loads(fname)

for entry in json_data:
    name = entry[0]
    title = entry[1]
    role = entry[2]
    print(name,title,role)

    cur.execute("INSERT OR IGNORE INTO Course (title) VALUES (?)",(title,))
    cur.execute("SELECT id FROM Course WHERE title = ?",(title,))
    Course_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO User (name) VALUES (?)",(name,))
    cur.execute("SELECT id FROM User WHERE name = ?",(name,))
    User_id = cur.fetchone()[0]

    cur.execute("INSERT OR REPLACE INTO Member (Course_id,User_id,role) VALUES(?,?,?)",(Course_id,User_id,role))

    conn.commit()

#display
state = '''SELECT hex(User.name || Course.title || Member.role ) AS X FROM
    User JOIN Member JOIN Course
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X'''
for i in cur.execute(state):
    print(i[0])
