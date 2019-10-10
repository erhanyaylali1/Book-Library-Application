import sys
from PyQt5 import QtWidgets,QtGui
import sqlite3
import os


class Pencere(QtWidgets.QMainWindow):

    def __init__(self):

        super().__init__()
        self.ui()
        self.database()
        self.pencere = Widget1()
        self.setCentralWidget(self.pencere)


    def database(self):

        self.con = sqlite3.connect("database.db")
        self.cursor = self.con.cursor()
        self.con.execute("CREATE TABLE IF NOT EXISTS LIBRARY (NAME TEXT,AUTHOR TEXT,EDITOR TEXT,PAGE INT)")
        self.con.commit()


    def ui(self):

        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.setWindowTitle("Kitaplık")
        self.setGeometry(450,240,831,600)

        menubar = self.menuBar()

        islemler = menubar.addMenu("İşlemler")

        book_add = QtWidgets.QAction("Kitap Ekle",self)
        book_add.triggered.connect(self.addbook)

        book_delete = QtWidgets.QAction("Kitap Silme",self)
        book_delete.triggered.connect(self.deletebook)

        book_update = QtWidgets.QAction("Kitap Güncelle",self)
        book_update.triggered.connect(self.update)

        about = QtWidgets.QAction("Program Hakkında", self)
        about.triggered.connect(self.about)


        islemler.addAction(book_add)
        islemler.addAction(book_delete)
        islemler.addAction(book_update)
        islemler.addAction(about)

        self.show()


    def addbook(self):

        self.newscreen = AddBookWidget()


    def deletebook(self):

        self.newscreen2 = DeleteBookWidget()


    def update(self):

        self.newscreen3 = UpdateBookWidget()


    def about(self):

        buttonReply = QtWidgets.QMessageBox.information(self, "Program Hakkında", "Bu Program Erhan Yaylalı Tarafından Yazılmıştır.\nÖneri ve Şikayet bildirileri için erhanyaylali9@gmail.com\nadresine mail atabilirsiniz.", QtWidgets.QMessageBox.Ok)


class Widget1(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()
        self.ui()


    def ui(self):


        table11 = QtWidgets.QLabel("Kitabın Adı")
        table21 = QtWidgets.QLabel("Kitabın Yazarı")
        table31 = QtWidgets.QLabel("Kitabın Yayınevi")
        table41 = QtWidgets.QLabel("Kitabın Sayfa Sayısı")

        self.con = sqlite3.connect("database.db")
        self.cursor = self.con.cursor()
        self.cursor.execute("SELECT * FROM LIBRARY")
        self.datas = self.cursor.fetchall()

        no = len(self.datas)

        self.text2 = QtWidgets.QLabel("Kitap Ara")
        self.text = QtWidgets.QLineEdit()

        self.button = QtWidgets.QPushButton("Ara")
        self.button.clicked.connect(self.arama)

        self.button2 = QtWidgets.QPushButton("Temizle")
        self.button2.clicked.connect(self.clear)

        self.button3 = QtWidgets.QPushButton("Yenile")
        self.button3.clicked.connect(self.refresh)

        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(self.text2)
        hbox.addWidget(self.text)
        hbox.addWidget(self.button)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)


        self.table = QtWidgets.QTableWidget()
        self.table.setRowCount(no)
        self.table.setColumnCount(4)
        self.table.setColumnWidth(0,192)
        self.table.setColumnWidth(1,192)
        self.table.setColumnWidth(2,191)
        self.table.setColumnWidth(3,190)

        for i in range(0,no):
            self.table.setItem(i, 0, QtWidgets.QTableWidgetItem(self.datas[i][0]))
            self.table.setItem(i, 1, QtWidgets.QTableWidgetItem(self.datas[i][1]))
            self.table.setItem(i, 2, QtWidgets.QTableWidgetItem(self.datas[i][2]))
            self.table.setItem(i, 3, QtWidgets.QTableWidgetItem(str(self.datas[i][3])))

        hbox2 = QtWidgets.QVBoxLayout()
        hbox2.addWidget(self.table)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)

        self.setLayout(vbox)
        self.show()


    def arama(self):

        isim = self.text.text()

        self.cursor.execute("SELECT * FROM LIBRARY WHERE NAME = ? OR  AUTHOR = ?",(isim,isim))
        data = self.cursor.fetchall()

        no = len(data)
        self.table.setRowCount(no)

        for i in range(0,no):
            self.table.setItem(i, 0, QtWidgets.QTableWidgetItem(data[i][0]))
            self.table.setItem(i, 1, QtWidgets.QTableWidgetItem(data[i][1]))
            self.table.setItem(i, 2, QtWidgets.QTableWidgetItem(data[i][2]))
            self.table.setItem(i, 3, QtWidgets.QTableWidgetItem(str(data[i][3])))


    def clear(self):

        self.cursor.execute("SELECT * FROM LIBRARY")
        self.datas = self.cursor.fetchall()
        no = len(self.datas)

        self.text.clear()

        self.table.setRowCount(no)

        for i in range(0,no):
            self.table.setItem(i, 0, QtWidgets.QTableWidgetItem(self.datas[i][0]))
            self.table.setItem(i, 1, QtWidgets.QTableWidgetItem(self.datas[i][1]))
            self.table.setItem(i, 2, QtWidgets.QTableWidgetItem(self.datas[i][2]))
            self.table.setItem(i, 3, QtWidgets.QTableWidgetItem(str(self.datas[i][3])))


    def refresh(self):

        self.cursor.execute("SELECT * FROM LIBRARY")
        self.datas = self.cursor.fetchall()
        no = len(self.datas)

        self.table.setRowCount(no)

        for i in range(0,no):
            self.table.setItem(i, 0, QtWidgets.QTableWidgetItem(self.datas[i][0]))
            self.table.setItem(i, 1, QtWidgets.QTableWidgetItem(self.datas[i][1]))
            self.table.setItem(i, 2, QtWidgets.QTableWidgetItem(self.datas[i][2]))
            self.table.setItem(i, 3, QtWidgets.QTableWidgetItem(str(self.datas[i][3])))


