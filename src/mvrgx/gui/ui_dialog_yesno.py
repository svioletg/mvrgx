# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_yesno.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QSizePolicy, QWidget)

class Ui_DialogYN(object):
    def setupUi(self, DialogYN):
        if not DialogYN.objectName():
            DialogYN.setObjectName(u"DialogYN")
        DialogYN.resize(400, 150)
        self.buttonBoxYN = QDialogButtonBox(DialogYN)
        self.buttonBoxYN.setObjectName(u"buttonBoxYN")
        self.buttonBoxYN.setGeometry(QRect(20, 100, 360, 32))
        self.buttonBoxYN.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBoxYN.setStandardButtons(QDialogButtonBox.StandardButton.No|QDialogButtonBox.StandardButton.Yes)
        self.buttonBoxYN.setCenterButtons(True)
        self.labelMessage = QLabel(DialogYN)
        self.labelMessage.setObjectName(u"labelMessage")
        self.labelMessage.setGeometry(QRect(20, 20, 360, 70))
        self.labelMessage.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelMessage.setWordWrap(True)

        self.retranslateUi(DialogYN)
        self.buttonBoxYN.accepted.connect(DialogYN.accept)
        self.buttonBoxYN.rejected.connect(DialogYN.reject)

        QMetaObject.connectSlotsByName(DialogYN)
    # setupUi

    def retranslateUi(self, DialogYN):
        DialogYN.setWindowTitle(QCoreApplication.translate("DialogYN", u"Dialog", None))
        self.labelMessage.setText(QCoreApplication.translate("DialogYN", u"MESSAGE", None))
    # retranslateUi

