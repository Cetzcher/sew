import sys, model
import controller as cntrl
from view import *
from PySide import QtGui

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    win = QtGui.QMainWindow()
    # create model view and controller.
    view = Ui_MyGame()

    view.setupUi(win)  # this initializes the created UI
    mod = model.Model()
    cnt = cntrl.Controller(mod, view)

    win.show()
    app.exec_()
    sys.exit()