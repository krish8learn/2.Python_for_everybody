import sqlite3

conn = sqlite3.connect('orgdb2.sqlite')
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Counts")

cur.execute("CREATE TABLE Counts (org TEXT,count INTEGER)")

file = input("Enter the file name: ")
fhandle = open(file)
for line in fhandle:
    if (line.startswith("From: ")):
        pieces = line.split()
        org=pieces[1].split('@')[1]
        cur.execute("SELECT count FROM Counts WHERE org= ?",(org,))
        row = cur.fetchone()
        if row is None:
            cur.execute("INSERT INTO Counts (org,count) VALUES(?,1)",(org,))
        else:
            cur.execute("UPDATE Counts SET count = count + 1 WHERE org = ?",(org,))
conn.commit()

#display
statement ="SELECT org,count FROM Counts ORDER BY count DESC"

for row in cur.execute(statement):
    print(row[1])
cur.close()
