from pytubefix import YouTube
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("YouTube Downloader")
        self.initUI()

    def initUI(self):
        self.textbox = QtWidgets.QLineEdit(self)
        self.textbox.setPlaceholderText('Enter URL here')
        self.textbox.move(20, 20)
        self.textbox.resize(260, 40)

        self.textbox2 = QtWidgets.QLineEdit(self)
        self.textbox2.setPlaceholderText('Enter path here of type : /Users/alex/Documents/Downloads/')
        self.textbox2.move(20, 70)
        self.textbox2.resize(260, 40)

        self.button = QtWidgets.QPushButton("Download", self)
        self.button.move(20, 120)
        self.button.resize(260, 40)
        self.button.clicked.connect(self.download)

        self.checkbox = QtWidgets.QCheckBox('Download audio only', self)
        self.checkbox.move(20, 170)
        self.checkbox.resize(260, 40)
    
    def download(self):
        yt = YouTube(self.textbox.text())
        if self.checkbox.isChecked():
            audio = yt.streams.filter(only_audio=True).get_highest_resolution()
            audio.download(self.textbox2.text())
        else:
            video = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
            video.download(self.textbox2.text())
        print('Successfully downloaded :', yt.title)
        self.textbox.clear()
        self.textbox2.clear()

def window():
    app=QApplication(sys.argv)
    win=MyWindow()
    win.show()
    sys.exit(app.exec_())

window()