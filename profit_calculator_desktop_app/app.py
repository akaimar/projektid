import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from fbs_runtime.application_context.PyQt5 import ApplicationContext
import finviz
from datetime import datetime

#KASUTATUD DOKUMENTATSIOON:
#https://www.riverbankcomputing.com/static/Docs/PyQt5/index.html
#Finviz API dokumentatsioon: https://github.com/mariostoev/finviz

#JUHIS KUIDAS GENEREERIDA antud python koodist .EXE laiendiga Windosi süsteemidele töötav rakendus
#app .exe file kompileeritakse kasutades fbs moodulit - fbs # pip install fbs
#app vali õige path projekti jaoks C:\Users\aimar.roosalu\AppData\Roaming\Python\Python37\Scripts\ ### fbs startproject
#app main.py location: C:\Users\aimar.roosalu\AppData\Roaming\Python\Python37\Scripts\target\MyApp
#app kompileerime C:\Users\aimar.roosalu\AppData\Roaming\Python\Python37\Scripts\ ### fbs freeze et kompileerida .exe fail
#selle koodi autor on Aimar Roosalu 11/2020 aimar.roosalu@gmail.com

#erinevate widgetite koordinaadid
hor = 10
hor1 = hor+70

class Window(QtWidgets.QMainWindow): #akna konteiner
    
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(200, 200, 300, 550)
        self.setWindowTitle("Kasumi kalkulaator")
        self.setWindowIcon(QtGui.QIcon('icon.png')) # tuli importida QtGui, et saada ikoon
        
        self.home()

    def home(self):
        
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")    
        
        #<------ LABELID ----->
        
        # ticker
        self.ticker = QtWidgets.QLabel("Ticker:", self)
        self.ticker.move(10, 25)
              
        # ostuhind
        self.ostuhind = QtWidgets.QLabel("Ostuhind:", self)
        self.ostuhind.move(10, 50)
        
        # ostukogus
        self.ostukogus = QtWidgets.QLabel("Ostukogus:", self)
        self.ostukogus.move(10, 75)
        
        # myygihind
        self.myygihind = QtWidgets.QLabel("Müügihind:", self)
        self.myygihind.move(10, 100)
        
        # myygikogus
        self.myygikogus = QtWidgets.QLabel("Müügikogus:", self)
        self.myygikogus.move(10, 125)
        
        # ostukulu
        self.ostukulu = QtWidgets.QLabel("Ostukulu:", self)
        self.ostukulu.move(10, 150)
        
        # müügikulu
        self.myygikulu = QtWidgets.QLabel("Müügikulu:", self)
        self.myygikulu.move(10, 175)
        
 
        # <!---- WIDGETID ----->
        self.ticker = QtWidgets.QLineEdit("", self)
        self.ticker.resize(100, 20)
        self.ticker.move(100, 30)
        self.ticker.editingFinished.connect(self.aktsiahind) #Kui siit kastist väljuda, käivitub funktsioon "aktsiahind"
 
        self.ostuhind = QtWidgets.QDoubleSpinBox(self)
        self.ostuhind.setSingleStep(0.01)
        self.ostuhind.setMaximum(99999)
        self.ostuhind.resize(100, 20)
        self.ostuhind.move(100, 55)
        
        self.ostukogus = QtWidgets.QSpinBox(self)
        self.ostukogus.resize(100, 20)
        self.ostukogus.move(100, 80)
        
        self.myygihind = QtWidgets.QDoubleSpinBox(self)
        self.myygihind.setSingleStep(0.01)
        self.myygihind.setMaximum(99999)
        self.myygihind.resize(100, 20)
        self.myygihind.move(100, 105)
        
        self.myygikogus = QtWidgets.QSpinBox(self)
        self.myygikogus.resize(100, 20)
        self.myygikogus.move(100, 130)
        
        self.ostukulu = QtWidgets.QDoubleSpinBox(self)
        self.ostukulu.setSingleStep(0.01)
        self.ostukulu.resize(100, 20)
        self.ostukulu.move(100, 155)

        self.myygikulu = QtWidgets.QDoubleSpinBox(self)
        self.myygikulu.setSingleStep(0.01)
        self.myygikulu.resize(100, 20)
        self.myygikulu.move(100, 180)
        
        # Button
        btn = QtWidgets.QPushButton("Arvuta", self)
        btn.resize(50, 25)
        btn.move(100, 210)
        btn.clicked.connect(self.arvuta)
        
        # INFOTAHVLI VÄLJUNDID
        
        # test label, mis tegelikult läheb üles ostuhinna widgetisse
        self.print_0l = QtWidgets.QLabel("Aktsiahind:", self)
        self.print_0l.move(10, 275)
        
        self.print_aktsiahind = QtWidgets.QLabel(self)
        self.print_aktsiahind.setGeometry(QtCore.QRect(hor+hor1, 285, 200, 10))

        self.print_1l = QtWidgets.QLabel("Kogukulu: ", self)
        self.print_1l.move(10, 300)

        self.print_kogukulu = QtWidgets.QLabel(self)
        self.print_kogukulu.move(hor+hor1, 50+250)

        self.print_2l = QtWidgets.QLabel("Kasum: ", self)
        self.print_2l.move(10, 325)
        
        self.print_kasum = QtWidgets.QLabel(self)
        self.print_kasum.move(hor+hor1, 50+275)
        
        self.print_3l = QtWidgets.QLabel("Tehingukulu: ", self)
        self.print_3l.move(10, 350)
        
        self.print_kulu = QtWidgets.QLabel(self)
        self.print_kulu.move(hor+hor1, 50+300)
        
        self.print_4l = QtWidgets.QLabel("Breakeven: ", self)
        self.print_4l.move(10, 375)
        
        self.print_breakeven = QtWidgets.QLabel(self)
        self.print_breakeven.move(hor+hor1, 50+325)
    
        
        #COPYRIGHT        
        self.print_copyright = QtWidgets.QLabel("__________________________________\nCopyright 2020 A.R.\nSisesta aktsia lühend (nt. AAPL).\nHind tuleb turult automaatselt ja \non 15 min. viitajaga.", self)
        self.print_copyright.setGeometry(QtCore.QRect(10, 450, 300, 100))
        self.show()

