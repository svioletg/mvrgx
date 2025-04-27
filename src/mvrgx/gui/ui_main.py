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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)
from . import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.labelSrcDir = QLabel(self.centralwidget)
        self.labelSrcDir.setObjectName(u"labelSrcDir")
        self.labelSrcDir.setGeometry(QRect(20, 10, 371, 20))
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
        self.labelSrcDirErrMsg = QLabel(self.centralwidget)
        self.labelSrcDirErrMsg.setObjectName(u"labelSrcDirErrMsg")
        self.labelSrcDirErrMsg.setEnabled(True)
        self.labelSrcDirErrMsg.setGeometry(QRect(400, 40, 161, 21))
        self.labelSrcDirErrMsg.setStyleSheet(u"color: rgb(246, 97, 81);")
        self.listWidgetSrcContents = QListWidget(self.centralwidget)
        self.listWidgetSrcContents.setObjectName(u"listWidgetSrcContents")
        self.listWidgetSrcContents.setGeometry(QRect(20, 70, 760, 111))
        self.labelSrcDirCount = QLabel(self.centralwidget)
        self.labelSrcDirCount.setObjectName(u"labelSrcDirCount")
        self.labelSrcDirCount.setGeometry(QRect(20, 180, 361, 30))
        self.lineEditInputRegex = QLineEdit(self.centralwidget)
        self.lineEditInputRegex.setObjectName(u"lineEditInputRegex")
        self.lineEditInputRegex.setGeometry(QRect(20, 260, 360, 20))
        self.lineEditOutputPattern = QLineEdit(self.centralwidget)
        self.lineEditOutputPattern.setObjectName(u"lineEditOutputPattern")
        self.lineEditOutputPattern.setGeometry(QRect(420, 260, 360, 20))
        self.pushButtonRenameFiles = QPushButton(self.centralwidget)
        self.pushButtonRenameFiles.setObjectName(u"pushButtonRenameFiles")
        self.pushButtonRenameFiles.setEnabled(False)
        self.pushButtonRenameFiles.setGeometry(QRect(20, 540, 761, 40))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 210, 760, 3))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.listWidgetMvBefore = QListWidget(self.centralwidget)
        self.listWidgetMvBefore.setObjectName(u"listWidgetMvBefore")
        self.listWidgetMvBefore.setGeometry(QRect(20, 290, 360, 230))
        self.listWidgetMvAfter = QListWidget(self.centralwidget)
        self.listWidgetMvAfter.setObjectName(u"listWidgetMvAfter")
        self.listWidgetMvAfter.setGeometry(QRect(420, 289, 360, 230))
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(400, 220, 3, 300))
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 240, 360, 24))
        self.horizontalLayoutInputRegex = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayoutInputRegex.setObjectName(u"horizontalLayoutInputRegex")
        self.horizontalLayoutInputRegex.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayoutInputRegex.setContentsMargins(0, 0, 0, 0)
        self.labelInputRegex = QLabel(self.horizontalLayoutWidget)
        self.labelInputRegex.setObjectName(u"labelInputRegex")

        self.horizontalLayoutInputRegex.addWidget(self.labelInputRegex)

        self.checkBoxRecursive = QCheckBox(self.horizontalLayoutWidget)
        self.checkBoxRecursive.setObjectName(u"checkBoxRecursive")
        self.checkBoxRecursive.setAutoFillBackground(False)
        self.checkBoxRecursive.setStyleSheet(u"")
        self.checkBoxRecursive.setChecked(False)
        self.checkBoxRecursive.setTristate(False)

        self.horizontalLayoutInputRegex.addWidget(self.checkBoxRecursive)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutInputRegex.addItem(self.horizontalSpacer)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(420, 240, 351, 22))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.labelOutputPattern = QLabel(self.horizontalLayoutWidget_2)
        self.labelOutputPattern.setObjectName(u"labelOutputPattern")

        self.horizontalLayout_2.addWidget(self.labelOutputPattern)

        self.labelOutputPatternWarning = QLabel(self.horizontalLayoutWidget_2)
        self.labelOutputPatternWarning.setObjectName(u"labelOutputPatternWarning")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelOutputPatternWarning.sizePolicy().hasHeightForWidth())
        self.labelOutputPatternWarning.setSizePolicy(sizePolicy1)
        self.labelOutputPatternWarning.setMaximumSize(QSize(16, 16))
        self.labelOutputPatternWarning.setPixmap(QPixmap(u":/icon/img/warning.svg"))
        self.labelOutputPatternWarning.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.labelOutputPatternWarning)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelSrcDir.setText(QCoreApplication.translate("MainWindow", u"Source directory", None))
        self.pushButtonSrcBrowse.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.labelSrcDirErrMsg.setText(QCoreApplication.translate("MainWindow", u"Invalid directory.", None))
        self.labelSrcDirCount.setText(QCoreApplication.translate("MainWindow", u"0 items", None))
        self.pushButtonRenameFiles.setText(QCoreApplication.translate("MainWindow", u"Rename files", None))
        self.labelInputRegex.setText(QCoreApplication.translate("MainWindow", u"Input regex", None))
        self.checkBoxRecursive.setText(QCoreApplication.translate("MainWindow", u"Recursive", None))
        self.labelOutputPattern.setText(QCoreApplication.translate("MainWindow", u"Output pattern", None))
        self.labelOutputPatternWarning.setText("")
    # retranslateUi

