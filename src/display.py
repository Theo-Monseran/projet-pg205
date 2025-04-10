from PyQt6 import QtCore, QtGui, QtWidgets
from mainwindow import Ui_MainWindow
import audio

class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = UI()
    win.show()
    
    audio.setup()
    
    sys.exit(app.exec())
