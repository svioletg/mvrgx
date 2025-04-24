# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.labelSrcDir = QLabel(self.centralwidget)
        self.labelSrcDir.setObjectName(u"labelSrcDir")
        self.labelSrcDir.setGeometry(QRect(20, 10, 371, 21))
        self.pushButtonSrcBrowse = QPushButton(self.centralwidget)
        self.pushButtonSrcBrowse.setObjectName(u"pushButtonSrcBrowse")
        self.pushButtonSrcBrowse.setGeometry(QRect(20, 40, 71, 21))
        self.lineEditSrcDir = QLineEdit(self.centralwidget)
        self.lineEditSrcDir.setObjectName(u"lineEditSrcDir")
        self.lineEditSrcDir.setGeometry(QRect(100, 40, 290, 20))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditSrcDir.sizePolicy().hasHeightForWidth())
        self.lineEditSrcDir.setSizePolicy(sizePolicy)
        self.labelSrcDirMissing = QLabel(self.centralwidget)
        self.labelSrcDirMissing.setObjectName(u"labelSrcDirMissing")
        self.labelSrcDirMissing.setEnabled(True)
        self.labelSrcDirMissing.setGeometry(QRect(400, 40, 161, 21))
        self.labelSrcDirMissing.setStyleSheet(u"color: rgb(246, 97, 81);")
        self.listWidgetSrcContents = QListWidget(self.centralwidget)
        self.listWidgetSrcContents.setObjectName(u"listWidgetSrcContents")
        self.listWidgetSrcContents.setGeometry(QRect(20, 70, 760, 111))
        self.labelSrcDirCount = QLabel(self.centralwidget)
        self.labelSrcDirCount.setObjectName(u"labelSrcDirCount")
        self.labelSrcDirCount.setGeometry(QRect(20, 180, 361, 30))
        self.labelInputRegex = QLabel(self.centralwidget)
        self.labelInputRegex.setObjectName(u"labelInputRegex")
        self.labelInputRegex.setGeometry(QRect(20, 220, 360, 20))
        self.lineEditInputRegex = QLineEdit(self.centralwidget)
        self.lineEditInputRegex.setObjectName(u"lineEditInputRegex")
        self.lineEditInputRegex.setGeometry(QRect(20, 260, 360, 20))
        self.lineEditOutputPattern = QLineEdit(self.centralwidget)
        self.lineEditOutputPattern.setObjectName(u"lineEditOutputPattern")
        self.lineEditOutputPattern.setGeometry(QRect(420, 260, 360, 20))
        self.labelOutputPattern = QLabel(self.centralwidget)
        self.labelOutputPattern.setObjectName(u"labelOutputPattern")
        self.labelOutputPattern.setGeometry(QRect(420, 220, 360, 20))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 550, 761, 40))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 210, 760, 3))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.listWidgetMvBefore = QListWidget(self.centralwidget)
        self.listWidgetMvBefore.setObjectName(u"listWidgetMvBefore")
        self.listWidgetMvBefore.setGeometry(QRect(20, 290, 360, 191))
        self.listWidgetMvAfter = QListWidget(self.centralwidget)
        self.listWidgetMvAfter.setObjectName(u"listWidgetMvAfter")
        self.listWidgetMvAfter.setGeometry(QRect(420, 289, 360, 191))
        self.checkBoxRecursive = QCheckBox(self.centralwidget)
        self.checkBoxRecursive.setObjectName(u"checkBoxRecursive")
        self.checkBoxRecursive.setGeometry(QRect(20, 240, 360, 20))
        self.checkBoxRecursive.setAutoFillBackground(False)
        self.checkBoxRecursive.setStyleSheet(u"")
        self.checkBoxRecursive.setChecked(False)
        self.checkBoxRecursive.setTristate(False)
        self.labelOutputPatternMissing = QLabel(self.centralwidget)
        self.labelOutputPatternMissing.setObjectName(u"labelOutputPatternMissing")
        self.labelOutputPatternMissing.setGeometry(QRect(420, 240, 360, 20))
        self.labelOutputPatternMissing.setStyleSheet(u"color: rgb(246, 97, 81);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelSrcDir.setText(QCoreApplication.translate("MainWindow", u"Source directory", None))
        self.pushButtonSrcBrowse.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.labelSrcDirMissing.setText(QCoreApplication.translate("MainWindow", u"Invalid directory.", None))
        self.labelSrcDirCount.setText(QCoreApplication.translate("MainWindow", u"0 items", None))
        self.labelInputRegex.setText(QCoreApplication.translate("MainWindow", u"Input regex", None))
        self.labelOutputPattern.setText(QCoreApplication.translate("MainWindow", u"Output pattern", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Rename files", None))
        self.checkBoxRecursive.setText(QCoreApplication.translate("MainWindow", u"Recursive", None))
        self.labelOutputPatternMissing.setText(QCoreApplication.translate("MainWindow", u"Cannot be empty.", None))
    # retranslateUi

