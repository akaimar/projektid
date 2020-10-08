import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from fbs_runtime.application_context.PyQt5 import ApplicationContext
import finviz
from datetime import datetime

#app .exe file is compled by using fbs # pip install fbs
#app new project C:\Users\aimar.roosalu\AppData\Roaming\Python\Python37\Scripts\ ### fbs startproject
#app main.py location: C:\Users\aimar.roosalu\AppData\Roaming\Python\Python37\Scripts\target\MyApp
#app compile C:\Users\aimar.roosalu\AppData\Roaming\Python\Python37\Scripts\ ### fbs freeze to complie to .exe
#produced by Aimar Roosalu 04/2020 aimar.roosalu@gmail.com

hor = 10
ver = 50
hor1 = hor+70

class Window(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100, 100, 300, 550)
        self.setWindowTitle("Kasumi kalkulaator")
        self.setWindowIcon(QtGui.QIcon('icon.png')) # tuli importida QtGui
        
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
        self.ticker = QtWidgets.QLineEdit(self)
        self.ticker.resize(100, 20)
        self.ticker.move(80, 30)
        self.ticker.editingFinished.connect(self.aktsiahind)
 
        self.ostuhind = QtWidgets.QDoubleSpinBox(self)
        self.ostuhind.setSingleStep(0.01)
        self.ostuhind.setMaximum(99999)
        self.ostuhind.resize(100, 20)
        self.ostuhind.move(80, 55)
        
        self.ostukogus = QtWidgets.QSpinBox(self)
        self.ostukogus.resize(100, 20)
        self.ostukogus.move(80, 80)
        
        self.myygihind = QtWidgets.QDoubleSpinBox(self)
        self.myygihind.setSingleStep(0.01)
        self.myygihind.setMaximum(99999)
        self.myygihind.resize(100, 20)
        self.myygihind.move(80, 105)
        
        self.myygikogus = QtWidgets.QSpinBox(self)
        self.myygikogus.resize(100, 20)
        self.myygikogus.move(80, 130)
        
        self.ostukulu = QtWidgets.QDoubleSpinBox(self)
        self.ostukulu.setSingleStep(0.01)
        self.ostukulu.resize(100, 20)
        self.ostukulu.move(80, 155)

        self.myygikulu = QtWidgets.QDoubleSpinBox(self)
        self.myygikulu.setSingleStep(0.01)
        self.myygikulu.resize(100, 20)
        self.myygikulu.move(80, 180)
        
        # Button
        btn = QtWidgets.QPushButton("Arvuta", self)
        btn.resize(50, 25)
        btn.move(80, 210)
        btn.clicked.connect(self.arvuta)
        
        # INFOTAHVLI VÄLJUNDID
        
        # test label, mis tegelikult läheb üles ostuhinna widgetisse
        self.print_0l = QtWidgets.QLabel("Aktsiahind:", self)
        self.print_0l.move(10, 275)
        
        self.print_aktsiahind = QtWidgets.QLabel(self)
        self.print_aktsiahind.move(hor+hor1, 275)

        self.print_1l = QtWidgets.QLabel("Kogukulu: ", self)
        self.print_1l.move(10, 300)

        self.print_kogukulu = QtWidgets.QLabel(self)
        self.print_kogukulu.move(hor+hor1, 50+245)

        self.print_2l = QtWidgets.QLabel("Kasum: ", self)
        self.print_2l.move(10, 325)
        
        self.print_kasum = QtWidgets.QLabel(self)
        self.print_kasum.move(hor+hor1, 50+270)
        
        self.print_3l = QtWidgets.QLabel("Tehingukulu: ", self)
        self.print_3l.move(10, 350)
        
        self.print_kulu = QtWidgets.QLabel(self)
        self.print_kulu.move(hor+hor1, 50+295)
        
        self.print_4l = QtWidgets.QLabel("Breakeven: ", self)
        self.print_4l.move(10, 375)
        
        self.print_breakeven = QtWidgets.QLabel(self)
        self.print_breakeven.move(hor+hor1, 50+320)
    
        
        #COPYRIGHT        
        self.print_copyright = QtWidgets.QLabel("(C) 2020 A.R.", self)
        self.print_copyright.move(10, 50+400)
    
        self.show()

#FUNKTSIOONID aka MEETODID
        
    # finviz api kaudu viimane hind (15 min delay)
    def aktsiahind(self):
        if self.ticker.text() == "": #validaator, et väli ei oleks tühi ja errori vältimiseks
            self.print_aktsiahind.setText("Sisesta ticker")
        else:    
            stock = finviz.get_stock(self.ticker.text())
            self.ostuhind.setValue(float(stock['Price'])) #prindime välja ostuhinna väljale, tuleb konverteerida komakohtadeks
            self.print_aktsiahind.setText(str(stock['Price'])) #prindime ka alla infotahvlile

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
    app.setStyle(QtWidgets.QStyleFactory.create('fusion'))
    GUI = Window()
    app.exec_()

run()



