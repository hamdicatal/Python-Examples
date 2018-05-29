# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import pymysql.cursors
from Tkinter import *
from ttk import *

db = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='python',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

cursor = db.cursor()

def ListeyiDoldur():
    sql = "SELECT * FROM users"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        liste.insert("", 0, text=row['Id'], values=(row['Ad'], row['Soyad'], row['Bolum']))

def ListeSecim(event):
    id = liste.item(liste.selection()[0])['text']
    ad = liste.item(liste.selection()[0])['values'][0]
    soyad = liste.item(liste.selection()[0])['values'][1]
    bolum = liste.item(liste.selection()[0])['values'][2]
    txtId.delete(0, END)
    txtId.insert(0, id)
    txtAdi.delete(0, END)
    txtAdi.insert(0, ad)
    txtSoyadi.delete(0, END)
    txtSoyadi.insert(0, soyad)
    cmbBolum.delete(0, END)
    cmbBolum.insert(0, bolum)

def Ekle():
    ad = txtAdi.get()
    soyad = txtSoyadi.get()
    bolum = cmbBolum.get()
    sql = "INSERT INTO users (Ad, Soyad, Bolum) VALUES ('"+ad+"','"+soyad+"','"+bolum+"')"
    cursor.execute(sql)
    db.commit()

def Duzenle():
    id = txtId.get()
    ad = txtAdi.get()
    soyad = txtSoyadi.get()
    bolum = cmbBolum.get()
    sql = "UPDATE users SET Ad = '" + ad + "', Soyad = '" + soyad + "', bolum = '" + bolum + "' WHERE Id = "+id
    cursor.execute(sql)
    db.commit()

def Sil():
    id = txtId.get()
    sql = "DELETE FROM users WHERE Id = " + id
    cursor.execute(sql)
    db.commit()

top = Tk()

lblId = Label(top, text="Id: ").grid(row=1, column=1)
txtId = Entry(top)
txtId.grid(row=1, column=2)

lblAdi = Label(top, text="Adi: ").grid(row=2, column=1)
txtAdi = Entry(top)
txtAdi.grid(row=2, column=2)

lblSoyadi = Label(top, text="Soyadi: ").grid(row=3, column=1)
txtSoyadi = Entry(top)
txtSoyadi.grid(row=3, column=2)

lblBolum = Label(top, text="Bölümü: ").grid(row=4, column=1)
cmbBolum = Combobox(top)
cmbBolum['values'] = ("Bilgisayar", "Makine", "Elektrik")
cmbBolum.current(0)
cmbBolum.grid(row=4, column=2)

btnEkle = Button(top, text="EKLE", command=Ekle)
btnEkle.grid(row=5, column=1)

btnDuzenle = Button(top, text="DUZENLE", command=Duzenle)
btnDuzenle.grid(row=5, column=2)

btnSil = Button(top, text="SIL", command=Sil)
btnSil.grid(row=5, column=3)

liste = Treeview(top)
liste["columns"] = ("col1", "col2", "col3")
liste.grid(row=6, column=1, columnspan=4)

liste.heading("#0", text="Id")
liste.heading("col1", text="Ad")
liste.heading("col2", text="Soyad")
liste.heading("col3", text="Bolum")

liste.bind('<ButtonRelease-1>', ListeSecim)

ListeyiDoldur()

top.mainloop()
