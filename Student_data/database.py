# import dependency
import sqlite3

# connect to database
conn = sqlite3.connect("student.db")

# create a cursor
c = conn.cursor()

#c.execute('drop table students')

 #create a student table
c.execute("""CREATE TABLE students(
                   first_name text,
                   last_name text,
                   email text,
                   course text
)""")

# insert values into the table
students_list = [('Mayowa','Kolawole','mayowakolawole@gmail.com','DataScience'),
                 ('Ifeanyi','Akawi','ifeanyiakawi@gmail.com','DataScience'),
                 ('Toyin','Olape','toyinolape@gmail.com','DataScience'),
                 ('Uso','Ikiliagwu','usoikiliagwu@gmail.com','DataScience'),
                 ('Paul','Omikunle','paulomikunle@gmail.com','DataScience'),
                 ('Edun','Etinosa','edunetinosa@gmail.com','DataScience'),
                 ('Alex','Alexander','alexal@gmail.com','DataScience'),
                 ('Josiah','Jovido','josiahjovido@gmail.com','DataScience'),
]

c.executemany("INSERT INTO students values(?,?,?,?)",students_list)

print('command excuted successfully...')

# commit command
conn.commit()

# close connection
conn.close()