#FUNKTSIOONID
         
    # finviz api kaudu viimane hind (15 min delay)
    def aktsiahind(self):

        #valideerimine - lubatud sümbolid tickeri jaoks
        lubatud = {'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z'}

        kontroll_string = self.ticker.text()
        if lubatud.issuperset(kontroll_string) == True: #kui sisestatud sümbol vastab tingimustele, peab sisaldama ainult lubatud tähti
            
            try: 
                stock = finviz.get_stock(self.ticker.text())
                self.ostuhind.setValue(float(stock['Price'])) #prindime välja ostuhinna väljale, tuleb konverteerida komakohtadeks
                self.print_aktsiahind.setText(str(stock['Price'])) #prindime ka alla infotahvlile
            except:
                self.print_aktsiahind.setText(str("Sellist aktsiat ei ole!")) #prindime ka alla infotahvlile
        
        else:
            self.print_aktsiahind.setText(str("Lubatud ainult tähed!")) #prindime ka alla infotahvlile

    # arvutused infotahvlile
    def arvuta(self):
        a = self.ostuhind.value()
        b = self.ostukogus.value()
        c = self.myygihind.value()
        d = self.myygikogus.value()
        e = self.ostukulu.value()
        f = self.myygikulu.value()
        
        #arvutused ja ümardame kahe komakohani 
        kogukulu = round(a * b, 2)
        kulu = round((e + f) * d, 2)
        kasum = round((c * d) - (a * b) - kulu, 2)
        
        if b == 0: #nulliga jagamise errori lahendamine
            breakeven = 0
        else:
            breakeven = round((kulu / b) + a, 2) # ((ostukulu + müügikulu) / ostukogus) + ostuhind
        
        #muudame labelil teksti
        self.print_kogukulu.setText(str(kogukulu))
        self.print_kasum.setText(str(kasum))
        self.print_kulu.setText(str(kulu))
        self.print_breakeven.setText(str(breakeven))

#mainloop
def run():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('fusion')) #akna stiiliks on "fusion"
    GUI = Window()
    app.exec_()

run()




