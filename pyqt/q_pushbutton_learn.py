from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QStatusBar, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize
import sys


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QT Learn")
        self.setWindowIcon(QIcon(r"./icon/spider.png"))
        self.setGeometry(200, 200, 1920, 1080)

        # self.setStyleSheet('background-color: #81D8CF')

        self.statusBar().showMessage("Spyder Learn")
        file = self.menuBar().addMenu("File")
        file.addAction("Open")
        save = file.addMenu("Save")
        save.addAction("Save")
        save.addAction("Save As")
        file.addAction("Exit")
        self.menuBar().addMenu("Edit")
        self.menuBar().addMenu("Help")

        self.creat_button()



    def creat_button(self):
        btn = QPushButton('Click', self)
        btn.setGeometry(100, 100, 200, 50)


        btn.setFont(QFont('Times New Roman', 20, QFont.Weight.Bold))

        btn.setIcon(QIcon(r"./icon/snake.jpg"))
        btn.setIconSize(QSize(60, 34))



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyWindow()

    window.show()

    sys.exit(app.exec())
