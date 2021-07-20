from PyQt5.QtWidgets import *

from numpad import NumpadDialog, isfloat


def callBackOnSubmit(arg1, arg2):
    print("Function is called with args: %s & %s" % (arg1, arg2))


class CoordinatesWidget(QWidget):

    def __init__(self, MainWindow, parent=None):
        super().__init__(parent)
        self.MainWindow = MainWindow
        self.xField = QLineEdit(self)
        self.yField = QLineEdit(self)
        self.zField = QLineEdit(self)

        self.x = 0.0
        self.y = 0.0
        self.z = 0.0

        self.xField.setText(str(self.x)  + " mm")
        self.yField.setText(str(self.y)  + " mm")
        self.zField.setText(str(self.z)  + " mm")
        self.xField.setReadOnly(True)
        self.yField.setReadOnly(True)
        self.zField.setReadOnly(True)

        xText = QLabel("X:")
        zText = QLabel("Y:")
        yText = QLabel("Z:")

        self.xSet = QPushButton("Set")
        self.ySet = QPushButton("Set")
        self.zSet = QPushButton("Set")

        self.xSet.clicked.connect(self.setPressed)
        self.ySet.clicked.connect(self.setPressed)
        self.zSet.clicked.connect(self.setPressed)

        xLayout = QHBoxLayout()
        yLayout = QHBoxLayout()
        zLayout = QHBoxLayout()

        xLayout.addWidget(xText)
        xLayout.addWidget(self.xField)
        xLayout.addWidget(self.xSet)
        yLayout.addWidget(yText)
        yLayout.addWidget(self.yField)
        yLayout.addWidget(self.ySet)
        zLayout.addWidget(zText)
        zLayout.addWidget(self.zField)
        zLayout.addWidget(self.zSet)

        layout = QVBoxLayout()

        layout.addLayout(xLayout)
        layout.addLayout(yLayout)
        layout.addLayout(zLayout)

        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.setLayout(layout)

    def resizeEvent(self, e):
        self.setMinimumWidth(self.height())

    def setPressed(self):
        text = ""
        setter = self.setX
        if self.sender() == self.xSet:
            text = "X:"
            setter = self.setX
        if self.sender() == self.ySet:
            text = "Y:"
            setter = self.setY
        if self.sender() == self.zSet:
            text = "Z:"
            setter = self.setZ
        value = NumpadDialog.getValue(self, text)
        if value != "Cancel" and isfloat(value):
            setter(float(value))

    def setX(self, x):
        self.x = x
        self.xField.setText(str(x) + " mm")

    def setY(self, y):
        self.y = y
        self.yField.setText(str(y) + " mm")

    def setZ(self, z):
        self.z = z
        self.zField.setText(str(z) + " mm")