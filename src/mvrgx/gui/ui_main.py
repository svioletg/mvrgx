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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
from . import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setProperty(u"inputValid", True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(20, 20, 20, 20)
        self.verticalLayoutTopHalf = QVBoxLayout()
        self.verticalLayoutTopHalf.setObjectName(u"verticalLayoutTopHalf")
        self.verticalLayoutTopHalf.setContentsMargins(-1, -1, -1, 0)
        self.labelSrcDir = QLabel(self.centralwidget)
        self.labelSrcDir.setObjectName(u"labelSrcDir")

        self.verticalLayoutTopHalf.addWidget(self.labelSrcDir)

        self.horizontalLayoutSrcDir = QHBoxLayout()
        self.horizontalLayoutSrcDir.setObjectName(u"horizontalLayoutSrcDir")
        self.horizontalLayoutSrcDir.setContentsMargins(-1, -1, -1, 0)
        self.pushButtonSrcBrowse = QPushButton(self.centralwidget)
        self.pushButtonSrcBrowse.setObjectName(u"pushButtonSrcBrowse")

        self.horizontalLayoutSrcDir.addWidget(self.pushButtonSrcBrowse)

        self.lineEditSrcDir = QLineEdit(self.centralwidget)
        self.lineEditSrcDir.setObjectName(u"lineEditSrcDir")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditSrcDir.sizePolicy().hasHeightForWidth())
        self.lineEditSrcDir.setSizePolicy(sizePolicy)

        self.horizontalLayoutSrcDir.addWidget(self.lineEditSrcDir)

        self.labelSrcDirErrMsg = QLabel(self.centralwidget)
        self.labelSrcDirErrMsg.setObjectName(u"labelSrcDirErrMsg")
        self.labelSrcDirErrMsg.setEnabled(True)
        self.labelSrcDirErrMsg.setStyleSheet(u"color: rgb(246, 97, 81);")

        self.horizontalLayoutSrcDir.addWidget(self.labelSrcDirErrMsg)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutSrcDir.addItem(self.horizontalSpacer_3)


        self.verticalLayoutTopHalf.addLayout(self.horizontalLayoutSrcDir)

        self.listWidgetSrcContents = QListWidget(self.centralwidget)
        self.listWidgetSrcContents.setObjectName(u"listWidgetSrcContents")

        self.verticalLayoutTopHalf.addWidget(self.listWidgetSrcContents)

        self.labelSrcDirCount = QLabel(self.centralwidget)
        self.labelSrcDirCount.setObjectName(u"labelSrcDirCount")

        self.verticalLayoutTopHalf.addWidget(self.labelSrcDirCount)


        self.verticalLayout_4.addLayout(self.verticalLayoutTopHalf)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_2)

        self.gridLayoutInOut = QGridLayout()
        self.gridLayoutInOut.setObjectName(u"gridLayoutInOut")
        self.gridLayoutInOut.setContentsMargins(-1, -1, -1, 0)
        self.listWidgetMvAfter = QListWidget(self.centralwidget)
        self.listWidgetMvAfter.setObjectName(u"listWidgetMvAfter")

        self.gridLayoutInOut.addWidget(self.listWidgetMvAfter, 2, 1, 1, 1)

        self.horizontalLayoutOutputPattern = QHBoxLayout()
        self.horizontalLayoutOutputPattern.setObjectName(u"horizontalLayoutOutputPattern")
        self.labelOutputPatternWarning = QLabel(self.centralwidget)
        self.labelOutputPatternWarning.setObjectName(u"labelOutputPatternWarning")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelOutputPatternWarning.sizePolicy().hasHeightForWidth())
        self.labelOutputPatternWarning.setSizePolicy(sizePolicy1)
        self.labelOutputPatternWarning.setMaximumSize(QSize(16, 16))
        self.labelOutputPatternWarning.setPixmap(QPixmap(u":/icon/img/warning.svg"))
        self.labelOutputPatternWarning.setScaledContents(True)

        self.horizontalLayoutOutputPattern.addWidget(self.labelOutputPatternWarning)

        self.labelOutputPattern = QLabel(self.centralwidget)
        self.labelOutputPattern.setObjectName(u"labelOutputPattern")

        self.horizontalLayoutOutputPattern.addWidget(self.labelOutputPattern)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutOutputPattern.addItem(self.horizontalSpacer_2)


        self.gridLayoutInOut.addLayout(self.horizontalLayoutOutputPattern, 0, 1, 1, 1)

        self.listWidgetMvBefore = QListWidget(self.centralwidget)
        self.listWidgetMvBefore.setObjectName(u"listWidgetMvBefore")

        self.gridLayoutInOut.addWidget(self.listWidgetMvBefore, 2, 0, 1, 1)

        self.lineEditOutputPattern = QLineEdit(self.centralwidget)
        self.lineEditOutputPattern.setObjectName(u"lineEditOutputPattern")
        self.lineEditOutputPattern.setProperty(u"inputValid", True)

        self.gridLayoutInOut.addWidget(self.lineEditOutputPattern, 1, 1, 1, 1)

        self.lineEditInputRegex = QLineEdit(self.centralwidget)
        self.lineEditInputRegex.setObjectName(u"lineEditInputRegex")
        self.lineEditInputRegex.setStyleSheet(u"font-family: \"Cascadia Mono\", monospace;")
        self.lineEditInputRegex.setText(u"(.+)\\..+$")
        self.lineEditInputRegex.setPlaceholderText(u"")

        self.gridLayoutInOut.addWidget(self.lineEditInputRegex, 1, 0, 1, 1)

        self.horizontalLayoutInputRegex = QHBoxLayout()
        self.horizontalLayoutInputRegex.setObjectName(u"horizontalLayoutInputRegex")
        self.horizontalLayoutInputRegex.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayoutInputRegex.setContentsMargins(-1, -1, 0, -1)
        self.labelInputRegexWarning = QLabel(self.centralwidget)
        self.labelInputRegexWarning.setObjectName(u"labelInputRegexWarning")
        self.labelInputRegexWarning.setMaximumSize(QSize(16, 16))
        self.labelInputRegexWarning.setPixmap(QPixmap(u":/icon/img/warning.svg"))
        self.labelInputRegexWarning.setScaledContents(True)

        self.horizontalLayoutInputRegex.addWidget(self.labelInputRegexWarning)

        self.labelInputRegex = QLabel(self.centralwidget)
        self.labelInputRegex.setObjectName(u"labelInputRegex")
        self.labelInputRegex.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayoutInputRegex.addWidget(self.labelInputRegex)

        self.checkBoxRecursive = QCheckBox(self.centralwidget)
        self.checkBoxRecursive.setObjectName(u"checkBoxRecursive")
        self.checkBoxRecursive.setAutoFillBackground(False)
        self.checkBoxRecursive.setStyleSheet(u"")
        self.checkBoxRecursive.setChecked(False)
        self.checkBoxRecursive.setTristate(False)

        self.horizontalLayoutInputRegex.addWidget(self.checkBoxRecursive)

        self.comboBoxInputFilter = QComboBox(self.centralwidget)
        self.comboBoxInputFilter.addItem("")
        self.comboBoxInputFilter.addItem("")
        self.comboBoxInputFilter.addItem("")
        self.comboBoxInputFilter.setObjectName(u"comboBoxInputFilter")
        self.comboBoxInputFilter.setEditable(False)

        self.horizontalLayoutInputRegex.addWidget(self.comboBoxInputFilter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutInputRegex.addItem(self.horizontalSpacer)


        self.gridLayoutInOut.addLayout(self.horizontalLayoutInputRegex, 0, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayoutInOut)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.pushButtonMoveFiles = QPushButton(self.centralwidget)
        self.pushButtonMoveFiles.setObjectName(u"pushButtonMoveFiles")
        self.pushButtonMoveFiles.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(3)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButtonMoveFiles.sizePolicy().hasHeightForWidth())
        self.pushButtonMoveFiles.setSizePolicy(sizePolicy2)
        self.pushButtonMoveFiles.setMinimumSize(QSize(0, 0))
        self.pushButtonMoveFiles.setStyleSheet(u"")
        self.pushButtonMoveFiles.setProperty(u"thickButton", True)

        self.horizontalLayout.addWidget(self.pushButtonMoveFiles)

        self.pushButtonUndoMove = QPushButton(self.centralwidget)
        self.pushButtonUndoMove.setObjectName(u"pushButtonUndoMove")
        self.pushButtonUndoMove.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButtonUndoMove.sizePolicy().hasHeightForWidth())
        self.pushButtonUndoMove.setSizePolicy(sizePolicy3)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditUndo))
        self.pushButtonUndoMove.setIcon(icon)
        self.pushButtonUndoMove.setCheckable(False)
        self.pushButtonUndoMove.setFlat(False)
        self.pushButtonUndoMove.setProperty(u"thickButton", True)

        self.horizontalLayout.addWidget(self.pushButtonUndoMove)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
        self.labelSrcDir.setBuddy(self.lineEditSrcDir)
        self.labelOutputPattern.setBuddy(self.lineEditOutputPattern)
        self.labelInputRegex.setBuddy(self.lineEditInputRegex)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.pushButtonSrcBrowse, self.lineEditSrcDir)
        QWidget.setTabOrder(self.lineEditSrcDir, self.listWidgetSrcContents)
        QWidget.setTabOrder(self.listWidgetSrcContents, self.checkBoxRecursive)
        QWidget.setTabOrder(self.checkBoxRecursive, self.comboBoxInputFilter)
        QWidget.setTabOrder(self.comboBoxInputFilter, self.lineEditInputRegex)
        QWidget.setTabOrder(self.lineEditInputRegex, self.listWidgetMvBefore)
        QWidget.setTabOrder(self.listWidgetMvBefore, self.lineEditOutputPattern)
        QWidget.setTabOrder(self.lineEditOutputPattern, self.listWidgetMvAfter)
        QWidget.setTabOrder(self.listWidgetMvAfter, self.pushButtonMoveFiles)
        QWidget.setTabOrder(self.pushButtonMoveFiles, self.pushButtonUndoMove)

        self.retranslateUi(MainWindow)

        self.pushButtonUndoMove.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelSrcDir.setText(QCoreApplication.translate("MainWindow", u"Source directory", None))
        self.pushButtonSrcBrowse.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.labelSrcDirErrMsg.setText(QCoreApplication.translate("MainWindow", u"Invalid directory.", None))
        self.labelSrcDirCount.setText(QCoreApplication.translate("MainWindow", u"0 items", None))
