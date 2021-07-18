import matplotlib
from PyQt5.QtWidgets import *

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

        self.xPlusButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.xMinusButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.yPlusButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.yMinusButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.zPlusButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.zMinusButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        layout.addWidget(self.xPlusButton, 1, 2)
        layout.addWidget(self.xMinusButton, 1, 0)
        layout.addWidget(self.yPlusButton, 0, 1)
        layout.addWidget(self.yMinusButton, 2, 1)
        layout.addWidget(self.zPlusButton, 0, 3)
        layout.addWidget(self.zMinusButton, 2, 3)
        for i in range(6):
            layout.setRowStretch(i, 1)
            layout.setColumnStretch(i, 1)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.setLayout(layout)

    def resizeEvent(self, e):
        self.setMinimumWidth(self.height())
