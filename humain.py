from PyQt4 import QtGui, QtCore
import random

from matrice import Matrice

class Humain(QtGui.QGraphicsItem, Matrice):

    def __init__(self):
        super(Humain, self).__init__()
        Matrice.__init__(self)  # pour initialiser matrice, avec super ca bug

        # la vitesse (nb de pixel par fin de timer)
        self.speed = 5

        """
        L'axe des coord change avec l'orientation. faire gaffe aux collisions
        """
        start_x = random.randint(10, 300)  # changer x affecte y..
        start_y = random.randint(10, 300)
        # start_x = 200
        # start_y = 100

        self.setPos(self.mapToParent(start_x, start_y))

        # rotation de départ
        # angle = (QtCore.qrand() % 360)  # marche pas cette merde??
        angle = random.randint(0, 360)
        self.setRotation(angle)

    def boundingRect(self):  # les contours, pour les collision notament
        return QtCore.QRectF(0, 0, 20, 20)  # cercle pas trop possible apparement

    def paint(self, QPainter, QStyleOptionGraphicsItem, QWidget_widget=None):
        rec = self.boundingRect()
        brush = QtGui.QBrush(QtCore.Qt.gray)

        # detection de collision
        if not self.scene().collidingItems(self):  # si la liste des collisions est vide
            brush.setColor(QtCore.Qt.green)
        else:
            objet_colli = self.scene().collidingItems(self)[0]
            brush.setColor(QtCore.Qt.red)
            self.docollision()
            if self.reproduction(objet_colli):
                self.scene().addItem(Humain())  # ca marche, ca fait juste exploser le pc

        QPainter.setBrush(brush)
        QPainter.drawEllipse(0, 0, 20, 20)

    def advance(self, phase):
        """
        Appelée à chaque fin de timer, fait bouger la position
        :param phase:
        :return:
        """
        if not phase:  # si phase == None (je vois pas a quoi sert phase.. la simu va beacuop plus vite sans
            return

        location = self.pos()
        self.setPos(self.mapToParent(0, self.speed))

    def docollision(self):
        """
        Ya un changement d'angle à chaque collision, puis
        :return:
        """

        # changement d'angle random
        self.setRotation(self.rotation() + 180 + random.randint(-30, 30))  # ca fait une sorte de demi tour

        # du mal à comprendre ca..
        # c'est la largeur de la boite de collision, de l'objet
        new_point = self.mapToParent(-self.boundingRect().width(), -self.boundingRect().width() + 0)  # 2

        if not self.scene().sceneRect().contains(new_point):  # si le nouveau point n'existe pas dans la scene
            new_point = self.mapToParent(0, 0)
        else:
            self.setPos(new_point)