class AddBookWidget(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()
        self.ui()


    def ui(self):

        id = QtWidgets.QLabel("Kitabın Adı:")
        self.id_text = QtWidgets.QLineEdit()
        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(id)
        hbox.addWidget(self.id_text)

        author = QtWidgets.QLabel("Kitabın Yazarı:")
        self.author_text = QtWidgets.QLineEdit()
        hbox2 = QtWidgets.QHBoxLayout()
        hbox2.addWidget(author)
        hbox2.addWidget(self.author_text)

        editor = QtWidgets.QLabel("Kitabın Yayınevi:")
        self.editor_text = QtWidgets.QLineEdit()
        hbox3 = QtWidgets.QHBoxLayout()
        hbox3.addWidget(editor)
        hbox3.addWidget(self.editor_text)

        page = QtWidgets.QLabel("Kitabın Sayfa Sayısı:")
        self.page_text = QtWidgets.QLineEdit()
        hbox4 = QtWidgets.QHBoxLayout()
        hbox4.addWidget(page)
        hbox4.addWidget(self.page_text)

        self.button = QtWidgets.QPushButton("Ekle")
        self.button.clicked.connect(self.add)
        hbox5 = QtWidgets.QHBoxLayout()
        hbox5.addStretch()
        hbox5.addWidget(self.button)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)

        self.setWindowTitle("Kitap Ekleme")
        self.setLayout(vbox)
        self.show()


    def add(self):

        name = self.id_text.text()
        author = self.author_text.text()
        editor = self.editor_text.text()
        page = self.page_text.text()

        self.con = sqlite3.connect("database.db")
        self.cursor = self.con.cursor()
        self.cursor.execute("INSERT INTO LIBRARY VALUES (?,?,?,?)",(name,author,editor,page))
        self.con.commit()
        buttonReply = QtWidgets.QMessageBox.information(self,'Success', "Kitap Başarıyla Eklendi",QtWidgets.QMessageBox.Yes)

        if buttonReply == QtWidgets.QMessageBox.Yes:

            self.hide()


