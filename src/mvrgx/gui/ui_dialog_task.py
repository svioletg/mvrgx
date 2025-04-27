# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_task.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QLabel,
    QListWidget, QListWidgetItem, QProgressBar, QSizePolicy,
    QWidget)

class Ui_DialogTask(object):
    def setupUi(self, DialogTask):
        if not DialogTask.objectName():
            DialogTask.setObjectName(u"DialogTask")
        DialogTask.resize(400, 250)
        self.listWidgetStatus = QListWidget(DialogTask)
        self.listWidgetStatus.setObjectName(u"listWidgetStatus")
        self.listWidgetStatus.setGeometry(QRect(20, 59, 350, 151))
        self.listWidgetStatus.setAlternatingRowColors(False)
        self.listWidgetStatus.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.listWidgetStatus.setWordWrap(True)
        self.progressBar = QProgressBar(DialogTask)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 210, 350, 20))
        self.progressBar.setValue(24)
        self.labelMessage = QLabel(DialogTask)
        self.labelMessage.setObjectName(u"labelMessage")
        self.labelMessage.setGeometry(QRect(20, 20, 350, 40))
        self.labelMessage.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.retranslateUi(DialogTask)

        QMetaObject.connectSlotsByName(DialogTask)
    # setupUi

    def retranslateUi(self, DialogTask):
        DialogTask.setWindowTitle(QCoreApplication.translate("DialogTask", u"Dialog", None))
        self.labelMessage.setText(QCoreApplication.translate("DialogTask", u"MESSAGE", None))
    # retranslateUi

