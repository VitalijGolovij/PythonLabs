#!/usr/bin/env python3
import cgi
import html
import sqlite3

db = sqlite3.connect('cams.db')
cursor = db.cursor()

ex = cursor.execute("SELECT * FROM GOODS")


print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print("<h1>Данные таблицы:</h1>")
print("""<table>
<tr><th>Номер</th><th>Фирма</th><th>Название</th><th>Фото</th><th>Видео</th><th>Цена</th></tr> 
<tr>""")
for val in ex:
    print("<td>{}</td>".format(val[0]))
    print("<td>{}</td>".format(val[1]))
    print("<td>{}</td>".format(val[2]))
    print("<td>{}</td>".format(val[3]))
    print("<td>{}</td>".format(val[4]))
    print("<td>{}</td>".format(val[5]))
    print("</tr>")

print("""</body>
        </html>""")