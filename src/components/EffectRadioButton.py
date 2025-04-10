from PyQt6 import QtWidgets
from PyQt6.QtCore import pyqtSignal
from effects.manager import Effect

class EffectRadioButton(QtWidgets.QRadioButton):

    effectSelected = pyqtSignal(Effect)
    
    def __init__(self, parent):
        super().__init__(parent)
        self.effect: Effect | None = None

    def mousePressEvent(self, e):
        self.effectSelected.emit(self.effect)
        return super().mousePressEvent(e)