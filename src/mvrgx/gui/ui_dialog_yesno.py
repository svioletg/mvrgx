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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 200)
        self.buttonBoxYN = QDialogButtonBox(Dialog)
        self.buttonBoxYN.setObjectName(u"buttonBoxYN")
        self.buttonBoxYN.setGeometry(QRect(20, 140, 350, 32))
        self.buttonBoxYN.setOrientation(Qt.Horizontal)
        self.buttonBoxYN.setStandardButtons(QDialogButtonBox.No|QDialogButtonBox.Yes)
        self.buttonBoxYN.setCenterButtons(True)
        self.labelMessage = QLabel(Dialog)
        self.labelMessage.setObjectName(u"labelMessage")
        self.labelMessage.setGeometry(QRect(20, 20, 350, 110))
        self.labelMessage.setAlignment(Qt.AlignCenter)
        self.labelMessage.setWordWrap(True)

        self.retranslateUi(Dialog)
        self.buttonBoxYN.accepted.connect(Dialog.accept)
        self.buttonBoxYN.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.labelMessage.setText(QCoreApplication.translate("Dialog", u"MESSAGE", None))
    # retranslateUi

