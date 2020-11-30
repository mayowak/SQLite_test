#!usr/bin/env python3

#import dependecies
import sqlite3
import csv

#connect to test_data
conn = sqlite3.connect('test_data.db')

#create a cursor
c = conn.cursor()

c.execute("DROP TABLE test_data")

#create a test_data table
c.execute("""CREATE TABLE test_data(age integer,
                                    sex text,
                                    bmi real,
                                    children integer,
                                    smoker text,
                                    region text)""")

#get test_data file
get_file = open('test_data.csv')

#read test_data file
read_file = csv.reader(get_file)

c.executemany("INSERT INTO  test_data VALUES (?, ?, ?, ?, ?, ?,?)", read_file)

conn.commit()

conn.close()