#if QT_CONFIG(tooltip)
        self.listWidgetMvAfter.setToolTip(QCoreApplication.translate("MainWindow", u"Hover over an item to see its full path", None))
#endif // QT_CONFIG(tooltip)
        self.labelOutputPatternWarning.setText("")
        self.labelOutputPattern.setText(QCoreApplication.translate("MainWindow", u"Output pattern", None))
#if QT_CONFIG(tooltip)
        self.listWidgetMvBefore.setToolTip(QCoreApplication.translate("MainWindow", u"Hover over a filename to see its full path", None))
#endif // QT_CONFIG(tooltip)
        self.lineEditOutputPattern.setText(QCoreApplication.translate("MainWindow", u"\\1", None))
        self.lineEditOutputPattern.setPlaceholderText("")
        self.labelInputRegexWarning.setText("")
        self.labelInputRegex.setText(QCoreApplication.translate("MainWindow", u"Input regex", None))
        self.checkBoxRecursive.setText(QCoreApplication.translate("MainWindow", u"Recursive", None))
        self.comboBoxInputFilter.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))
        self.comboBoxInputFilter.setItemText(1, QCoreApplication.translate("MainWindow", u"Only directories", None))
        self.comboBoxInputFilter.setItemText(2, QCoreApplication.translate("MainWindow", u"Only files", None))

#if QT_CONFIG(tooltip)
        self.comboBoxInputFilter.setToolTip(QCoreApplication.translate("MainWindow", u"Choose how to filter matched results.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonMoveFiles.setText(QCoreApplication.translate("MainWindow", u"Rename/move files", None))
        self.pushButtonUndoMove.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
    # retranslateUi

