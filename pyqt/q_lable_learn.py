from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QStatusBar, QLabel
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
import sys


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QT Learn")
        self.setWindowIcon(QIcon(r"./icon/spider.png"))
        self.setGeometry(200, 200, 1920, 1080)

        self.setStyleSheet('background-color: #81D8CF')

        self.statusBar().showMessage("Spyder Learn")
        file = self.menuBar().addMenu("File")
        file.addAction("Open")
        save = file.addMenu("Save")
        save.addAction("Save")
        save.addAction("Save As")
        file.addAction("Exit")
        self.menuBar().addMenu("Edit")
        self.menuBar().addMenu("Help")

        #######
        self.label = QLabel('', self)
        self.label.move(100, 100)
        self.label.resize(300, 168)
        #self.label.setText("中文")
        #self.label.setFont(QFont("Kaiti", 20))
        self.label.setPixmap(QPixmap(r"./icon/snake.jpg"))

        label_2 = QLabel('', self)
        label_2.move(500, 100)
        label_2.resize(160, 117)
        movie_kongfu = QMovie(r"./icon/kongfu.gif")
        movie_kongfu.setSpeed(168)
        label_2.setMovie(movie_kongfu)
        movie_kongfu.start()





if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyWindow()

    window.show()

    sys.exit(app.exec())


