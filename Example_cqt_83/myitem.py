from PyQt4 import QtGui, QtCore



class Myitem(QtGui.QGraphicsItem):
    
    def __init__(self):
        super(Myitem, self).__init__()

        # rotation de départ
        angle = (QtCore.qrand() % 360)
        self.setRotation(angle)

        # la vitesse (nb de pixel)
        self.speed = 5

        # position de départ aléatoire
        start_x = 0
        start_y = 0

        if (QtCore.qrand() % 1):  # en gros un booleen true flase..
            start_x = QtCore.qrand() % 200
            start_y = QtCore.qrand() % 200
        else:
            start_x = QtCore.qrand() % -100
            start_y = QtCore.qrand() % -100

        self.setPos(self.mapToParent(start_x, start_y))

    def boundingRect(self):
        return QtCore.QRectF(0, 0, 20, 20)  # a la base ct Qrect, j'aim mis QrectF

    def paint(self, QPainter, QStyleOptionGraphicsItem, QWidget_widget=None):
        rec = self.boundingRect()
        brush = QtGui.QBrush(QtCore.Qt.gray)

        # detection de collision
        # if(scene()->collidingItems(this).isEmpty())
        if not self.scene().collidingItems(self):
            brush.setColor(QtCore.Qt.green)
        else:
            brush.setColor(QtCore.Qt.red)
            self.docollision()

        QPainter.fillRect(rec, brush)
        QPainter.drawRect(rec)

    def advance(self, phase):

        if not phase:  # si phase == None (a voir si ca amrche..)
            return

        location = self.pos()
        self.setPos(self.mapToParent(0, -self.speed))

    def docollision(self):

        # changement d'angle random
        if QtCore.qrand() % 1:  # en gros un booleen true flase..
            self.setRotation(self.rotation() + (180 + QtCore.qrand() % 10))
        else:
            self.setRotation(self.rotation() + (180 + QtCore.qrand() % -10))

        new_point = self.mapToParent(-self.boundingRect().width(), -self.boundingRect().width() + 2)

        if not self.scene().sceneRect().contains(new_point):
            new_point = self.mapToParent(0, 0)
        else:
            self.setPos(new_point)