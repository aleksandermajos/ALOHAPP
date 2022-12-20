import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt6.QtGui import QPixmap, QIcon
from BUSINESS.NLP.REC_MIC_PYAUDIO import Mic_Recorder
from BUSINESS.NLP.TTS_DE_SILERO import TTS_DE
from BUSINESS.NLP.ASR_WHISPER import WhisperModel
from BUSINESS.NLP.TRANSLATE_EN_DE_FAIRQ import Translate
from BUSINESS.NLP.REC_SPEAKER import Sound_recorder
#from BUSINESS.NLP.CHATGPT_UNOFFICIAL import Gadula





class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        icon = QIcon("DATA/PIC/ALOHA.jpg")
        self.setWindowIcon(icon)
        self.initializeAI()
        self.initializeUI()
    def initializeAI(self):
        #self.gadula = Gadula()
        self.mic_recorder = Mic_Recorder(length=10, path="DATA/PHRASES/SPEAKING/", file='polish666.wav')
        self.sound_recorder = Sound_recorder()
        self.whisper_model = WhisperModel(size='medium', lang='german')
        #self.whisper_model.transcribe_all_in_dir(path="DATA/PHRASES/LISTENING/",fe='.mp3')
        self.translator = Translate()
        self.tts_de = TTS_DE()
    def initializeUI(self):
        self.setGeometry(70,70,400,250)
        self.setWindowTitle("ALOHAPP!")
        self.setUpMainWindow()

        self.lbl = QLabel(self)

        self.talk_label = QLineEdit(self)
        self.talk_label.move(60, 110)
        self.talk_label.resize(220, 20)
        self.talk_label.textChanged[str].connect(self.onChanged)

        self.english_label = QLineEdit(self)
        self.english_label.move(60, 150)
        self.english_label.resize(220, 20)
        self.english_label.textChanged[str].connect(self.onChanged)

        self.german_label = QLineEdit(self)
        self.german_label.move(60, 190)
        self.german_label.resize(220, 20)
        self.german_label.textChanged[str].connect(self.onChanged)


        self.show()

    def setUpMainWindow(self):
        self.times_pressed_buttonrec_PL = 1
        self.times_pressed_buttonrec_UK = 1
        self.times_pressed_buttonrec_DE = 1

        self.buttonrec_PL = QPushButton("PL", self)
        self.buttonrec_PL.move(60, 70)
        self.buttonrec_PL.clicked.connect(self.buttonClicked_PL)

        self.buttonrec_UK = QPushButton("UK", self)
        self.buttonrec_UK.move(140, 70)
        self.buttonrec_UK.clicked.connect(self.buttonClicked_UK)

        self.buttonrec_DE = QPushButton("DE", self)
        self.buttonrec_DE.move(220, 70)
        self.buttonrec_DE.clicked.connect(self.buttonClicked_DE)

    def buttonClicked_PL(self):
        self.times_pressed_buttonrec_PL += 1
        if (self.times_pressed_buttonrec_PL % 2) != 0:
            self.buttonrec_PL.setText("START RECORDING")
            self.buttonrec_PL.adjustSize()


        if (self.times_pressed_buttonrec_PL % 2) == 0:
            self.times_pressed_buttonrec_PL += 1
            self.buttonrec_PL.setText("PL")
            self.buttonrec_PL.adjustSize()
            self.mic_recorder = Mic_Recorder(length=4, path="DATA/PHRASES/SPEAKING/", file='polish666.wav')
            self.mic_recorder.record()
            self.whisper_model.options = dict(language='polish', beam_size=5, best_of=5)
            self.whisper_model.transcribe_options = dict(task="transcribe", **self.whisper_model.options)
            self.whisper_model.translate_options = dict(task="translate", **self.whisper_model.options)
            self.whisper_model.transcribe_file(path=self.mic_recorder.path, file=self.mic_recorder.file)
            self.whisper_model.translate_file()
            self.talk_label.setText(self.whisper_model.last_transcribe)
            self.english_label.setText(self.whisper_model.last_translate)
            self.german_label.setText(self.translator.translate(self.whisper_model.last_translate))
            self.tts_de.create_and_save(self.german_label.text())


    def buttonClicked_UK(self):
        self.times_pressed_buttonrec_UK += 1
        if (self.times_pressed_buttonrec_UK % 2) != 0:
            self.buttonrec_UK.setText("START RECORDING")
            self.buttonrec_UK.adjustSize()

        if (self.times_pressed_buttonrec_UK % 2) == 0:
            self.times_pressed_buttonrec_UK += 1
            self.buttonrec_UK.setText("UK")
            self.buttonrec_UK.adjustSize()
            self.mic_recorder = Mic_Recorder(length=4, path="DATA/PHRASES/SPEAKING/", file='polish666.wav')
            self.mic_recorder.record()
            self.whisper_model.options = dict(language='english', beam_size=5, best_of=5)
            self.whisper_model.transcribe_options = dict(task="transcribe", **self.whisper_model.options)
            self.whisper_model.translate_options = dict(task="translate", **self.whisper_model.options)
            self.whisper_model.transcribe_file(path=self.mic_recorder.path, file=self.mic_recorder.file)
            self.talk_label.setText(self.whisper_model.last_transcribe)
            self.english_label.setText(self.whisper_model.last_transcribe)
            self.german_label.setText(self.translator.translate(self.whisper_model.last_transcribe))
            self.tts_de.create_and_save(self.german_label.text())

    def buttonClicked_DE(self):
        self.times_pressed_buttonrec_DE += 1
        if (self.times_pressed_buttonrec_DE % 2) != 0:
            self.buttonrec_DE.setText("DE")
            self.buttonrec_DE.adjustSize()

        if (self.times_pressed_buttonrec_DE % 2) == 0:
            self.times_pressed_buttonrec_DE += 1
            self.buttonrec_DE.setText("DE")
            self.buttonrec_DE.adjustSize()
            self.mic_recorder = Mic_Recorder(length=4, path="DATA/PHRASES/SPEAKING/", file='polish666.wav')
            self.mic_recorder.record()
            self.whisper_model.options = dict(language='german', beam_size=5, best_of=5)
            self.whisper_model.transcribe_options = dict(task="transcribe", **self.whisper_model.options)
            self.whisper_model.translate_options = dict(task="translate", **self.whisper_model.options)
            self.whisper_model.transcribe_file(path=self.mic_recorder.path, file=self.mic_recorder.file)
            self.whisper_model.translate_file()
            self.talk_label.setText(self.whisper_model.last_transcribe)
            self.english_label.setText(self.whisper_model.last_translate)
            self.german_label.setText(self.whisper_model.last_transcribe)
            self.tts_de.create_and_save(self.german_label.text())

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