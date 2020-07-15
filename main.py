import sqlite3 as sql
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QPushButton, QMessageBox, QWidget, QDesktopWidget, QPlainTextEdit
import sys
import subprocess

modules = ["Seçiniz","math","re"]
fileExists = os.path.exists("main.dbdb")
db = sql.connect("main.dbdb")
cr = db.cursor()

cr.execute("""CREATE TABLE IF NOT EXISTS math (function,english,turkish,example)""")
cr.execute("""CREATE TABLE IF NOT EXISTS re (function,english,turkish,example)""")

if not fileExists:
    dataMath = [("ceil","Return the ceiling of x as an Integral. This is the smallest integer >= x.","Verilen Ondalıklı Sayıyı Bir Üstündeki Tam Sayıya Çevirir.","import math\nnum = 15\nnum_sqrt=math.sqrt(num)\nprint(num)\nprint(num_sqrt)"),
                ("fabs","Return the absolute value of the float x.","Değerin Mutlak Değerini Alır ve Ondalıklı Sayı Olarak Döndürür.","import math\n"),
                ("factorial","Find x!. Raise a ValueError if x is negative or non-integral.","Pozitif Değeri Faktöriyelini Alır.Negatif Değerde 'ValueError' Hatası Verir.","import math\n"),
                ("floor","Return the floor of x as an Integral. This is the largest integer <= x.","Verilen Ondalıklı Sayıyı Bir Altındaki Tam Sayıya Çevirir.","import math\n"),
                ("cos","Return the cosine of x (measured in radians).","Radyan cinsinden verilen parametrenin kosinüsünü hesaplar.","import math\n"),
                ("trunc","Truncates the Real x to the nearest Integral toward 0.","Ondalıklı Sayıyı En Yakın Tam Sayıya Çevirir.","import math\n"),
                ("exp","Return e raised to the power of x.","e lerin sabitinin kuvvetini alır.","import math\n"),
                ("radians","Convert angle x from degrees to radians.","Verilen sayıyı dereceden radyana çevirir.","import math\n"),
                ("degrees","Convert angle x from radians to degrees.","Verilen sayıyı radyandan dereceye çevirir.","import math\n"),
                ("sqrt","Return the square root of x.","Verilen sayının karekökünü hesaplar.","import math\n"),
                ("pow","Return x**y (x to the power of y).","Birinci sayının ikinci sayıya göre kuvvetini alıyor.","import math\n"),
                ("log","log(x, [base=math.e]). Return the logarithm of x to the given base.","Birinci değerin ikinci değere göre logaritmasını hesaplar.","import math\n"),
                ("tan","Return the tangent of x (measured in radians).","Radyan cinsinden verilen parametrenin tanjantını hesaplar.","import math\n"),
                ("sin","Return the sine of x (measured in radians).","Radyan cinsinden verilen sayının sinüsünü hesaplar.","import math\n"),
                ("gcd","Greatest common divisor of x and y","Verilen iki sayının EBOB’unu veriyor.","import math\n"),
                ("tanh","Return the hyperbolic tangent of x.","Verilen değerin hiperbolik tanjantını döndürür.","import math\n"),
                ("sinh","Return the hyperbolic sine of x.","Verilen değerin hiperbolik sinüsünü döndürür.","import math\n"),
                ("cosh","Return the hyperbolic cosine of x.","Verilen değerin hiperbolik kosinüsünü döndürür.","import math\n"),
                ("hypot","Return the Euclidean distance, sqrt(x*x + y*y).","Değerleri (a,b) Dersek => sqrt(x*x+y*y) İşlemini Yapar.","import math\n"),
                ("copysign","Return a float with the magnitude (absolute value) of x but the sign of y.","İki Parametrenin (a,b) b'nin değeri a'ya geçer ve b sıfır değerini alır.","import math\n")]

    dataRe = [("endpos","Writes the Total Number of Characters in the Text, Including Line Jumps.","Metin İçerisindeki Karakterlerin Toplam Adedini Yazar.Satır Atlamalarıda Dahil.",""),
              ("findall","It shows how many times the word we look for in the text.","Metin İçerisinde Aradığımız Kelimenin Kaç Kere Geçtiğini Gösterir.",""),
              ("* Karakteri","Finds All Repetitions of the Statement.","İfadenin Tüm Tekrarlarını Bulur.",""),
              ("? Karakteri","It queries the word that comes before it to repeat 0 or 1 times.","Kendisinden Önce Gelen Kelimenin 0 veya 1 Kere Tekrar Etmesini Sorgular.1 den Fazla Olanları Yazdırmaz.",""),
              ("[] Karakteri","Queries All Characters Written Between Square Brackets.","Köşeli Parantez Arasına Yazılan Tüm Karakterleri Sorgular.",""),
              ("| Karakteri","'or' Means","'veya' Anlamına Gelir",""),
              ("( ) Karakterleri","Brackets are also used to group the patterns we wrote.","Parantez de yazdığımız kalıpları gruplamak için kullanılır.",""),
              ("(backslash)s İfadesi","Traps Space In Source.","Kaynaktaki Boşluğu Yakalar.",""),
              ("(backslash)S İfadesi","Captures Except Space.","Boşluk Haricindekileri Yakalar.",""),
              ("(backslash)d İfadesi","captures the number in the source.","Kaynaktaki sayıyı yakalar.",""),
              ("(backslash)D İfadesi","Catch Non-Number in Source.","Kaynaktaki Sayı Olmayanları Yakalar.",""),
              ("(backslash)w İfadesi","Catches Number and Underline.","Sayıyı ve altı çizgiyi Yakalar.",""),
              ("(backslashW İfadesi","Catches the Inverse ie Characters like space, point, question mark.","Boşluğu, noktayı, soru işareti gibi Karakterleri Yakalar.","")]

    datas = [dataMath,dataRe]
    c = 0
    
    for m in modules[1:]:
        for d in datas[c]:
            dbCommand  = """INSERT INTO """ + m + """ VALUES (?,?,?,?)"""
            cr.execute(dbCommand,d)
        c+=1
    c = 0
