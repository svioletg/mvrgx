# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_process.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QListWidget,
    QListWidgetItem, QSizePolicy, QWidget)

class Ui_DialogProcess(object):
    def setupUi(self, DialogProcess):
        if not DialogProcess.objectName():
            DialogProcess.setObjectName(u"DialogProcess")
        DialogProcess.resize(400, 200)
        self.listWidgetStatus = QListWidget(DialogProcess)
        self.listWidgetStatus.setObjectName(u"listWidgetStatus")
        self.listWidgetStatus.setGeometry(QRect(20, 40, 350, 130))
        self.listWidgetStatus.setAlternatingRowColors(False)
        self.listWidgetStatus.setSelectionMode(QAbstractItemView.NoSelection)
        self.listWidgetStatus.setWordWrap(True)

        self.retranslateUi(DialogProcess)

        QMetaObject.connectSlotsByName(DialogProcess)
    # setupUi

    def retranslateUi(self, DialogProcess):
        DialogProcess.setWindowTitle(QCoreApplication.translate("DialogProcess", u"Dialog", None))
    # retranslateUi

