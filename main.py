import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt6.QtGui import QPixmap, QIcon
from BUSINESS.NLP.REC_MIC_PYAUDIO import Mic_Recorder
from BUSINESS.NLP.TTS_DE_SILERO import TTS_DE
from BUSINESS.NLP.ASR_WHISPER import WhisperModel
from BUSINESS.NLP.TRANSLATE_EN_DE_FAIRQ import Translate
from BUSINESS.NLP.REC_SPEAKER import Sound_recorder





class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        icon = QIcon("DATA/PIC/ALOHA.jpg")
        self.setWindowIcon(icon)
        self.initializeAI()
        self.initializeUI()
    def initializeAI(self):
        self.mic_recorder = Mic_Recorder(length=10, path="DATA/PHRASES/SPEAKING/", file='polish666.wav')
        self.sound_recorder = Sound_recorder()
        self.whisper_model = WhisperModel(size='small', lang='polish')
        self.translator = Translate()
        self.tts_de = TTS_DE()
    def initializeUI(self):
        self.setGeometry(70,70,300,440)
        self.setWindowTitle("ALOHAPP!")
        self.setUpMainWindow()

        self.lbl = QLabel(self)

        self.orginal_label = QLineEdit(self)
        self.orginal_label.move(60, 110)
        self.orginal_label.resize(220, 20)
        self.orginal_label.textChanged[str].connect(self.onChanged)

        self.english_label = QLineEdit(self)
        self.english_label.move(60, 150)
        self.english_label.resize(220, 20)
        self.english_label.textChanged[str].connect(self.onChanged)

        self.translated_label = QLineEdit(self)
        self.translated_label.move(60, 190)
        self.translated_label.resize(220, 20)
        self.translated_label.textChanged[str].connect(self.onChanged)


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
            #self.sound_recorder.record()
            self.mic_recorder = Mic_Recorder(length=5, path="DATA/PHRASES/SPEAKING/", file='polish666.wav')
            self.mic_recorder.record()
            self.whisper_model.transcribe_file(path=self.mic_recorder.path, file=self.mic_recorder.file)
            self.orginal_label.setText(self.whisper_model.last_transcribe)
            self.english_label.setText(self.whisper_model.last_translate)
            self.translated_label.setText(self.translator.translate(self.whisper_model.last_translate))
            self.tts_de.create_and_save(self.translated_label.text())


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