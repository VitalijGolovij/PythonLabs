#!/usr/bin/env python3
import cgi
import html
import sqlite3

form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1")
text2 = form.getfirst("TEXT_2")
text3 = form.getfirst("TEXT_3")

text1 = html.escape(text1)
text2 = html.escape(text2)
text3 = html.escape(text3)

db = sqlite3.connect('cams.db')
cursor = db.cursor()
try:
    cursor.execute(f"INSERT INTO ORDERS_GOODS (order_id, product_id, quantity) VALUES (?, ?, ?);",(int(text1),int(text2),int(text3)) )
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

    print("<h1>Строка добавлена!</h1>")
    print("<p>Номер заказа: {}</p>".format(text1))
    print("<p>Номер товара: {}</p>".format(text2))
    print("<p>Количество: {}</p>".format(text3))

    print("""</body>
                    </html>""")