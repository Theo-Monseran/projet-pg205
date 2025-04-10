from PyQt6 import QtCore, QtGui, QtWidgets
from mainwindow import Ui_MainWindow
import effects.manager
from player import VACPlayer

class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.player = VACPlayer(device=(1, 6))

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.__setup_mouse_events()
        
        
    def __setup_mouse_events(self):
        for effect, rb in self.ui.get_radio_buttons().items():
            rb.effect = effect
            rb.effectSelected.connect(lambda e: effects.manager.set_effect(e, True))

        startButton = self.ui.get_start_button()
        startButton.clicked.connect(self.player.toggle)
        startButton.clicked.connect(lambda _: startButton.setText("Stop") if self.player.active else startButton.setText("Start"))

def log(event):
    print(f"Event : {event} | Type : {type(event)}")

if __name__ == "__main__":
    import sys

    effects.manager.setup()

    app = QtWidgets.QApplication(sys.argv)
    win = UI()
    win.show()
    
    
    sys.exit(app.exec())
