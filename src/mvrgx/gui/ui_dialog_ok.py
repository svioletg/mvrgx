# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_ok.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_DialogOK(object):
    def setupUi(self, DialogOK):
        if not DialogOK.objectName():
            DialogOK.setObjectName(u"DialogOK")
        DialogOK.resize(400, 150)
        self.labelMessage = QLabel(DialogOK)
        self.labelMessage.setObjectName(u"labelMessage")
        self.labelMessage.setGeometry(QRect(20, 20, 351, 70))
        self.labelMessage.setAlignment(Qt.AlignCenter)
        self.labelMessage.setWordWrap(True)
        self.pushButtonOK = QPushButton(DialogOK)
        self.pushButtonOK.setObjectName(u"pushButtonOK")
        self.pushButtonOK.setGeometry(QRect(140, 100, 100, 30))

        self.retranslateUi(DialogOK)
        self.pushButtonOK.clicked.connect(DialogOK.accept)

        QMetaObject.connectSlotsByName(DialogOK)
    # setupUi

    def retranslateUi(self, DialogOK):
        DialogOK.setWindowTitle(QCoreApplication.translate("DialogOK", u"Dialog", None))
        self.labelMessage.setText(QCoreApplication.translate("DialogOK", u"MESSAGE", None))
        self.pushButtonOK.setText(QCoreApplication.translate("DialogOK", u"OK", None))
    # retranslateUi

