#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial

In the example, we draw randomly 1000 red points
on the window.

author: Jan Bodnar
website: zetcode.com
last edited: September 2011
"""

import sys, random, time
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Points')
        self.show()

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.dessine(qp)
        qp.end()

    def dessine(self, qp):

        qp.setPen(QtCore.Qt.red)
        size = self.size()

        color = QtGui.QColor()
        brush = QtGui.QBrush(QtCore.Qt.SolidPattern)
        brush.setColor(color.blue())

        for i in range(1000):
            x = random.randint(1, size.width()-1)
            y = random.randint(1, size.height()-1)
            qp.setBrush(brush)
            qp.drawRect(x, y, 10, 10)
            # time.sleep(1)
            # self.update()


            # qp.fillRect()


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()