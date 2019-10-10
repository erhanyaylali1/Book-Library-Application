import sqlite3

con = sqlite3.connect("database.db")
cursor = con.cursor()
con.execute("CREATE TABLE IF NOT EXISTS LIBRARY (NAME TEXT,AUTHOR TEXT,EDITOR TEXT,PAGE INT)")

def veri_ekleme(isim,yazar,yayınevi,sayfa_sayisi):
    cursor.execute("INSERT INTO LIBRARY values (?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayisi))
    con.commit()

sayfa_sayisi = -1

while(sayfa_sayisi!=0):
    isim = input("isim: ")
    yazar = input("yazar: ")
    yayınevi = input("yayınevi: ")
    sayfa_sayisi = input("sayfa sayisi: ")
    veri_ekleme(isim,yazar,yayınevi,sayfa_sayisi)
    print("--------------------------")

con.close()