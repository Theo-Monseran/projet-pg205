from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenuBar, QRadioButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(964, 771)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(180, 150, 561, 281))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(8, 8, 8, 8)
        self.iconNoEffect = QLabel(self.gridLayoutWidget)
        self.iconNoEffect.setObjectName(u"iconLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iconNoEffect.sizePolicy().hasHeightForWidth())
        self.iconNoEffect.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.iconNoEffect)

        self.radioNoEffect = QRadioButton(self.gridLayoutWidget)
        self.radioNoEffect.setObjectName(u"radioButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.radioNoEffect.sizePolicy().hasHeightForWidth())
        self.radioNoEffect.setSizePolicy(sizePolicy1)
        self.radioNoEffect.setChecked(True)

        self.verticalLayout.addWidget(self.radioNoEffect)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(8, 8, 8, 8)
        self.iconTremolo = QLabel(self.gridLayoutWidget)
        self.iconTremolo.setObjectName(u"iconLabel_3")
        sizePolicy.setHeightForWidth(self.iconTremolo.sizePolicy().hasHeightForWidth())
        self.iconTremolo.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.iconTremolo)

        self.radioTremolo = QRadioButton(self.gridLayoutWidget)
        self.radioTremolo.setObjectName(u"radioButton_5")
        sizePolicy1.setHeightForWidth(self.radioTremolo.sizePolicy().hasHeightForWidth())
        self.radioTremolo.setSizePolicy(sizePolicy1)
        self.radioTremolo.setChecked(True)

        self.verticalLayout_3.addWidget(self.radioTremolo)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 1, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(8, 8, 8, 8)
        self.iconVibrato = QLabel(self.gridLayoutWidget)
        self.iconVibrato.setObjectName(u"iconLabel_4")
        sizePolicy.setHeightForWidth(self.iconVibrato.sizePolicy().hasHeightForWidth())
        self.iconVibrato.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.iconVibrato)

        self.radioVibrato = QRadioButton(self.gridLayoutWidget)
        self.radioVibrato.setObjectName(u"radioButton_6")
        sizePolicy1.setHeightForWidth(self.radioVibrato.sizePolicy().hasHeightForWidth())
        self.radioVibrato.setSizePolicy(sizePolicy1)
        self.radioVibrato.setChecked(True)

        self.verticalLayout_4.addWidget(self.radioVibrato)


        self.gridLayout.addLayout(self.verticalLayout_4, 0, 2, 1, 1)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(8, 8, 8, 8)
        self.iconApplyFile = QLabel(self.gridLayoutWidget)
        self.iconApplyFile.setObjectName(u"iconLabel_8")
        sizePolicy.setHeightForWidth(self.iconApplyFile.sizePolicy().hasHeightForWidth())
        self.iconApplyFile.setSizePolicy(sizePolicy)

        self.verticalLayout_8.addWidget(self.iconApplyFile)

        self.radioApplyFile = QRadioButton(self.gridLayoutWidget)
        self.radioApplyFile.setObjectName(u"radioButton_9")
        sizePolicy1.setHeightForWidth(self.radioApplyFile.sizePolicy().hasHeightForWidth())
        self.radioApplyFile.setSizePolicy(sizePolicy1)
        self.radioApplyFile.setChecked(True)

        self.verticalLayout_8.addWidget(self.radioApplyFile)


        self.gridLayout.addLayout(self.verticalLayout_8, 1, 0, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(8, 8, 8, 8)
        self.iconLowPassFilter = QLabel(self.gridLayoutWidget)
        self.iconLowPassFilter.setObjectName(u"iconLabel_9")
        sizePolicy.setHeightForWidth(self.iconLowPassFilter.sizePolicy().hasHeightForWidth())
        self.iconLowPassFilter.setSizePolicy(sizePolicy)

        self.verticalLayout_9.addWidget(self.iconLowPassFilter)

        self.radioLowPassFilter = QRadioButton(self.gridLayoutWidget)
        self.radioLowPassFilter.setObjectName(u"radioButton_10")
        sizePolicy1.setHeightForWidth(self.radioLowPassFilter.sizePolicy().hasHeightForWidth())
        self.radioLowPassFilter.setSizePolicy(sizePolicy1)
        self.radioLowPassFilter.setChecked(True)

        self.verticalLayout_9.addWidget(self.radioLowPassFilter)


        self.gridLayout.addLayout(self.verticalLayout_9, 1, 1, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(8, 8, 8, 8)
        self.iconHighPassFilter = QLabel(self.gridLayoutWidget)
        self.iconHighPassFilter.setObjectName(u"iconLabel_10")
        sizePolicy.setHeightForWidth(self.iconHighPassFilter.sizePolicy().hasHeightForWidth())
        self.iconHighPassFilter.setSizePolicy(sizePolicy)

        self.verticalLayout_10.addWidget(self.iconHighPassFilter)

        self.radioHighPassFilter = QRadioButton(self.gridLayoutWidget)
        self.radioHighPassFilter.setObjectName(u"radioButton_11")
        sizePolicy1.setHeightForWidth(self.radioHighPassFilter.sizePolicy().hasHeightForWidth())
        self.radioHighPassFilter.setSizePolicy(sizePolicy1)
        self.radioHighPassFilter.setChecked(True)

        self.verticalLayout_10.addWidget(self.radioHighPassFilter)


        self.gridLayout.addLayout(self.verticalLayout_10, 1, 2, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 40, 351, 71))
        font = QFont()
        font.setFamilies([u"Segoe Print"])
        font.setPointSize(36)
        font.setBold(True)
        self.label.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 964, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.iconNoEffect.setText(QCoreApplication.translate("MainWindow", u"Icon", None))
        self.radioNoEffect.setText(QCoreApplication.translate("MainWindow", u"No Effect", None))
        self.iconTremolo.setText(QCoreApplication.translate("MainWindow", u"Icon", None))
        self.radioTremolo.setText(QCoreApplication.translate("MainWindow", u"Tremolo", None))
        self.iconVibrato.setText(QCoreApplication.translate("MainWindow", u"Icon", None))
        self.radioVibrato.setText(QCoreApplication.translate("MainWindow", u"Vibrato", None))
        self.iconApplyFile.setText(QCoreApplication.translate("MainWindow", u"Icon", None))
        self.radioApplyFile.setText(QCoreApplication.translate("MainWindow", u"Apply file", None))
        self.iconLowPassFilter.setText(QCoreApplication.translate("MainWindow", u"Icon", None))
        self.radioLowPassFilter.setText(QCoreApplication.translate("MainWindow", u"Low pass filter", None))
        self.iconHighPassFilter.setText(QCoreApplication.translate("MainWindow", u"Icon", None))
        self.radioHighPassFilter.setText(QCoreApplication.translate("MainWindow", u"High pass filter", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Open Vocoder", None))
    # retranslateUi
