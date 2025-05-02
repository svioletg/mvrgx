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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_DialogOK(object):
    def setupUi(self, DialogOK):
        if not DialogOK.objectName():
            DialogOK.setObjectName(u"DialogOK")
        DialogOK.resize(400, 150)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogOK.sizePolicy().hasHeightForWidth())
        DialogOK.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(DialogOK)
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelMessage = QLabel(DialogOK)
        self.labelMessage.setObjectName(u"labelMessage")
        sizePolicy.setHeightForWidth(self.labelMessage.sizePolicy().hasHeightForWidth())
        self.labelMessage.setSizePolicy(sizePolicy)
        self.labelMessage.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelMessage.setWordWrap(True)

        self.gridLayout.addWidget(self.labelMessage, 0, 0, 1, 1)

        self.pushButtonOK = QPushButton(DialogOK)
        self.pushButtonOK.setObjectName(u"pushButtonOK")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButtonOK.sizePolicy().hasHeightForWidth())
        self.pushButtonOK.setSizePolicy(sizePolicy1)
        self.pushButtonOK.setAutoFillBackground(False)
        self.pushButtonOK.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButtonOK, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.pushButtonOK.raise_()
        self.labelMessage.raise_()

        self.retranslateUi(DialogOK)
        self.pushButtonOK.clicked.connect(DialogOK.accept)

        QMetaObject.connectSlotsByName(DialogOK)
    # setupUi

    def retranslateUi(self, DialogOK):
        DialogOK.setWindowTitle(QCoreApplication.translate("DialogOK", u"Dialog", None))
        self.labelMessage.setText(QCoreApplication.translate("DialogOK", u"MESSAGE", None))
        self.pushButtonOK.setText(QCoreApplication.translate("DialogOK", u"OK", None))
    # retranslateUi

