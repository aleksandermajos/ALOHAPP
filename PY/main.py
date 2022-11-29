import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt6.QtGui import QPixmap, QIcon
from ENGINE.PYAUDIO import Recorder
from ENGINE.ASR_WHISPER import WhisperModel
from ENGINE.PICGEN_STABLEDIFF import StableDiffiusion





class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        icon = QIcon("../DATA/PIC/ALOHA.jpg")
        self.setWindowIcon(icon)
        self.initializeAI()
        self.initializeUI()
    def initializeAI(self):
        self.whisper_model = WhisperModel(size='medium', lang='polish')
        self.recorder_model = Recorder(length=10, path="../DATA/PHRASES/SPEAKING/",file='polish666.wav')
        self.sd_model = StableDiffiusion(model_id="stabilityai/stable-diffusion-2")
    def initializeUI(self):
        self.setGeometry(50,50,250,400)
        self.setWindowTitle("ALOHAPP!")
        self.setUpMainWindow()

        self.lbl = QLabel(self)

        self.transcription_label = QLineEdit(self)
        self.transcription_label.move(60, 110)
        self.transcription_label.resize(140, 20)
        self.transcription_label.textChanged[str].connect(self.onChanged)

        self.translation_label = QLineEdit(self)
        self.translation_label.move(60, 150)
        self.translation_label.resize(140, 20)
        self.translation_label.textChanged[str].connect(self.onChanged)


        self.show()

    def setUpMainWindow(self):
        self.times_pressed_buttonrec = 1

        self.buttonrec = QPushButton("PUSH TO RECORD", self)
        self.buttonrec.move(60, 70)
        self.buttonrec.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        self.times_pressed_buttonrec += 1
        if (self.times_pressed_buttonrec % 2) != 0:
            self.buttonrec.setText("START RECORDING")
            self.buttonrec.adjustSize()


        if (self.times_pressed_buttonrec % 2) == 0:
            self.buttonrec.setText("STOP RECORDING")
            self.buttonrec.adjustSize()
            self.recorder_model = Recorder(length=10, path="../DATA/PHRASES/SPEAKING/", file='polish666.wav')
            self.recorder_model.record()
            self.whisper_model.transcribe_file(path=self.recorder_model.path,file=self.recorder_model.file)
            self.transcription_label.setText(self.whisper_model.last_transcribe)
            self.translation_label.setText(self.whisper_model.last_translate)
            self.sd_model.ask_and_save(self.translation_label.text(),self.translation_label.text()+'.png')

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
