import mysql.connector
import datetime
import sys

conn = mysql.connector.connect(
         user='root',
         password='root',
         host='10.231.30.60',
         database='scrapy')
cursor = conn.cursor()

sql = "SELECT * FROM aastock;"

cursor.execute(sql)

results = cursor.fetchall()

print(results[0][0])