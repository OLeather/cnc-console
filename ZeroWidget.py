from PyQt5.QtWidgets import *


class ZeroWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout()
        self.zeroXBtn = QPushButton("Zero X")
        self.zeroYBtn = QPushButton("Zero Y")
        self.zeroZBtn = QPushButton("Zero Z")
        self.zeroAllBtn = QPushButton("Zero All")
        layout.addWidget(self.zeroXBtn)
        layout.addWidget(self.zeroYBtn)
        layout.addWidget(self.zeroZBtn)
        layout.addWidget(self.zeroAllBtn)
        self.setLayout(layout)