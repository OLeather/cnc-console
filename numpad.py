import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


class NumpadDialog(QDialog):
    def __init__(self, parent, text):
        super(NumpadDialog, self).__init__(parent)

        self.value = ""

        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        hLayout = QHBoxLayout()
        self.lineEdit = QLineEdit()
        self.lineEdit.setReadOnly(True)
        label = QLabel(text)
        hLayout.addWidget(label)
        hLayout.addWidget(self.lineEdit)

        self.btn0 = QPushButton("0")
        sizePolicy.setHeightForWidth(self.btn0.sizePolicy().hasHeightForWidth())
        self.btn0.setSizePolicy(sizePolicy)
        self.btn1 = QPushButton("1")
        sizePolicy.setHeightForWidth(self.btn1.sizePolicy().hasHeightForWidth())
        self.btn1.setSizePolicy(sizePolicy)
        self.btn2 = QPushButton("2")
        sizePolicy.setHeightForWidth(self.btn2.sizePolicy().hasHeightForWidth())
        self.btn2.setSizePolicy(sizePolicy)
        self.btn3 = QPushButton("3")
        sizePolicy.setHeightForWidth(self.btn3.sizePolicy().hasHeightForWidth())
        self.btn3.setSizePolicy(sizePolicy)
        self.btn4 = QPushButton("4")
        sizePolicy.setHeightForWidth(self.btn4.sizePolicy().hasHeightForWidth())
        self.btn4.setSizePolicy(sizePolicy)
        self.btn5 = QPushButton("5")
        sizePolicy.setHeightForWidth(self.btn5.sizePolicy().hasHeightForWidth())
        self.btn5.setSizePolicy(sizePolicy)
        self.btn6 = QPushButton("6")
        sizePolicy.setHeightForWidth(self.btn6.sizePolicy().hasHeightForWidth())
        self.btn6.setSizePolicy(sizePolicy)
        self.btn7 = QPushButton("7")
        sizePolicy.setHeightForWidth(self.btn7.sizePolicy().hasHeightForWidth())
        self.btn7.setSizePolicy(sizePolicy)
        self.btn8 = QPushButton("8")
        sizePolicy.setHeightForWidth(self.btn8.sizePolicy().hasHeightForWidth())
        self.btn8.setSizePolicy(sizePolicy)
        self.btn9 = QPushButton("9")
        sizePolicy.setHeightForWidth(self.btn9.sizePolicy().hasHeightForWidth())
        self.btn9.setSizePolicy(sizePolicy)
        self.btn_dec = QPushButton(".")
        sizePolicy.setHeightForWidth(self.btn_dec.sizePolicy().hasHeightForWidth())
        self.btn_dec.setSizePolicy(sizePolicy)
        self.btn_minus = QPushButton("-")
        sizePolicy.setHeightForWidth(self.btn_minus.sizePolicy().hasHeightForWidth())
        self.btn_minus.setSizePolicy(sizePolicy)
        self.btn_cancel = QPushButton("Cancel")
        sizePolicy.setHeightForWidth(self.btn_cancel.sizePolicy().hasHeightForWidth())
        self.btn_cancel.setSizePolicy(sizePolicy)
        self.btn_enter = QPushButton("Enter")
        sizePolicy.setHeightForWidth(self.btn_enter.sizePolicy().hasHeightForWidth())
        self.btn_enter.setSizePolicy(sizePolicy)
        self.btn_del = QPushButton("Delete")
        sizePolicy.setHeightForWidth(self.btn_del.sizePolicy().hasHeightForWidth())
        self.btn_del.setSizePolicy(sizePolicy)
        self.btn_clear = QPushButton("C")
        sizePolicy.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy)

        layout = QGridLayout()
        layout.addLayout(hLayout, 0, 0, 1, 4)
        layout.addWidget(self.btn1, 1, 0, 1, 1)
        layout.addWidget(self.btn2, 1, 1, 1, 1)
        layout.addWidget(self.btn3, 1, 2, 1, 1)
        layout.addWidget(self.btn4, 2, 0, 1, 1)
        layout.addWidget(self.btn5, 2, 1, 1, 1)
        layout.addWidget(self.btn6, 2, 2, 1, 1)
        layout.addWidget(self.btn7, 3, 0, 1, 1)
        layout.addWidget(self.btn8, 3, 1, 1, 1)
        layout.addWidget(self.btn9, 3, 2, 1, 1)
        layout.addWidget(self.btn_minus, 4, 0, 1, 1)
        layout.addWidget(self.btn0, 4, 1, 1, 1)
        layout.addWidget(self.btn_dec, 4, 2, 1, 1)
        layout.addWidget(self.btn_clear, 1, 3, 2, 1)
        layout.addWidget(self.btn_del, 3, 3, 2, 1)
        layout.addWidget(self.btn_enter, 5, 0, 1, 2)
        layout.addWidget(self.btn_cancel, 5, 2, 1, 2)

        self.btn0.clicked.connect(self.button_press)
        self.btn1.clicked.connect(self.button_press)
        self.btn2.clicked.connect(self.button_press)
        self.btn3.clicked.connect(self.button_press)
        self.btn4.clicked.connect(self.button_press)
        self.btn5.clicked.connect(self.button_press)
        self.btn6.clicked.connect(self.button_press)
        self.btn7.clicked.connect(self.button_press)
        self.btn8.clicked.connect(self.button_press)
        self.btn9.clicked.connect(self.button_press)
        self.btn_dec.clicked.connect(self.button_press)
        self.btn_minus.clicked.connect(self.button_press)
        self.btn_del.clicked.connect(self.button_press)
        self.btn_clear.clicked.connect(self.button_press)
        self.btn_enter.clicked.connect(self.enter_press)
        self.btn_cancel.clicked.connect(self.cancel_press)

        self.setLayout(layout)

    def button_press(self):
        if self.sender() == self.btn0:
            self.value += "0"
        if self.sender() == self.btn1:
            self.value += "1"
        if self.sender() == self.btn2:
            self.value += "2"
        if self.sender() == self.btn3:
            self.value += "3"
        if self.sender() == self.btn4:
            self.value += "4"
        if self.sender() == self.btn5:
            self.value += "5"
        if self.sender() == self.btn6:
            self.value += "6"
        if self.sender() == self.btn7:
            self.value += "7"
        if self.sender() == self.btn8:
            self.value += "8"
        if self.sender() == self.btn9:
            self.value += "9"
        if self.sender() == self.btn_dec:
            self.value += "."
        if self.sender() == self.btn_minus:
            self.value += "-"
        if self.sender() == self.btn_del:
            self.value = self.value[:-1]
        if self.sender() == self.btn_clear:
            self.value = ""
        self.lineEdit.setText(self.value)

    def cancel_press(self):
        self.value = "Cancel"
        self.close()

    def enter_press(self):
        self.close()

    @classmethod
    def getValue(cls, parent, text):
        dialog = cls(parent, text)
        dialog.exec_()
        return dialog.value
