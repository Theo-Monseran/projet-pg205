from PyQt6 import QtCore, QtGui, QtWidgets
from mainwindow import Ui_MainWindow
import effects.manager
from player import VACPlayer

class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.player = VACPlayer(samplerate=44100, blocksize=44100//15)#device=(1, 6))
        effects.manager.blocksize = VACPlayer.blocksize
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.__setup_mouse_events()
        
    
    def __change_effect(self, e: effects.manager.Effect):
        self.player.toggle(False) # OFF
        effects.manager.set_effect(e, True)
        self.player.toggle(True) # ON


    def __setup_mouse_events(self):
        for effect, rb in self.ui.get_radio_buttons().items():
            rb.effect = effect
            rb.effectSelected.connect(self.__change_effect)

        startButton = self.ui.get_start_button()
        startButton.clicked.connect(self.player.toggle)
        startButton.clicked.connect(lambda _: startButton.setText("Stop") if self.player.active else startButton.setText("Start"))


if __name__ == "__main__":
    import sys

    effects.manager.setup()

    app = QtWidgets.QApplication(sys.argv)
    win = UI()
    win.show()
    
    
    sys.exit(app.exec())
