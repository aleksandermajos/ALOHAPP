import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt6.QtGui import QPixmap, QAction, QIcon
from PyQt6.QtCore import Qt



class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        icon = QIcon("../DATA/PIC/ALOHA.jpg")
        self.setWindowIcon(icon)
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(50,50,250,400)
        self.setWindowTitle("ALOHAPP!")

        self.setUpMainWindow()

        self.lbl = QLabel(self)
        qle = QLineEdit(self)
        qle.move(60, 100)
        self.lbl.move(60, 40)
        qle.textChanged[str].connect(self.onChanged)

        self.show()

    def setUpMainWindow(self):
        self.times_pressed_buttonrec = 1

        self.buttonrec = QPushButton("PUSH TO RECORD", self)
        self.buttonrec.move(80, 70)
        self.buttonrec.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        self.times_pressed_buttonrec += 1
        if (self.times_pressed_buttonrec % 2) != 0:
            self.buttonrec.setText("START RECORDING")
            self.buttonrec.adjustSize()
        if (self.times_pressed_buttonrec % 2) == 0:
            self.buttonrec.setText("STOP RECORDING")
            self.buttonrec.adjustSize()

    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

    def createImageLabel(self):
        images = ["../DATA/PIC/ALOHA.jpg"]

        for image in images:
            try:
                with open(image):
                    label = QLabel(self)
                    pixmap = QPixmap(image)
                    label.setPixmap(pixmap)
            except FileNotFoundError as error:
                print(f"Image not found.\nError: {error}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
