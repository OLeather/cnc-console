import matplotlib
from PyQt5.QtWidgets import *

from numpad import NumpadDialog, isfloat

matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class JogWidget(QWidget):

    def __init__(self, parent=None):
        layout = QGridLayout()
        super().__init__(parent)
        self.xPlusButton = QPushButton("+X")
        self.xMinusButton = QPushButton("-X")
        self.yPlusButton = QPushButton("+Y")
        self.yMinusButton = QPushButton("-Y")
        self.zPlusButton = QPushButton("+Z")
        self.zMinusButton = QPushButton("-Z")

        self.step = 10.0

        hLayout = QHBoxLayout()
        self.lineEdit = QLineEdit()
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setText(str(self.step)+" mm")
        label = QLabel("Step:")

        self.setBtn = QPushButton("Set")
        self.setBtn.clicked.connect(self.setPressed)

        hLayout.addWidget(label)
        hLayout.addWidget(self.lineEdit)
        hLayout.addWidget(self.setBtn)

        self.xPlusButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.xMinusButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.yPlusButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.yMinusButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.zPlusButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.zMinusButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        layout.addLayout(hLayout, 0, 0, 1, 4)
        layout.addWidget(self.xPlusButton, 2, 2)
        layout.addWidget(self.xMinusButton, 2, 0)
        layout.addWidget(self.yPlusButton, 1, 1)
        layout.addWidget(self.yMinusButton, 3, 1)
        layout.addWidget(self.zPlusButton, 1, 3)
        layout.addWidget(self.zMinusButton, 3, 3)
        for i in range(6):
            layout.setRowStretch(i, 1)
            layout.setColumnStretch(i, 1)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.setLayout(layout)

    def resizeEvent(self, e):
        self.setMinimumWidth(self.height())

    def setPressed(self):
        text = ""
        value = NumpadDialog.getValue(self, text)
        if value is not "Cancel" and isfloat(value):
            self.step = float(value)
            self.lineEdit.setText(str(self.step)+" mm")
