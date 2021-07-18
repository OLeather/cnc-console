import re
import numpy as np
from gcodeparser import GcodeParser, GcodeLine, Commands
from printrun import printcore


def plotGcode(gcode):
    lines = GcodeParser(gcode.read()).lines
    xs = np.array([0])
    ys = np.array([0])
    zs = np.array([0])
    for line in lines:
        if line.type == Commands.MOVE:
            if line.command[1] == 1:
                x, y, z = extractMoveValues(line, xs, ys, zs)
                xs, ys, zs = appendMoveValues(x, y, z, xs, ys, zs)
            if line.command[1] == 2:
                x, y, z = extractCircle(line, xs, ys, zs, True)
                xs, ys, zs = appendMoveValues(x, y, z, xs, ys, zs)
            if line.command[1] == 3:
                x, y, z = extractCircle(line, xs, ys, zs, False)
                xs, ys, zs = appendMoveValues(x, y, z, xs, ys, zs)
    return xs, ys, zs


def extractMoveValues(line, xs, ys, zs):
    x = getLast(xs)
    y = getLast(ys)
    z = getLast(zs)
    if line.get_param("X") is not None:
        x = line.get_param("X")
    if line.get_param("Y") is not None:
        y = line.get_param("Y")
    if line.get_param("Z") is not None:
        z = line.get_param("Z")
    return x, y, z


def appendMoveValues(x, y, z, xs, ys, zs):
    xs = np.append(xs, x)
    ys = np.append(ys, y)
    zs = np.append(zs, z)
    return xs, ys, zs


def extractCircle(line, xs, ys, zs, clockwise):
    startX = getLast(xs)
    startY = getLast(ys)
    startZ = getLast(zs)
    endX = line.get_param("X")
    endY = line.get_param("Y")
    endZ = line.get_param("Z")
    circleXs = np.array([startX])
    circleYs = np.array([startY])
    circleZs = np.array([startZ])
    I = line.get_param("I")
    if I is None:
        I = 0.0
    J = line.get_param("J")
    if J is None:
        J = 0.0
    if endX is None:
        endX = startX
    if endY is None:
        endY = startY
    endZ = startZ
    radius = np.sqrt(I * I + J * J)

    print(I, J)

    plotXs, plotYs, plotZs = plotArc(I + startX, J + startY, radius, startX, startY, endX, endY, startZ, clockwise)

    circleXs, circleYs, circleZs = appendMoveValues(plotXs, plotYs, plotZs, circleXs, circleYs, circleZs)

    circleXs, circleYs, circleZs = appendMoveValues(endX, endY, endZ, circleXs, circleYs, circleZs)
    return circleXs, circleYs, circleZs


def plotArc(cx, cy, radius, x1, y1, x2, y2, z, clockwise=False):
    a1 = np.arctan((cy - y1) / (cx - x1))
    a2 = np.arctan((cy - y2) / (cx - x2))
    circleXs = []
    circleYs = []
    circleZs = []
    if x1 <= cx:
        a1 += np.pi
    if x2 <= cx:
        a2 += np.pi
    x = cx - x2
    y = cy - y2
    if a1 > a2 and not clockwise:
        a2 += np.pi * 2
    if a2 > a1 and clockwise:
        a1 += np.pi * 2
    a = a1

    # print(y, x, np.arctan(y / x))
    # print(a1, a2, cx, cy, x1, y1, x2, y2, clockwise)

    while a > a2:
        if clockwise:
            a -= 0.01
        else:
            a += 0.01
        x = np.cos(a) * radius + cx
        y = np.sin(a) * radius + cy
        circleXs = np.append(circleXs, x)
        circleYs = np.append(circleYs, y)
        circleZs = np.append(circleZs, z)
    return circleXs, circleYs, circleZs


def getLast(arr):
    return arr[len(arr) - 1]
