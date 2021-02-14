#this is a pyhton file that interacts between database file source file(from which we have created the database file)
import sqlite3

#creating the database file
conn = sqlite3.connect('emaildb1.sqlite')
cur = conn.cursor()

#if there is a pre exist table in database file will be deleted by this command
cur.execute('DROP TABLE IF EXISTS Users')

#creating the database in the database file
cur.execute('CREATE TABLE Users(email text, count INTEGER)')

fname = input("Enter the file name: ")
fhandle = open(fname)
for line in fhandle:
    if line.startswith('From: '):
        pieces = line.split()
        email = pieces[1].
        cur.execute('SELECT count FROM Users WHERE email = ? ',(email,))
        row = cur.fetchone()
        if row is None:
            cur.execute('INSERT INTO Users (email,count) VALUES(?,1)',(email,))
        else:
            cur.execute('UPDATE Users SET count = count+1 WHERE email =?',(email,))
        conn.commit()
#The creating, inserting, updating operation completed, now we will print data from the databse file
sqlst = 'SELECT email,count FROM Users ORDER BY count'
for row in cur.execute(sqlst):
    print(str(row[0]),row[1])
cur.close()
