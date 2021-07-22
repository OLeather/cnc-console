from threading import Thread
from time import sleep

from Printrun.printrun import gcoder
from Printrun.printrun.printcore import printcore

from GCode import plotGcode


class Machine:
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow
        self.mainWindow.coordinatesWidget.machinePositionSetter = self.setPosition
        self.mainWindow.fileWidget.gcodeSetter = self.loadGCode
        self.mainWindow.programWidget.startProgramFunction = self.startProgram
        self.mainWindow.programWidget.pauseProgramFunction = self.pause
        self.mainWindow.programWidget.resumeProgramFunction = self.resume
        self.mainWindow.programWidget.endProgramFunction = self.end
        self._bindJogButtons()
        self.gcode = None

        self.cnc = printcore()
        self.cnc.connect('COM3', 115200, True)
        while not self.cnc.online:
            sleep(.1)
        self.cnc.endcb = self.mainWindow.programWidget.programDone()

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
        self.mainWindow.zeroWidget.zeroXBtn.clicked.connect(self.zeroXPressed)
        self.mainWindow.zeroWidget.zeroYBtn.clicked.connect(self.zeroYPressed)
        self.mainWindow.zeroWidget.zeroZBtn.clicked.connect(self.zeroZPressed)
        self.mainWindow.zeroWidget.zeroAllBtn.clicked.connect(self.zeroXPressed)
        self.mainWindow.zeroWidget.zeroAllBtn.clicked.connect(self.zeroYPressed)
        self.mainWindow.zeroWidget.zeroAllBtn.clicked.connect(self.zeroZPressed)

    def jogPlusX(self):
        self.setPosition(x=self.cnc.analyzer.abs_x + self.mainWindow.jogWidget.step)

    def jogMinusX(self):
        self.setPosition(x=self.cnc.analyzer.abs_x - self.mainWindow.jogWidget.step)

    def jogPlusY(self):
        self.setPosition(y=self.cnc.analyzer.abs_y + self.mainWindow.jogWidget.step)

    def jogMinusY(self):
        self.setPosition(y=self.cnc.analyzer.abs_y - self.mainWindow.jogWidget.step)

    def jogPlusZ(self):
        self.setPosition(z=self.cnc.analyzer.abs_z + self.mainWindow.jogWidget.step)

    def jogMinusZ(self):
        self.setPosition(z=self.cnc.analyzer.abs_z - self.mainWindow.jogWidget.step)

    def zeroXPressed(self):
        self.zero(x=True)

    def zeroYPressed(self):
        self.zero(y=True)

    def zeroZPressed(self):
        self.zero(z=True)

    def run(self):
        while True:
            self.mainWindow.coordinatesWidget.setXText(self.cnc.analyzer.abs_x)
            self.mainWindow.coordinatesWidget.setYText(self.cnc.analyzer.abs_y)
            self.mainWindow.coordinatesWidget.setZText(self.cnc.analyzer.abs_z)
            sleep(0.1)

    def loadGCode(self, path):
        self.mainWindow.graphWidget.axes.cla()
        if path is "":
            self.gcode = None
        else:
            self.gcode = gcoder.LightGCode([i.strip() for i in open(path)])
            xs, ys, zs = plotGcode(open(path))
            self.mainWindow.graphWidget.axes.plot(xs, ys, zs)
        self.mainWindow.graphWidget.fig.canvas.draw()

    def startProgram(self):
        if not self.cnc.online:
            print("CNC Machine not online")
        else:
            self.cnc.startprint(self.gcode)

    def pause(self):
        self.cnc.pause()

    def resume(self):
        self.cnc.resume()

    def end(self):
        self.cnc.cancelprint()

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
        command = "G92"
        if x:
            command += "X0"
        if y:
            command += "Y0"
        if z:
            command += "Z0"
        self.cnc.send_now(command)
