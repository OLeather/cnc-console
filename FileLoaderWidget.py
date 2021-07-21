from PyQt5.QtWidgets import *


class FileLoaderWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.gcodeSetter = None
        self.loadFileBtn = QPushButton("Load GCode File")
        self.clearBtn = QPushButton("Clear")
        loadedFileText = QLabel("Loaded File:")
        self.loadedFileLine = QLineEdit("None")
        self.loadedFileLine.setReadOnly(True)
        self.loadFileBtn.clicked.connect(self.getFile)
        self.clearBtn.clicked.connect(self.clearPressed)
        layout = QHBoxLayout()
        layout.addWidget(self.loadFileBtn)
        layout.addWidget(loadedFileText)
        layout.addWidget(self.loadedFileLine)
        layout.addWidget(self.clearBtn)
        self.setLayout(layout)

    def getFile(self):
        file = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "GCode files (*.gcode)")
        if str(file[0]) is not "":
            self.gcodeSetter(str(file[0]))
            self.loadedFileLine.setText(str(file[0]))

    def clearPressed(self):
        self.gcodeSetter("")
        self.loadedFileLine.setText("None")
