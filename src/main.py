from PyQt6 import QtCore, QtGui, QtWidgets
from mainwindow import Ui_MainWindow
import effects.manager

class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

def log(event):
    print(f"Event : {event} | Type : {type(event)}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = UI()
    win.show()
    for effect, rb in win.ui.get_radio_buttons().items():
        rb.effect = effect
        rb.effectSelected.connect(lambda e: effects.manager.set_effect(e, True))

    effects.manager.setup()
    
    sys.exit(app.exec())
