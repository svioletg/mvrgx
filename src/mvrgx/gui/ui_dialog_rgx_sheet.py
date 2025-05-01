# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_rgx_sheet.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QWidget)

class Ui_DialogRgxSheet(object):
    def setupUi(self, DialogRgxSheet):
        if not DialogRgxSheet.objectName():
            DialogRgxSheet.setObjectName(u"DialogRgxSheet")
        DialogRgxSheet.resize(400, 400)
        self.labelLeftSide = QLabel(DialogRgxSheet)
        self.labelLeftSide.setObjectName(u"labelLeftSide")
        self.labelLeftSide.setGeometry(QRect(20, 20, 170, 360))
        self.labelLeftSide.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelRightSide = QLabel(DialogRgxSheet)
        self.labelRightSide.setObjectName(u"labelRightSide")
        self.labelRightSide.setGeometry(QRect(210, 20, 170, 360))

        self.retranslateUi(DialogRgxSheet)

        QMetaObject.connectSlotsByName(DialogRgxSheet)
    # setupUi

    def retranslateUi(self, DialogRgxSheet):
        DialogRgxSheet.setWindowTitle(QCoreApplication.translate("DialogRgxSheet", u"Dialog", None))
        self.labelLeftSide.setText(QCoreApplication.translate("DialogRgxSheet", u"<html><head/><body><p>Paths with extensions</p></body></html>", None))
        self.labelRightSide.setText(QCoreApplication.translate("DialogRgxSheet", u"<html><head/><body><p>^\\. \u2026 \\..+$</p></body></html>", None))
    # retranslateUi

