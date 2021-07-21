from PyQt5.QtWidgets import *


class ProgramManagerWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.startProgramFunction = None
        self.endProgramFunction = None
        self.pauseProgramFunction = None
        self.resumeProgramFunction = None
        self.startBtn = QPushButton("Start Program")
        self.endBtn = QPushButton("End")
        self.pauseBtn = QPushButton("Pause")
        self.resumeBtn = QPushButton("Resume")
        self.progressBar = QProgressBar()
        self.pauseBtn.hide()
        self.resumeBtn.hide()
        self.endBtn.hide()
        self.startBtn.clicked.connect(self.startProgramPress)
        self.endBtn.clicked.connect(self.endProgramPress)
        self.pauseBtn.clicked.connect(self.pauseProgramPress)
        self.resumeBtn.clicked.connect(self.resumeProgramPress)
        layout = QHBoxLayout()
        layout.addWidget(self.startBtn)
        layout.addWidget(self.endBtn)
        layout.addWidget(self.pauseBtn)
        layout.addWidget(self.resumeBtn)
        layout.addWidget(self.progressBar)
        self.setLayout(layout)

    def startProgramPress(self):
        self.startBtn.hide()
        self.endBtn.show()
        self.pauseBtn.show()
        if self.startProgramFunction is not None:
            self.startProgramFunction()

    def endProgramPress(self):
        self.startBtn.show()
        self.endBtn.hide()
        self.resumeBtn.hide()
        self.pauseBtn.hide()
        if self.endProgramFunction is not None:
            self.endProgramFunction()

    def pauseProgramPress(self):
        self.resumeBtn.show()
        self.pauseBtn.hide()
        if self.pauseProgramFunction is not None:
            self.pauseProgramFunction()

    def resumeProgramPress(self):
        self.resumeBtn.hide()
        self.pauseBtn.show()
        if self.resumeProgramFunction is not None:
            self.resumeProgramFunction()

    def programDone(self):
        self.startBtn.show()
        self.endBtn.hide()
        self.resumeBtn.hide()
        self.pauseBtn.hide()

    def setProgramProgress(self, progress):
        self.progressBar.setValue(progress)