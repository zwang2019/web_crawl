from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QStatusBar, QLineEdit, QLabel, QPushButton, QListWidget
from PyQt6.QtGui import QIcon
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

        self.initui()



    def initui(self):

        label_1 = QLabel("account", self)
        label_1.move(200, 300)
        line = QLineEdit(self)
        line.move(300, 300)
        line.resize(200, 30)
        line.setPlaceholderText('input the account')
        line.setClearButtonEnabled(True)

        label_2 = QLabel("password", self)
        label_2.move(200, 400)
        line_2 = QLineEdit(self)
        line_2.move(300, 400)
        line_2.resize(200, 30)
        line_2.setPlaceholderText('input the password')
        line_2.setEchoMode(QLineEdit.EchoMode.Password)
        line_2.setClearButtonEnabled(True)

        btn = QPushButton("OK", self)
        btn.setGeometry(550, 350, 100, 30)
        btn.clicked.connect(self.onbuttonclick)


        listWidget_1 = QListWidget(self)
        listWidget_1.setGeometry(200, 500, 500, 500)
        listWidget_1.addItem("python")
        listWidget_1.addItem("java")
        listWidget_1.addItem("c++")
        listWidget_1.addItem("c#")
        listWidget_1.addItem("javascript")

        listWidget_1.clicked.connect(self.listwidgetclick)

        self.list_label = QLabel("", self)

    def onbuttonclick(self):
        print('button click')

    def listwidgetclick(self, item):
        print(item.data())
        self.list_label.setText(item.data())
        self.list_label.move(800, 500)





if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyWindow()

    window.show()

    sys.exit(app.exec())

