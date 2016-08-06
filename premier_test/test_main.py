import random
import sys
import time

from PyQt4 import QtGui, QtCore
#from pinceau import Pinceau

"""
Decriptif du jeu: avoir une map 2D carrée avec des points qui se déplacent, les points noirs sont des humains, qui sont
associés coté programme a une matrice evolutive, il peuvent donc se reproduire, ont un durée de vie. toutes leur
actions sont définies par la matrice. Leur durée de vie est définie par leur abilité à se nourrir, couper des arbres
pour construire des maisons ou bouffer des animaus.

Pour l'instant je ne sais pas comment définir le temps dans le jeu, j'aimerais le séparer du temps reel.

Le but du jeu serait d'avoir une humanité qui dure le plus longtemps, mais je ne vois pas encore quelle interaction
faire avec le jeu.
"""

"""
Bon là faire attention c'est Qt4
faudra pe utiliser une QAnimation
"""


class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()  # appelle le parent en gros..
        self.setGeometry(50, 50, 500, 500)  # coordonnées de départ plus taille fenetre
        self.setWindowTitle("Demostasy")
        # self.setWindowIconText(QtGui.QIcon(''))  # définir l'image de l'icone
        # self.show()

        self.inst_widget = Widget()
        self.setCentralWidget(self.inst_widget)


        # self.boutonton()
        self.show()

    def boutonton(self):

        btn = QtGui.QPushButton("petit bouton", self)

        # btn.connect(btn, QtCore.SIGNAL("clicked()"), app, QtCore.SLOT("quit()"))  # methode genre C++
        # btn.connect(btn, QtCore.SIGNAL("clicked()"), btn, QtCore.SLOT(btn.fait_truc()))
        # btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn.clicked.connect(lambda: btn.move(60, 60))  # lambda pass l'évaluation de la fct, qui casse les C

        self.show()

    def keyPressEvent(self, e):  # si echap est pressé
        if e.key() == QtCore.Qt.Key_2:
            self.inst_widget.pos_y += 20
            time.sleep(1)  # bon là ca fait pas chier
            self.inst_widget.update()
        if e.key() == QtCore.Qt.Key_8:
            self.inst_widget.pos_y += -20
            self.inst_widget.update()
        if e.key() == QtCore.Qt.Key_4:
            self.inst_widget.pos_x += -20
            self.inst_widget.update()
        if e.key() == QtCore.Qt.Key_6:
            self.inst_widget.pos_x += 20
            self.inst_widget.update()


class Widget(QtGui.QWidget):  # là ou on trace les trucs

    def __init__(self):  # ne changer pas à l'update
        super(Widget, self).__init__()
        self.setGeometry(100, 100, 300, 300)  # change rien
        self.taille = 10
        self.pos_x = 250  # un peu inversé..
        self.pos_y = 10

        """ apparement pas de paint dans le init..
        paint1 = QtGui.QPainter()
        paint1.begin(self)
        paint1.setPen(QtCore.Qt.red)
        paint1.drawRect(100, 200, 20, 20)
        """



    def paintEvent(self, e):  # surcharge

        #qp2 = Pinceau(self)
        qp = QtGui.QPainter()
        qp.begin(self)
        color = QtGui.QColor(0, 0, 0)
        # color.blue()  # bon impossilbe d'utiliser les putain de couleur prédéfinies..

        self.taille = random.randint(10, 30)
        qp.setPen(QtCore.Qt.red)
        qp.setBrush(color)
        qp.drawEllipse(self.pos_x, self.pos_y, self.taille, 10)
        print("tracé")
        qp.end()


"""
class WidgetVue(QtGui.QWidget):

    def __init__(self):
        super(WidgetVue, self).__init__()

        btn2 = Human("bouton2", self)
        btn3 = Human("bouton3", self)

        layout_h = QtGui.QHBoxLayout()
        layout_h.addWidget(btn2)
        layout_h2 = QtGui.QHBoxLayout()
        layout_h2.addWidget(btn3)

        layout = QtGui.QVBoxLayout()  # layout vertical, principal
        layout.addLayout(layout_h2)
        layout.addLayout(layout_h)

        self.setLayout(layout)
"""

app = QtGui.QApplication(sys.argv)
gui = Window()
# app.processEvents()
sys.exit(app.exec_())  # pr que la fenetre reste
