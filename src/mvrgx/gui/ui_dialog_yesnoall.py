# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_yesnoall.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QGridLayout, QLabel, QSizePolicy,
    QWidget)
from . import icons_rc

class Ui_DialogYNAll(object):
    def setupUi(self, DialogYNAll):
        if not DialogYNAll.objectName():
            DialogYNAll.setObjectName(u"DialogYNAll")
        DialogYNAll.resize(400, 150)
        self.gridLayout = QGridLayout(DialogYNAll)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBoxYN = QDialogButtonBox(DialogYNAll)
        self.buttonBoxYN.setObjectName(u"buttonBoxYN")
        self.buttonBoxYN.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBoxYN.setStandardButtons(QDialogButtonBox.StandardButton.No|QDialogButtonBox.StandardButton.Yes)
        self.buttonBoxYN.setCenterButtons(True)

        self.gridLayout.addWidget(self.buttonBoxYN, 1, 0, 1, 1)

        self.labelMessage = QLabel(DialogYNAll)
        self.labelMessage.setObjectName(u"labelMessage")
        self.labelMessage.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelMessage.setWordWrap(True)

        self.gridLayout.addWidget(self.labelMessage, 0, 0, 1, 1)

        self.checkBoxForAll = QCheckBox(DialogYNAll)
        self.checkBoxForAll.setObjectName(u"checkBoxForAll")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBoxForAll.sizePolicy().hasHeightForWidth())
        self.checkBoxForAll.setSizePolicy(sizePolicy)
        self.checkBoxForAll.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.checkBoxForAll.setAutoFillBackground(False)
        self.checkBoxForAll.setChecked(False)

        self.gridLayout.addWidget(self.checkBoxForAll, 2, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.retranslateUi(DialogYNAll)
        self.buttonBoxYN.accepted.connect(DialogYNAll.accept)
        self.buttonBoxYN.rejected.connect(DialogYNAll.reject)

        QMetaObject.connectSlotsByName(DialogYNAll)
    # setupUi

    def retranslateUi(self, DialogYNAll):
        DialogYNAll.setWindowTitle(QCoreApplication.translate("DialogYNAll", u"Dialog", None))
        self.labelMessage.setText(QCoreApplication.translate("DialogYNAll", u"MESSAGE", None))
        self.checkBoxForAll.setText(QCoreApplication.translate("DialogYNAll", u"Do this for remaining actions?", None))
    # retranslateUi

