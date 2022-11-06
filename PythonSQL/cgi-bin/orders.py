#!/usr/bin/env python3
import cgi
import html
import sqlite3

form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1")

text1 = html.escape(text1)

db = sqlite3.connect('cams.db')
cursor = db.cursor()
try:
    cursor.execute(f"INSERT INTO ORDERS (date) VALUES (?);",(text1) )
    db.commit()
except Exception:
    print("Content-type: text/html\n")
    print("""<!DOCTYPE HTML>
                <html>
                <head>
                    <meta charset="utf-8">
                    <title>Обработка данных форм</title>
                </head>
                <body>""")

    print("<h1>Произошла ошибка =(</h1>")

    print("""</body>
                </html>""")
else:
    print("Content-type: text/html\n")
    print("""<!DOCTYPE HTML>
            <html>
            <head>
                <meta charset="utf-8">
                <title>Обработка данных форм</title>
            </head>
            <body>""")

    print("<h1>Страка добавлена!</h1>")
    print("<p>Дата заказа: {}</p>".format(text1))

    print("""</body>
            </html>""")