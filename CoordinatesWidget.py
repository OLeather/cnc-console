from PyQt5.QtWidgets import *

from numpad import NumpadDialog, isfloat


def callBackOnSubmit(arg1, arg2):
    print("Function is called with args: %s & %s" % (arg1, arg2))


class CoordinatesWidget(QWidget):

    def __init__(self, MainWindow, parent=None):
        super().__init__(parent)
        self.machinePositionSetter = None
        self.MainWindow = MainWindow
        self.xSetField = QLineEdit(self)
        self.ySetField = QLineEdit(self)
        self.zSetField = QLineEdit(self)

        self.x = 0.0
        self.y = 0.0
        self.z = 0.0

        self.x = 0.0
        self.y = 0.0
        self.z = 0.0

        self.xSetField.setText(str(self.x) + " mm")
        self.ySetField.setText(str(self.y) + " mm")
        self.zSetField.setText(str(self.z) + " mm")
        self.xSetField.setReadOnly(True)
        self.ySetField.setReadOnly(True)
        self.zSetField.setReadOnly(True)


        xText = QLabel("X:")
        yText = QLabel("Y:")
        zText = QLabel("Z:")

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
        xLayout.addWidget(self.xSetField)
        xLayout.addWidget(self.xSet)
        yLayout.addWidget(yText)
        yLayout.addWidget(self.ySetField)
        yLayout.addWidget(self.ySet)
        zLayout.addWidget(zText)
        zLayout.addWidget(self.zSetField)
        zLayout.addWidget(self.zSet)

        layout = QVBoxLayout()

        layout.addLayout(xLayout)
        layout.addLayout(yLayout)
        layout.addLayout(zLayout)

        self.setLayout(layout)

    def setPressed(self):
        text = ""
        setter = self.setXText
        value = "Cancel"
        if self.sender() == self.xSet:
            value = NumpadDialog.getValue(self, "X:")
            if value != "Cancel" and isfloat(value):
                self.setXText(float(value))
                self.machinePositionSetter(x=float(value))
        if self.sender() == self.ySet:
            value = NumpadDialog.getValue(self, "Y:")
            if value != "Cancel" and isfloat(value):
                self.setYText(float(value))
                self.machinePositionSetter(y=float(value))
        if self.sender() == self.zSet:
            value = NumpadDialog.getValue(self, "Z:")
            if value != "Cancel" and isfloat(value):
                self.setZText(float(value))
                self.machinePositionSetter(z=float(value))

    def setXText(self, x):
        self.x = x
        self.xSetField.setText(str(x) + " mm")

    def setYText(self, y):
        self.y = y
        self.ySetField.setText(str(y) + " mm")

    def setZText(self, z):
        self.z = z
        self.zSetField.setText(str(z) + " mm")