class DeleteBookWidget(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()
        self.ui()


    def ui(self):

        id = QtWidgets.QLabel("Silmek İstediğiniz Kitabı Bulunuz:")
        self.id_text = QtWidgets.QLineEdit()

        self.button = QtWidgets.QPushButton("Bul")
        self.button.clicked.connect(self.find)


        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(id)
        hbox.addWidget(self.id_text)
        hbox.addWidget(self.button)

        self.setWindowTitle("Kitap Silme")
        self.setLayout(hbox)
        self.show()


    def find(self):

        name = self.id_text.text()
        self.con = sqlite3.connect("database.db")
        self.cursor = self.con.cursor()
        self.cursor.execute("SELECT * FROM LIBRARY WHERE NAME = ?",(name,))

        list = self.cursor.fetchall()

        if len(list) != 0:

            buttonReply = QtWidgets.QMessageBox.question(self,'Delete', "Silmek İstediğinize Emin Misiniz?\n{}  {}  {}  {}\t\n".format(list[0][0],list[0][1],list[0][2],list[0][3]), QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)

            if buttonReply == QtWidgets.QMessageBox.Yes:
                self.cursor.execute("DELETE FROM LIBRARY WHERE NAME = ?",(name,))
                self.con.commit()
                buttonReply2 = QtWidgets.QMessageBox.information(self,"Success","Başarıyla Silindi",QtWidgets.QMessageBox.Ok)

                if buttonReply2 == QtWidgets.QMessageBox.Ok:
                    self.hide()

        else:

            buttonReply = QtWidgets.QMessageBox.warning(self,"ERROR","Böyle Bir Kitap Bulunamadı.",QtWidgets.QMessageBox.Ok)

            if buttonReply == QtWidgets.QMessageBox.Ok:
                self.hide()


class UpdateBookWidget(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()
        self.ui()


    def ui(self):

        id = QtWidgets.QLabel("Güncellemek İstediğiniz Kitabı Bulunuz:")
        self.id_text = QtWidgets.QLineEdit()

        self.button = QtWidgets.QPushButton("Bul")
        self.button.clicked.connect(self.find)


        hbox0 = QtWidgets.QHBoxLayout()
        hbox0.addWidget(id)
        hbox0.addWidget(self.id_text)
        hbox0.addWidget(self.button)

        self.setWindowTitle("Kitap Güncelleme")
        self.setLayout(hbox0)
        self.show()


    def find(self):

        name = self.id_text.text()
        self.con = sqlite3.connect("database.db")
        self.cursor = self.con.cursor()
        self.cursor.execute("SELECT * FROM LIBRARY WHERE NAME = ?",(name,))
        list = self.cursor.fetchall()



        if len(list) != 0:

            self.newscreen4 = UpdateBookWidget2()
            self.newscreen4.realname = name

            print("{},{},{},{}".format(list[0][0],list[0][1],list[0][2],list[0][3]))
            self.newscreen4.text1.setText(list[0][0])
            self.newscreen4.text2.setText(list[0][1])
            self.newscreen4.text3.setText(list[0][2])
            self.newscreen4.text4.setText(str(list[0][3]))

            if self.newscreen4.hide:
                self.hide()


        else:

            buttonReply = QtWidgets.QMessageBox.warning(self,"Error","Böyle Bir Kitap Bulunamadı.",QtWidgets.QMessageBox.Ok)

            if buttonReply == QtWidgets.QMessageBox.Ok:
                self.hide()


class UpdateBookWidget2(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()
        self.ui()


    def ui(self):

        self.realname = ""
        self.label0 = QtWidgets.QLabel()
        hbox0 = QtWidgets.QHBoxLayout()
        hbox0.addWidget(self.label0)

        self.label1 = QtWidgets.QLabel("Kitabın Adı")
        self.text1 = QtWidgets.QLineEdit()
        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(self.label1)
        hbox.addWidget(self.text1)

        self.label2 = QtWidgets.QLabel("Kitabın Yazarı")
        self.text2 = QtWidgets.QLineEdit()
        hbox2 = QtWidgets.QHBoxLayout()
        hbox2.addWidget(self.label2)
        hbox2.addWidget(self.text2)

        self.label3 = QtWidgets.QLabel("Kitabın Yayınevi")
        self.text3 = QtWidgets.QLineEdit()
        hbox3 = QtWidgets.QHBoxLayout()
        hbox3.addWidget(self.label3)
        hbox3.addWidget(self.text3)

        self.label4 = QtWidgets.QLabel("Kitabın Sayfa Sayısı")
        self.text4 = QtWidgets.QLineEdit()
        hbox4 = QtWidgets.QHBoxLayout()
        hbox4.addWidget(self.label4)
        hbox4.addWidget(self.text4)

        button = QtWidgets.QPushButton("Güncelle")
        button.clicked.connect(self.update)
        hbox5 = QtWidgets.QHBoxLayout()
        hbox5.addWidget(button)

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addLayout(hbox0)
        self.vbox.addLayout(hbox)
        self.vbox.addLayout(hbox2)
        self.vbox.addLayout(hbox3)
        self.vbox.addLayout(hbox4)
        self.vbox.addLayout(hbox5)

        self.setLayout(self.vbox)
        self.show()

    def update(self):

        isim = self.text1.text()
        yazar = self.text2.text()
        yayınevi = self.text3.text()
        sayfa = self.text4.text()

        self.con = sqlite3.connect("database.db")
        self.cursor = self.con.cursor()
        self.cursor.execute("Update LIBRARY set NAME = ?,AUTHOR = ?,EDITOR = ?, PAGE = ? where NAME = ?", (isim,yazar,yayınevi,sayfa,self.realname))
        self.con.commit()

        buttonReply = QtWidgets.QMessageBox.information(self, "Success", "Güncelleme İşlemi Başarıyla Tamamlandı.", QtWidgets.QMessageBox.Ok)

        if buttonReply == QtWidgets.QMessageBox.Ok:
            self.hide()







app = QtWidgets.QApplication(sys.argv)
uygulama = Pencere()
sys.exit(app.exec_())