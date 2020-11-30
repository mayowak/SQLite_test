import sqlite3

# query the database
conn = sqlite3.connect('student.db')

c = conn.cursor()

c.execute("SELECT * FROM students")

items = c.fetchall()
    
for item in items:
   print(item)

print("command successfully executed")

conn.commit()

conn.close()



    