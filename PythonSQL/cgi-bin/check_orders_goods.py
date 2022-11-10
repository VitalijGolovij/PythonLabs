#!/usr/bin/env python3
import cgi
import html
import sqlite3

db = sqlite3.connect('cams.db')
cursor = db.cursor()

ex = cursor.execute("SELECT * FROM ORDERS_GOODS")


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
<tr><th>Номер заказа</th><th>Номер товара</th><th>Количество</th></tr> 
<tr>""")
for val in ex:
    print("<td>{}</td>".format(val[0]))
    print("<td>{}</td>".format(val[1]))
    print("<td>{}</td>".format(val[2]))
    print("</tr>")

print("""</body>
        </html>""")