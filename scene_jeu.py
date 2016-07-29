import sys
from PyQt4 import QtGui, QtCore

from humain import Humain
import time

class SceneJeu(QtGui.QGraphicsView):
    def __init__(self):
        super().__init__()

        self.scene = QtGui.QGraphicsScene(self)
        self.setScene(self.scene)
        self.setRenderHint(QtGui.QPainter.Antialiasing)

        self.scene.setSceneRect(0, 0, 500, 500)
        mypen = QtGui.QPen(QtCore.Qt.red)
        # top left etc n'est pas detecté par l'introspection
        top_line = QtCore.QLineF(self.scene.sceneRect().topLeft(), self.scene.sceneRect().topRight())
        left_line = QtCore.QLineF(self.scene.sceneRect().topLeft(), self.scene.sceneRect().bottomLeft())
        right_line = QtCore.QLineF(self.scene.sceneRect().topRight(), self.scene.sceneRect().bottomRight())
        bottom_line = QtCore.QLineF(self.scene.sceneRect().bottomLeft(), self.scene.sceneRect().bottomRight())

        self.scene.addLine(top_line, mypen)
        self.scene.addLine(left_line, mypen)
        self.scene.addLine(right_line, mypen)
        self.scene.addLine(bottom_line, mypen)

        item_count = 10
        for i in range(0, item_count):
            item = Humain()

            self.scene.addItem(item)


        timer = QtCore.QTimer(self)
        self.connect(timer, QtCore.SIGNAL("timeout()"), self.scene, QtCore.SLOT("advance()"))
        # a chaque fois que le timer est finit, il envoit un signal à advance.
        timer.start(100)

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    view = SceneJeu()
    view.show()
    sys.exit(app.exec_())