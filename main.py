import sys
import matplotlib
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QPushButton, QWidget

from GCode import plotGcode
from GraphCanvas import GraphCanvas
from JogWidget import JogWidget

matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Create the maptlotlib FigureCanvas object,
        # which defines a single set of axes as self.axes.
        sc = GraphCanvas(self)
        xs, ys, zs = plotGcode(open("gcode1.gcode"))
        sc.axes.plot(xs, ys, zs)

        jogWidget = JogWidget(self)

        layout = QHBoxLayout()
        layout.addWidget(jogWidget)
        layout.addWidget(sc)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        self.show()



app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()
