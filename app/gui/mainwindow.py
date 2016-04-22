# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/ihor-pyvovarnyk/Documents/Workspace/oae-sound-processing-tool/resources/gui/mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(572, 342)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.groupBox = QtGui.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 551, 91))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.selected_file = QtGui.QLineEdit(self.groupBox)
        self.selected_file.setGeometry(QtCore.QRect(10, 30, 531, 21))
        self.selected_file.setReadOnly(True)
        self.selected_file.setObjectName(_fromUtf8("selected_file"))
        self.select_file_btn = QtGui.QPushButton(self.groupBox)
        self.select_file_btn.setGeometry(QtCore.QRect(430, 50, 113, 32))
        self.select_file_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.select_file_btn.setAcceptDrops(False)
        self.select_file_btn.setObjectName(_fromUtf8("select_file_btn"))
        self.invalid_file_label = QtGui.QLabel(self.groupBox)
        self.invalid_file_label.setGeometry(QtCore.QRect(10, 60, 411, 16))
        self.invalid_file_label.setObjectName(_fromUtf8("invalid_file_label"))
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 100, 551, 81))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.convert_target_ext_combo_box = QtGui.QComboBox(self.tab)
        self.convert_target_ext_combo_box.setGeometry(QtCore.QRect(170, 10, 104, 26))
        self.convert_target_ext_combo_box.setObjectName(_fromUtf8("convert_target_ext_combo_box"))
        self.convert_btn = QtGui.QPushButton(self.tab)
        self.convert_btn.setGeometry(QtCore.QRect(290, 10, 113, 32))
        self.convert_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.convert_btn.setObjectName(_fromUtf8("convert_btn"))
        self.select_extension_label = QtGui.QLabel(self.tab)
        self.select_extension_label.setGeometry(QtCore.QRect(10, 10, 151, 31))
        self.select_extension_label.setObjectName(_fromUtf8("select_extension_label"))
        self.convert_status_label = QtGui.QLabel(self.tab)
        self.convert_status_label.setGeometry(QtCore.QRect(420, 10, 111, 31))
        self.convert_status_label.setObjectName(_fromUtf8("convert_status_label"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 572, 22))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "Select file", None))
        self.select_file_btn.setText(_translate("MainWindow", "Select File", None))
        self.invalid_file_label.setText(_translate("MainWindow", "Wrong file format", None))
        self.convert_btn.setText(_translate("MainWindow", "Convert", None))
        self.select_extension_label.setText(_translate("MainWindow", "Select target extension", None))
        self.convert_status_label.setText(_translate("MainWindow", "convert_status_label", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Convert", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2", None))

