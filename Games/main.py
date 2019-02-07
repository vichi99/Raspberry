from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)

        self.windowTitleChanged.connect(lambda x: self.test(x , 9))
        self.setWindowTitle("My App")

        label = QLabel("Nice")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

    def onWindowTitleChange(self, s):
        print(s)

    def test(self, a ="hello", b=7):
        print(a, b)

app = QApplication(sys.argv)
Window = MainWindow()



Window.show()
app.exec_()
