from PyQt5 import QtWidgets
from pz29 import Ui_MainWindow
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
            v0 = float(self.ui.lineEdit.text())
            phi = float(self.ui.lineEdit_2.text())
            g = 10
            t_padenia = (2 * v0 * math.sin(math.radians(phi))) / g

        
            X=[]
            Y=[]
            for t in range(int(t_padenia)):
                x = v0 * t * math.cos(math.radians(phi))
                y = v0 * t * math.sin(math.radians(phi)) - (g * t * t) / 2
                X.append(x)
                Y.append(y)

        
            plt.plot(X, Y)
            plt.draw()
            plt.show()

        except ValueError:
            text = self.ui.lineEdit.text()
            text = self.ui.lineEdit_2.text()



app = QtWidgets.QApplication([])
window = my_win()
window.show()

sys.exit(app.exec())
