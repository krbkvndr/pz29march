from PyQt5 import QtWidgets
from pz29_2 import Ui_MainWindow
import sys
import matplotlib.pyplot as plt
import math

class my_win(QtWidgets.QMainWindow):
    def __init__(self):
        super(my_win, self).__init__() #Наследование аттрибутов из QMainWindow
        self.ui = Ui_MainWindow() #Создание ui
        self.ui.setupUi(self) #Запуск преднастройки
        self.ui.pushButton.clicked.connect(self.btnClicked) #Триггер при нажатии (функция кнопка)



    def btnClicked(self): #Что она делает
        try:
            amplituda = float(self.ui.lineEdit.text())
            chastota = float(self.ui.lineEdit_2.text())
            faza = float(self.ui.lineEdit_3.text())

            sum_t = 100

        
            S=[]

            for t in range(int(sum_t)):
                s = amplituda * math.sin(chastota * t + math.radians(faza))

                S.append(s)


        
            plt.plot(S)
            plt.draw()
            plt.show()

        except ValueError:
            text = self.ui.lineEdit.text()
            text = self.ui.lineEdit_2.text()



app = QtWidgets.QApplication([])
window = my_win()
window.show()

sys.exit(app.exec())
