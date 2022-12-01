from django.shortcuts import render
from django.http import HttpResponse
from django import forms
import sqlite3

class Goods_form(forms.Form):
    id_ = forms.IntegerField()
    firm = forms.CharField()
    name = forms.CharField()
    is_photo = forms.IntegerField()
    is_video = forms.IntegerField()
    cost = forms.FloatField()

class Orders_form(forms.Form):
    id_ = forms.IntegerField()
    date = forms.CharField()

class Orders_Goods_form(forms.Form):
    order_id = forms.IntegerField()
    product_id = forms.IntegerField()
    quantity = forms.IntegerField()

def index(request):
    db = sqlite3.connect("cams.db")
    cursor = db.cursor()


    goods_list = []
    orders_list = []
    orders_goods_list = []

    for val in cursor.execute('SELECT * FROM goods LIMIT 3'):
        goods_list.append(list(val))
    for val in cursor.execute('SELECT * FROM orders LIMIT 3'):
        orders_list.append(list(val))
    for val in cursor.execute('SELECT * FROM orders_goods LIMIT 3'):
        orders_goods_list.append(list(val))

    return render(request,"index.html", context={"goods_list":goods_list, "orders_list":orders_list,"orders_goods_list":orders_goods_list})



def goods(request):
    db = sqlite3.connect("cams.db")
    cursor = db.cursor()


    if request.method == "POST":
        id_ = request.POST.get("id_")
        firm = request.POST.get("firm")
        name = request.POST.get("name")
        is_photo = request.POST.get("is_photo")
        is_video = request.POST.get("is_video")
        cost = request.POST.get("cost")
        if len(list(cursor.execute(f'SELECT * FROM goods WHERE product_id = {id_}'))) != 0:
            cursor.execute(f'UPDATE goods SET firm = "{firm}", name = "{name}", is_photo = {is_photo}, is_video = {is_video}, cost = {cost} WHERE product_id = {id_} ')
        else:
            cursor.execute(f"INSERT INTO GOODS (firm, name, is_photo, is_video, cost) VALUES (?, ?, ?, ?, ?);", (firm, name, int(is_photo), int(is_video), float(cost)))
        db.commit()


    execute = cursor.execute("SELECT * FROM goods")
    respone_list = []
    for val in execute:
        respone_list.append(list(val))
    form = Goods_form()
    return render(request,"goods.html", context={"list": respone_list,"form": form})

def orders(request):
    db = sqlite3.connect("cams.db")
    cursor = db.cursor()

    if request.method == "POST":
        id_ = request.POST.get("id_")
        date = str(request.POST.get("date"))
        if len(list(cursor.execute(f'SELECT * FROM orders WHERE order_id = {id_}'))) != 0:
            cursor.execute(f'UPDATE orders SET date = "{date}" WHERE order_id = {id_} ')
        else:
            cursor.execute(f"INSERT INTO ORDERS (date) VALUES ('{date}');")
        db.commit()

    execute = cursor.execute("SELECT * FROM orders")
    respone_list = []
    for val in execute:
        respone_list.append(list(val))
    form = Orders_form()
    return render(request, "orders.html", context={"list": respone_list, "form": form})

def orders_goods(request):
    db = sqlite3.connect("cams.db")
    cursor = db.cursor()

    if request.method == "POST":
        order_id = request.POST.get("order_id")
        product_id = request.POST.get("product_id")
        quantity = request.POST.get("quantity")
        cursor.execute(f"INSERT INTO ORDERS_GOODS (order_id, product_id, quantity) VALUES ({order_id},{product_id},{quantity});")
        db.commit()

    execute = cursor.execute("SELECT * FROM orders_goods")
    respone_list = []
    for val in execute:
        respone_list.append(list(val))
    form = Orders_Goods_form()
    return render(request, "orders_goods.html", context={"list": respone_list, "form": form})
# Create your views here.