class Window(QMainWindow,QLabel):
    def __init__(self):
        super().__init__()

        self.combo1Example = ""
        self.a = 0
        self.b = 0
        self.spCommand = ""
        self.x = ""
        self.y = ""
        self.windowCenter()
        self.setWindowTitle("Proje")
        
        self.combo0 = QComboBox(self)
        
        for m in modules:
            self.combo0.addItem(m)
            
        self.combo0.setGeometry(30,30,100,45)
        self.combo0.activated[str].connect(self.activatedCombo0)

        self.combo1 = QComboBox(self)
        self.combo1.setGeometry(30,100,100,45)
        self.combo1.activated[str].connect(self.activatedCombo1)
        
        self.englishLabel = QLabel("",self)
        self.englishLabel.setGeometry(160,30,503,45)
        self.englishLabel.setStyleSheet("background-color: white")
        
        self.turkishLabel = QLabel("",self)
        self.turkishLabel.setGeometry(160,100,503,45)
        self.turkishLabel.setStyleSheet("background-color: white")
        
        self.textarea0 = QPlainTextEdit("",self)
        self.textarea0.resize(300,150)
        self.textarea0.move(30,175)
        self.textarea0.setPlaceholderText("Komut")

        self.textarea1 = QPlainTextEdit("",self)
        self.textarea1.resize(300,150)
        self.textarea1.move(360,175)
        self.textarea1.setPlaceholderText("Çıktı")
        self.textarea1.setReadOnly(True)
        
        self.button = QPushButton('Çalıştır', self)
        self.button.move(30,340)
        self.button.clicked.connect(self.clickedButton)
        
        self.show()

        for i in modules[1:]:
            try:
                self.spCommand = self.spCommand + "python -c \'" + "import " + i + "\'"
                subprocess.check_output(self.spCommand,shell=True, stderr=subprocess.STDOUT)
                self.spCommand = ""
            except:
                self.moduleError(i)
                self.spCommand = ""

    def activatedCombo0(self):
        if self.combo0.currentText() != "Seçiniz":
                self.combo1.clear()
                self.command0 = """SELECT function FROM """ + self.combo0.currentText()
                cr.execute(self.command0)
                for i in cr.fetchall():
                    self.combo1.addItem(str(i)[2:-3])
                    
        if self.combo0.currentText() == "Seçiniz":
            self.englishLabel.setText("")
            self.turkishLabel.setText("")
            self.combo1.clear()

    def activatedCombo1(self):
        if self.combo0.currentText() != "":
            self.command1a = """SELECT english FROM """ + self.combo0.currentText() + """ WHERE function= """ + "\'" + self.combo1.currentText() + "\'"
            cr.execute(self.command1a)
            self.combo1English = cr.fetchall()
            
            self.command1b = """SELECT turkish FROM """ + self.combo0.currentText() + """ WHERE function= """ + "\'" + self.combo1.currentText() + "\'"
            cr.execute(self.command1b)
            self.combo1Turkish = cr.fetchall()

            self.englishLabel.setText(str(self.combo1English)[3:-4])
            self.turkishLabel.setText(str(self.combo1Turkish)[3:-4])
            
            self.command1c = """SELECT example FROM """ + self.combo0.currentText() + """ WHERE function= """ + "\'"+self.combo1.currentText() + "\'"
            cr.execute(self.command1c)
            self.combo1ExampleCopy = str(cr.fetchall())[3:-4]
            
            for i in self.combo1ExampleCopy:
                self.a+=1
                if i == "\\" and self.combo1ExampleCopy[self.a] == "n" or i == "n" and self.combo1ExampleCopy[self.a-2] == "\\":
                    self.b+=1
                    if self.b%2 == 0:
                        self.b = 0
                        self.combo1Example = self.combo1Example + "\n"
                else:
                    self.combo1Example = self.combo1Example + i

            self.textarea0.setPlainText(self.combo1Example)
            self.combo1Example = ""
            self.a = 0
            

    def clickedButton(self):
        try:
            self.textarea1.clear()
            self.spCommand = self.spCommand + "python -c \'"
            for i in self.textarea0.document().toPlainText():
                if i == "\n":
                    self.spCommand = self.spCommand + ";"
                else:
                    self.spCommand = self.spCommand + i

            self.spCommand = self.spCommand + "\'"
            self.output = str(subprocess.check_output(self.spCommand,shell=True, stderr=subprocess.STDOUT))[2:-3]
            self.outputCopy = self.output
            self.output = ""
            for i in self.outputCopy:
                self.a+=1
                if i == "\\" and self.outputCopy[self.a] == "n" or i == "n" and self.outputCopy[self.a-2] == "\\":
                    self.b+=1
                    if self.b%2 == 0:
                        self.b = 0
                        self.output = self.output + "\n"
                else:
                    self.output = self.output + i
                    
            self.a = 0
            self.textarea1.insertPlainText(self.output)
            self.spCommand = ""

        except subprocess.CalledProcessError as e:
            self.errorOutput = str(e.output)[2:-3]
            self.errorOutputCopy = self.errorOutput
            self.errorOutput = ""
            for i in self.errorOutputCopy:
                self.a+=1
                if i == "\\" and self.errorOutputCopy[self.a] == "n" or i == "n" and self.errorOutputCopy[self.a-2] == "\\":
                    pass
                else:
                    self.errorOutput = self.errorOutput + i

            self.a = 0
            self.textarea1.clear()
            self.textarea1.insertPlainText(self.errorOutput)
            self.spCommand = ""
            self.errorOutput = ""

    def moduleError(self,m):
        QMessageBox.about(self,"Hata",m+" adlı modül bilgisayarınızda bulunmamaktadır.")

    def windowCenter(self):
        self.dtw = QDesktopWidget().availableGeometry().center()
        self.xy = str(self.dtw)[20:-1]
        for i in self.xy:
            if i == ",":
                break
            self.x = self.x + i
        self.y = self.xy[len(self.x)+2::]
        self.x = int(self.x)-345
        self.y = int(self.y)-200
                         
        self.setGeometry(self.x,self.y,690,400)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
