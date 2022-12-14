import sqlite3
import xml.etree.ElementTree as ET
def createdb(db, cursor):

    create_table = """
            CREATE TABLE IF NOT EXISTS GOODS
            (
                 product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                 firm TEXT,
                 name TEXT,
                 is_photo INTEGER CHECK( (is_photo = 0) OR (is_photo = 1) ),
                 is_video INTEGER CHECK( (is_video = 0) OR (is_video = 1) ),
                 cost REAL
            )
        """
    cursor.execute(create_table)

    create_table = """
                CREATE TABLE IF NOT EXISTS ORDERS
                (
                     order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                     date DATETIME
                )
            """
    cursor.execute(create_table)

    create_table = """
                CREATE TABLE IF NOT EXISTS ORDERS_GOODS
                (
                     order_id INTEGER ,
                     product_id INTEGER,
                     quantity INTEGER,
                     PRIMARY KEY(order_id, product_id),
                     FOREIGN KEY(order_id) REFERENCES ORDERS(order_id),
                     FOREIGN KEY(product_id) REFERENCES GOODS(product_id)
                )

            """
    cursor.execute(create_table)
    db.commit()

def filldb(db, cursor):
    values = ["""
        INSERT INTO GOODS (firm, name, is_photo, is_video, cost)
        VALUES ("asus", "pt-100", 1, 0, 20399.99);
        ""","""
        INSERT INTO GOODS (firm, name, is_photo, is_video, cost)
        VALUES ("hp", "lh-1", 1, 0, 10599.99);
        ""","""
        INSERT INTO GOODS (firm, name, is_photo, is_video, cost)
        VALUES ("asus", "pv-200", 0, 1, 40200.50);
        ""","""
        INSERT INTO GOODS (firm, name, is_photo, is_video, cost)
        VALUES ("hp", "vid5", 0, 1, 3599.00);
        ""","""
        INSERT INTO GOODS (firm, name, is_photo, is_video, cost)
        VALUES ("nokia", "C270", 0, 1, 22300.39);
        ""","""
        INSERT INTO GOODS (firm, name, is_photo, is_video, cost)
        VALUES ("asus", "FULL233", 1, 1, 58000.00);
        ""","""
        INSERT INTO GOODS (firm, name, is_photo, is_video, cost)
        VALUES ("hp", "L400", 1, 1, 44000.00);
    """]
    for value in values:
        cursor.execute(value)

    values = ["""
        INSERT INTO ORDERS (date)
        VALUES ("10.03.2022");
        ""","""
        INSERT INTO ORDERS (date)
        VALUES ("11.03.2022");
        ""","""
        INSERT INTO ORDERS (date)
        VALUES ("12.03.2022");
        ""","""
        INSERT INTO ORDERS (date)
        VALUES ("13.03.2022");
        ""","""
        INSERT INTO ORDERS (date)
        VALUES ("14.03.2022");
    """]
    for value in values:
        cursor.execute(value)

    values = ["""
            INSERT INTO ORDERS_GOODS(order_id, product_id, quantity)
            VALUES (1, 2, 3);
            ""","""
            INSERT INTO ORDERS_GOODS(order_id, product_id, quantity)
            VALUES (1, 3, 1);
            ""","""
            INSERT INTO ORDERS_GOODS(order_id, product_id, quantity)
            VALUES (2, 1, 1);
            ""","""
            INSERT INTO ORDERS_GOODS(order_id, product_id, quantity)
            VALUES (2, 2, 3);
            ""","""
            INSERT INTO ORDERS_GOODS(order_id, product_id, quantity)
            VALUES (2, 3, 2);
            ""","""
            INSERT INTO ORDERS_GOODS(order_id, product_id, quantity)
            VALUES (3, 1, 1);
            ""","""
            INSERT INTO ORDERS_GOODS(order_id, product_id, quantity)
            VALUES (4, 2, 1);
            ""","""
            INSERT INTO ORDERS_GOODS(order_id, product_id, quantity)
            VALUES (4, 5, 1);
            ""","""
            INSERT INTO ORDERS_GOODS(order_id, product_id, quantity)
            VALUES (5, 7, 5);
        """]
    for value in values:
        cursor.execute(value)
    db.commit()

def createXml (rows):
    root = ET.Element("data")
    for row in rows:
        author = ET.SubElement(root, "goods")
        id_a = ET.SubElement(author, "id")
        name = ET.SubElement(author, "frim")
        surname = ET.SubElement(author, "name")
        birtday = ET.SubElement(author, "is_photo")
        cit = ET.SubElement(author, "is_video")
        cost = ET.SubElement(author, "cost")
        id_a.text=str(row[0])
        name.text=str(row[1])
        surname.text=str(row[2])
        birtday.text=str(row[3])
        cit.text=str(row[4])
        cost.text = str(row[5])

    message=ET.tostring(root,"utf 8")
    doc = '<?xml version="1.0" encoding="UTF-8"?>' + message.decode("utf-8")

    tree=ET.ElementTree(root)
    tree.write("goods.xml",encoding="utf 8")

def readXMLtoGOODS(xmlfile,db,cursor):
    tree = ET.parse(xmlfile)
    root = tree.getroot()

    for val_r in root:
        cursor.execute(f"INSERT INTO GOODS (firm, name, is_photo, is_video, cost) VALUES (?, ?, ?, ?, ?);", (
        val_r[0].text, val_r[1].text, int(val_r[2].text), int(val_r[3].text), float(val_r[4].text)))
    db.commit()


def main():
    db = sqlite3.connect('cams.db')
    cursor = db.cursor()
    #createdb(db, cursor)
    #filldb(db,cursor)


    for val in cursor.execute("SELECT * FROM GOODS"):
        print(val)

    for val in cursor.execute("SELECT * FROM ORDERS"):
        print(val)

    for val in cursor.execute("SELECT * FROM ORDERS_GOODS"):
        print(val)

    for val in cursor.execute("""SELECT order_id, SUM(SUMM) 
    FROM 
    (SELECT ORDERS_GOODS.order_id as order_id, ORDERS_GOODS.product_id as product_id, ORDERS_GOODS.quantity as quantity, (GOODS.cost * ORDERS_GOODS.quantity) as SUMM 
    FROM ORDERS_GOODS INNER JOIN GOODS ON GOODS.product_id = ORDERS_GOODS.product_id) 
    GROUP BY order_id"""):
        print(val)


if __name__ == "__main__":
    main()