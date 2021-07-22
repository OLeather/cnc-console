import sys

import matplotlib
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QPushButton, QWidget, QApplication

from CoordinatesWidget import CoordinatesWidget
from FileLoaderWidget import FileLoaderWidget
from GraphWidget import GraphWidget
from JogWidget import JogWidget
from Machine import Machine
from ProgramManagerWidget import ProgramManagerWidget
from ZeroWidget import ZeroWidget

matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets


def callBackOnSubmit(arg1, arg2):
    print("Function is called with args: %s & %s" % (arg1, arg2))


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        font = self.font()
        font.setPointSize(12)
        # set the font for *any* widget created in this QApplication:
        QApplication.instance().setFont(font)

        self.graphWidget = GraphWidget(self)
        self.fileWidget = FileLoaderWidget(self)
        self.programWidget = ProgramManagerWidget(self)
        self.jogWidget = JogWidget(self)
        self.zeroWidget = ZeroWidget(self)
        self.coordinatesWidget = CoordinatesWidget(MainWindow, self)
        vLayout = QVBoxLayout()
        vLayout.addWidget(self.coordinatesWidget)
        vLayout.addWidget(self.programWidget)
        vLayout.addWidget(self.jogWidget)
        vLayout.addWidget(self.zeroWidget)

        vLayout1 = QVBoxLayout()
        vLayout1.addWidget(self.fileWidget)
        vLayout1.addWidget(self.graphWidget)
        layout = QHBoxLayout()
        layout.addLayout(vLayout)
        layout.addLayout(vLayout1)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    m = Machine(w)
    m.zero(True, True, True)
    app.exec_()
    m.cnc.disconnect()
