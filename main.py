import sys
import matplotlib
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QPushButton, QWidget

from CoordinatesWidget import CoordinatesWidget
from GCode import plotGcode
from GraphWidget import GraphWidget
from JogWidget import JogWidget
from Machine import Machine

matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets


def callBackOnSubmit(arg1, arg2):
    print("Function is called with args: %s & %s" % (arg1, arg2))


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = GraphWidget(self)

        self.jogWidget = JogWidget(self)
        self.coordinatesWidget = CoordinatesWidget(MainWindow, self)
        vLayout = QVBoxLayout()
        vLayout.addWidget(self.jogWidget)
        vLayout.addWidget(self.coordinatesWidget)
        layout = QHBoxLayout()
        layout.addLayout(vLayout)
        layout.addWidget(self.graphWidget)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    m = Machine(w)
    m.loadGCode("gcode1.gcode")
    app.exec_()
