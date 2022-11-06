#!/usr/bin/env python3
import cgi
import html
import sqlite3

form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1")
text2 = form.getfirst("TEXT_2")
text3 = form.getfirst("TEXT_3")
text4 = form.getfirst("TEXT_4")
text5 = form.getfirst("TEXT_5")

text1 = html.escape(text1)
text2 = html.escape(text2)
text3 = html.escape(text3)
text4 = html.escape(text4)
text5 = html.escape(text5)

db = sqlite3.connect('cams.db')
cursor = db.cursor()
try:
    cursor.execute(f"INSERT INTO GOODS (firm, name, is_photo, is_video, cost) VALUES (?, ?, ?, ?, ?);",(text1,text2,int(text3),int(text4),float(text5)) )
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
    print("<p>Фирма: {}</p>".format(text1))
    print("<p>Название: {}</p>".format(text2))
    print("<p>Фото: {}</p>".format(text3))
    print("<p>Видео: {}</p>".format(text4))
    print("<p>Цена: {}</p>".format(text5))

    print("""</body>
            </html>""")