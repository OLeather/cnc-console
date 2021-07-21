from threading import Thread
from time import sleep

from numpy.random import randint
from printrun.printcore import printcore, gcoder

from GCode import plotGcode


class Machine:
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow
        self.mainWindow.coordinatesWidget.machinePositionSetter = self.setPosition
        self._bindJogButtons()
        self.gcode = None
        self.cnc = printcore('COM3', 115200)
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        thread = Thread(target=self.run)
        thread.start()

    def _bindJogButtons(self):
        self.mainWindow.jogWidget.xPlusButton.clicked.connect(self.jogPlusX)
        self.mainWindow.jogWidget.xMinusButton.clicked.connect(self.jogMinusX)
        self.mainWindow.jogWidget.yPlusButton.clicked.connect(self.jogPlusY)
        self.mainWindow.jogWidget.yMinusButton.clicked.connect(self.jogMinusY)
        self.mainWindow.jogWidget.zPlusButton.clicked.connect(self.jogPlusZ)
        self.mainWindow.jogWidget.zMinusButton.clicked.connect(self.jogMinusZ)

    def jogPlusX(self):
        self.mainWindow.coordinatesWidget.setDesiredX(
            self.mainWindow.coordinatesWidget.desiredX + self.mainWindow.jogWidget.step)
        self.setPosition(x=self.mainWindow.coordinatesWidget.desiredX)

    def jogMinusX(self):
        self.mainWindow.coordinatesWidget.setDesiredX(
            self.mainWindow.coordinatesWidget.desiredX - self.mainWindow.jogWidget.step)
        self.setPosition(x=self.mainWindow.coordinatesWidget.desiredX)

    def jogPlusY(self):
        self.mainWindow.coordinatesWidget.setDesiredY(
            self.mainWindow.coordinatesWidget.desiredY + self.mainWindow.jogWidget.step)
        self.setPosition(y=self.mainWindow.coordinatesWidget.desiredY)

    def jogMinusY(self):
        self.mainWindow.coordinatesWidget.setDesiredY(
            self.mainWindow.coordinatesWidget.desiredY - self.mainWindow.jogWidget.step)
        self.setPosition(y=self.mainWindow.coordinatesWidget.desiredY)

    def jogPlusZ(self):
        self.mainWindow.coordinatesWidget.setDesiredZ(
            self.mainWindow.coordinatesWidget.desiredZ + self.mainWindow.jogWidget.step)
        self.setPosition(z=self.mainWindow.coordinatesWidget.desiredZ)

    def jogMinusZ(self):
        self.mainWindow.coordinatesWidget.setDesiredZ(
            self.mainWindow.coordinatesWidget.desiredZ - self.mainWindow.jogWidget.step)
        self.setPosition(z=self.mainWindow.coordinatesWidget.desiredZ)

    def run(self):
        while True:
            self.x, self.y, self.z = self._getAbsPos()
            self.mainWindow.coordinatesWidget.setActualX(self.x)
            self.mainWindow.coordinatesWidget.setActualY(self.y)
            self.mainWindow.coordinatesWidget.setActualZ(self.z)
            sleep(0.01)

    def loadGCode(self, path):
        self.gcode = gcoder.LightGCode([i.strip() for i in open(path)])
        self.mainWindow.graphWidget.axes.cla()
        xs, ys, zs = plotGcode(open(path))
        self.mainWindow.graphWidget.axes.plot(xs, ys, zs)

    def startPrint(self):
        if not self.cnc.online:
            print("CNC Machine not online")
        else:
            self.cnc.startprint(self.gcode)

    def pause(self):
        self.cnc.pause()

    def resume(self):
        self.cnc.resume()

    def setPosition(self, x=None, y=None, z=None):
        command = "G0"
        if x is not None:
            command += " X" + str(x)
        if y is not None:
            command += " Y" + str(y)
        if z is not None:
            command += " Z" + str(z)

        print(command)
        self.cnc.send_now("G21")
        self.cnc.send_now("G90")
        self.cnc.send_now(command)

    def zero(self, x=False, y=False, z=False):
        self.mainWindow.coordinatesWidget.setDesiredX(0)
        self.mainWindow.coordinatesWidget.setDesiredY(0)
        self.mainWindow.coordinatesWidget.setDesiredZ(0)
        command = "G92"
        if x:
            command += "X0"
        if y:
            command += "Y0"
        if z:
            command += "Z0"
        self.cnc.send_now(command)

    def _getAbsPos(self):
        return randint(100), randint(100), randint(100)
