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

        self.xActualField = QLineEdit(self)
        self.yActualField = QLineEdit(self)
        self.zActualField = QLineEdit(self)

        self.desiredX = 0.0
        self.desiredY = 0.0
        self.desiredZ = 0.0

        self.x = 0.0
        self.y = 0.0
        self.z = 0.0

        self.xSetField.setText(str(self.desiredX) + " mm")
        self.ySetField.setText(str(self.desiredY) + " mm")
        self.zSetField.setText(str(self.desiredZ) + " mm")
        self.xSetField.setReadOnly(True)
        self.ySetField.setReadOnly(True)
        self.zSetField.setReadOnly(True)


        self.xActualField.setText(str(self.x) + " mm")
        self.yActualField.setText(str(self.y) + " mm")
        self.zActualField.setText(str(self.z) + " mm")
        self.xActualField.setReadOnly(True)
        self.yActualField.setReadOnly(True)
        self.zActualField.setReadOnly(True)

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
        xLayout.addWidget(self.xActualField)
        xLayout.addWidget(self.xSetField)
        xLayout.addWidget(self.xSet)
        yLayout.addWidget(yText)
        yLayout.addWidget(self.yActualField)
        yLayout.addWidget(self.ySetField)
        yLayout.addWidget(self.ySet)
        zLayout.addWidget(zText)
        zLayout.addWidget(self.zActualField)
        zLayout.addWidget(self.zSetField)
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
        setter = self.setDesiredX
        if self.sender() == self.xSet:
            text = "X:"
            setter = self.setDesiredX
        if self.sender() == self.ySet:
            text = "Y:"
            setter = self.setDesiredY
        if self.sender() == self.zSet:
            text = "Z:"
            setter = self.setDesiredZ
        value = NumpadDialog.getValue(self, text)
        if value != "Cancel" and isfloat(value):
            setter(float(value))

    def setDesiredX(self, x):
        self.desiredX = x
        self.xSetField.setText(str(x) + " mm")
        self.machinePositionSetter(x=self.desiredX)

    def setDesiredY(self, y):
        self.desiredY = y
        self.ySetField.setText(str(y) + " mm")
        self.machinePositionSetter(y=self.desiredY)

    def setDesiredZ(self, z):
        self.desiredZ = z
        self.zSetField.setText(str(z) + " mm")
        self.machinePositionSetter(z=self.desiredZ)

    def setActualX(self, x):
        self.x = x
        self.xActualField.setText(str(x) + " mm")

    def setActualY(self, y):
        self.y = y
        self.yActualField.setText(str(y) + " mm")

    def setActualZ(self, z):
        self.z = z
        self.zActualField.setText(str(z) + " mm")


