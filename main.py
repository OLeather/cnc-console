import sys
import matplotlib
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QPushButton, QWidget

from CoordinatesWidget import CoordinatesWidget
from GCode import plotGcode
from GraphCanvas import GraphCanvas
from JogWidget import JogWidget

matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets


def callBackOnSubmit(arg1, arg2):
    print("Function is called with args: %s & %s" % (arg1, arg2))


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        sc = GraphCanvas(self)
        xs, ys, zs = plotGcode(open("gcode1.gcode"))
        sc.axes.plot(xs, ys, zs)

        jogWidget = JogWidget(self)
        coordinatesWidget = CoordinatesWidget(MainWindow, self)
        vLayout = QVBoxLayout()
        vLayout.addWidget(jogWidget)
        vLayout.addWidget(coordinatesWidget)
        layout = QHBoxLayout()
        layout.addLayout(vLayout)
        layout.addWidget(sc)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        self.show()


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()
