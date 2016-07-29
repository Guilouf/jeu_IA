from PyQt4 import QtGui
import random


class Pinceau(QtGui.QPainter):

    def __init__(self, daron):  # change à chaque update de la class parent
        super(Pinceau, self).__init__()
        self.pos_x = random.randint(50, 500)
        self.pos_y = random.randint(50, 500)
        self.begin(daron)
        self.setPen(QtGui.QColor(100, 200, 0))
        self.setBrush(QtGui.QColor(100, 200, 0))
        self.drawRect(self.pos_x, self.pos_y, 10, 10)

    # def begin(self, QPaintDevice):
    #     pass