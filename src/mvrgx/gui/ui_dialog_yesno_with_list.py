# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_yesno_with_list.ui'
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
    QGridLayout, QLabel, QListWidget, QListWidgetItem,
    QSizePolicy, QWidget)

class Ui_DialogYNList(object):
    def setupUi(self, DialogYNList):
        if not DialogYNList.objectName():
            DialogYNList.setObjectName(u"DialogYNList")
        DialogYNList.resize(400, 300)
        self.gridLayout = QGridLayout(DialogYNList)
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelMessage = QLabel(DialogYNList)
        self.labelMessage.setObjectName(u"labelMessage")
        self.labelMessage.setStyleSheet(u"padding: 1em;")
        self.labelMessage.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelMessage.setWordWrap(True)

        self.gridLayout.addWidget(self.labelMessage, 0, 0, 1, 1)

        self.listWidget = QListWidget(DialogYNList)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 1)

        self.buttonBoxYN = QDialogButtonBox(DialogYNList)
        self.buttonBoxYN.setObjectName(u"buttonBoxYN")
        self.buttonBoxYN.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBoxYN.setStandardButtons(QDialogButtonBox.StandardButton.No|QDialogButtonBox.StandardButton.Yes)
        self.buttonBoxYN.setCenterButtons(True)

        self.gridLayout.addWidget(self.buttonBoxYN, 2, 0, 1, 1)


        self.retranslateUi(DialogYNList)
        self.buttonBoxYN.accepted.connect(DialogYNList.accept)
        self.buttonBoxYN.rejected.connect(DialogYNList.reject)

        QMetaObject.connectSlotsByName(DialogYNList)
    # setupUi

    def retranslateUi(self, DialogYNList):
        DialogYNList.setWindowTitle(QCoreApplication.translate("DialogYNList", u"Dialog", None))
        self.labelMessage.setText(QCoreApplication.translate("DialogYNList", u"MESSAGE", None))
    # retranslateUi

