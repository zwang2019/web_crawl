from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QStatusBar, QHBoxLayout, QVBoxLayout, \
    QGridLayout, QFormLayout, QPushButton, QLineEdit, QLabel
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
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

        central_widget = QWidget()
        self.setCentralWidget(central_widget)


        # hbox = QHBoxLayout()
        main_layout = QVBoxLayout()
        grid = QGridLayout()
        form = QFormLayout()

        btn = QPushButton("1")
        btn_2 = QPushButton("2")
        btn_3 = QPushButton("3")
        btn_4 = QPushButton("4")
        btn_5 = QPushButton("5")
        btn_6 = QPushButton("6")

        grid.addWidget(btn, 0, 0)
        grid.addWidget(btn_2, 0, 1)
        grid.addWidget(btn_3, 1, 0)
        grid.addWidget(btn_4, 1, 1)
        grid.addWidget(btn_5, 2, 0)
        grid.addWidget(btn_6, 2, 1)
        # hbox.setAlignment(Qt.AlignmentFlag.AlignBottom)



        self.line = QLineEdit()
        self.line.setFixedSize(200, 30)
        self.line.setPlaceholderText('input the account')
        self.line.setClearButtonEnabled(True)

        self.line_2 = QLineEdit()
        self.line_2.setFixedSize(200, 30)
        self.line_2.setPlaceholderText('input the password')
        self.line_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.line_2.setClearButtonEnabled(True)

        btn_sub = QPushButton("Submit")
        btn_sub.setFixedWidth(200)
        btn_sub.clicked.connect(self.buttonclick)

        # form.setAlignment(Qt.AlignmentFlag.AlignLeft)
        form.addRow("Account:", self.line)
        form.addRow("Password:", self.line_2)
        form.addRow("Submit:", btn_sub)

        main_layout.addLayout(form)
        main_layout.addLayout(grid)
        central_widget.setLayout(main_layout)

    def buttonclick(self):

        data = {
            "account": self.line.text(),
            "password": self.line_2.text()
        }

        print(data)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyWindow()

    window.show()

    sys.exit(app.exec())


