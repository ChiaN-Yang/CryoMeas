# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './qtdesign/main_window_qt.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1656, 962)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setMouseTracking(False)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setMouseTracking(False)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setMouseTracking(False)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 2, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_3.addWidget(self.textBrowser, 1, 0, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.tab)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_3.addWidget(self.listWidget, 1, 1, 1, 1)
        self.listWidget_2 = QtWidgets.QListWidget(self.tab)
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout_3.addWidget(self.listWidget_2, 1, 2, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 2, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_3.addWidget(self.lineEdit, 2, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 2, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setMouseTracking(False)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 3, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(225)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(125)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(28)
        self.tableWidget.verticalHeader().setMinimumSectionSize(28)
        self.gridLayout_3.addWidget(self.tableWidget, 4, 0, 1, 4)
        self.pushButton_10 = QtWidgets.QPushButton(self.tab)
        self.pushButton_10.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_3.addWidget(self.pushButton_10, 5, 0, 1, 1)
        self.nextButton = QtWidgets.QPushButton(self.tab)
        self.nextButton.setObjectName("nextButton")
        self.gridLayout_3.addWidget(self.nextButton, 5, 3, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 7, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setMouseTracking(False)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 2, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 1, 1, 2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 7, 8, 1, 8)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 5, 5, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 15, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 2, 8, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 2, 5, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 5, 6, 1, 9)
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 5, 3, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 3, 1, 1)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setAutoFillBackground(False)
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setAlternatingRowColors(False)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 1, item)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget_2.horizontalHeader().setHighlightSections(False)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(125)
        self.tableWidget_2.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(28)
        self.tableWidget_2.verticalHeader().setMinimumSectionSize(28)
        self.tableWidget_2.verticalHeader().setSortIndicatorShown(False)
        self.gridLayout.addWidget(self.tableWidget_2, 1, 0, 1, 3)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 7, 16, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setMouseTracking(False)
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 3, 3, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 7, 17, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setMouseTracking(False)
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 3, 1, 1)
        self.listWidget_3 = QtWidgets.QListWidget(self.tab_2)
        self.listWidget_3.setObjectName("listWidget_3")
        self.gridLayout.addWidget(self.listWidget_3, 4, 0, 1, 3)
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_4.setAutoFillBackground(False)
        self.tableWidget_4.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_4.setAlternatingRowColors(False)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(5)
        self.tableWidget_4.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_4.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidget_4.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(0, 1, item)
        self.tableWidget_4.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_4.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget_4.horizontalHeader().setHighlightSections(False)
        self.tableWidget_4.horizontalHeader().setMinimumSectionSize(125)
        self.tableWidget_4.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_4.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_4.verticalHeader().setVisible(False)
        self.tableWidget_4.verticalHeader().setDefaultSectionSize(28)
        self.tableWidget_4.verticalHeader().setMinimumSectionSize(28)
        self.gridLayout.addWidget(self.tableWidget_4, 4, 3, 1, 13)
        self.treeWidget = QtWidgets.QTreeWidget(self.tab_2)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.header().setDefaultSectionSize(140)
        self.gridLayout.addWidget(self.treeWidget, 1, 3, 1, 15)
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setMouseTracking(False)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setMouseTracking(False)
        self.label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 16, 1, 1)
        self.pushButton_26 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_26.setObjectName("pushButton_26")
        self.gridLayout.addWidget(self.pushButton_26, 2, 9, 1, 1)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout.addWidget(self.textBrowser_2, 4, 16, 1, 2)
        self.pushButton_27 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_27.setObjectName("pushButton_27")
        self.gridLayout.addWidget(self.pushButton_27, 2, 10, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 5, 4, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 6, 8, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 6, 9, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 6, 10, 1, 8)
        self.label_7.raise_()
        self.label_6.raise_()
        self.tableWidget_2.raise_()
        self.treeWidget.raise_()
        self.tableWidget_4.raise_()
        self.textBrowser_2.raise_()
        self.label_9.raise_()
        self.listWidget_3.raise_()
        self.label_11.raise_()
        self.label_8.raise_()
        self.pushButton_3.raise_()
        self.pushButton_7.raise_()
        self.pushButton_9.raise_()
        self.pushButton_8.raise_()
        self.lineEdit_2.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_26.raise_()
        self.lineEdit_5.raise_()
        self.pushButton_27.raise_()
        self.pushButton_4.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.graphWidget = PlotWidget(self.tab_3)
        self.graphWidget.setGeometry(QtCore.QRect(10, 50, 1451, 691))
        self.graphWidget.setObjectName("graphWidget")
        self.stopButton = QtWidgets.QPushButton(self.tab_3)
        self.stopButton.setGeometry(QtCore.QRect(1490, 130, 111, 31))
        self.stopButton.setObjectName("stopButton")
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_12.setGeometry(QtCore.QRect(1490, 230, 111, 31))
        self.pushButton_12.setCheckable(False)
        self.pushButton_12.setChecked(False)
        self.pushButton_12.setAutoDefault(False)
        self.pushButton_12.setDefault(False)
        self.pushButton_12.setFlat(False)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_13.setGeometry(QtCore.QRect(1490, 270, 111, 31))
        self.pushButton_13.setCheckable(True)
        self.pushButton_13.setObjectName("pushButton_13")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_3.setGeometry(QtCore.QRect(90, 10, 760, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_3.sizePolicy().hasHeightForWidth())
        self.textBrowser_3.setSizePolicy(sizePolicy)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 71, 30))
        self.label_10.setMouseTracking(False)
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_5.setGeometry(QtCore.QRect(10, 760, 1451, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_5.sizePolicy().hasHeightForWidth())
        self.tableWidget_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tableWidget_5.setFont(font)
        self.tableWidget_5.setAutoFillBackground(False)
        self.tableWidget_5.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_5.setAlternatingRowColors(False)
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(2)
        self.tableWidget_5.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_5.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_5.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_5.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        self.tableWidget_5.horizontalHeader().setVisible(False)
        self.tableWidget_5.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_5.horizontalHeader().setDefaultSectionSize(127)
        self.tableWidget_5.horizontalHeader().setHighlightSections(False)
        self.tableWidget_5.horizontalHeader().setMinimumSectionSize(125)
        self.tableWidget_5.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_5.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_5.verticalHeader().setVisible(False)
        self.tableWidget_5.verticalHeader().setDefaultSectionSize(28)
        self.tableWidget_5.verticalHeader().setMinimumSectionSize(28)
        self.sweepButton = QtWidgets.QPushButton(self.tab_3)
        self.sweepButton.setGeometry(QtCore.QRect(1490, 670, 111, 31))
        self.sweepButton.setCheckable(True)
        self.sweepButton.setObjectName("sweepButton")
        self.pauseButton = QtWidgets.QPushButton(self.tab_3)
        self.pauseButton.setGeometry(QtCore.QRect(1490, 90, 111, 31))
        self.pauseButton.setCheckable(True)
        self.pauseButton.setChecked(False)
        self.pauseButton.setObjectName("pauseButton")
        self.pushButton_16 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_16.setGeometry(QtCore.QRect(1490, 310, 111, 31))
        self.pushButton_16.setCheckable(False)
        self.pushButton_16.setObjectName("pushButton_16")
        self.progressBar = QtWidgets.QProgressBar(self.tab_3)
        self.progressBar.setGeometry(QtCore.QRect(870, 10, 241, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.loopButton = QtWidgets.QPushButton(self.tab_3)
        self.loopButton.setGeometry(QtCore.QRect(1490, 710, 111, 31))
        self.loopButton.setCheckable(True)
        self.loopButton.setObjectName("loopButton")
        self.line = QtWidgets.QFrame(self.tab_3)
        self.line.setGeometry(QtCore.QRect(1480, 650, 131, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(1507, 630, 71, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.line_2 = QtWidgets.QFrame(self.tab_3)
        self.line_2.setGeometry(QtCore.QRect(1483, 210, 131, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(1510, 190, 71, 20))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(1507, 50, 71, 20))
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.line_3 = QtWidgets.QFrame(self.tab_3)
        self.line_3.setGeometry(QtCore.QRect(1480, 70, 131, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.spinBox = QtWidgets.QSpinBox(self.tab_3)
        self.spinBox.setGeometry(QtCore.QRect(1570, 360, 42, 22))
        self.spinBox.setMinimum(1)
        self.spinBox.setObjectName("spinBox")
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setGeometry(QtCore.QRect(1480, 360, 71, 20))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        self.label_15.setGeometry(QtCore.QRect(1480, 400, 71, 20))
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.spinBox_2 = QtWidgets.QSpinBox(self.tab_3)
        self.spinBox_2.setGeometry(QtCore.QRect(1570, 400, 42, 22))
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_16 = QtWidgets.QLabel(self.tab_3)
        self.label_16.setGeometry(QtCore.QRect(1480, 440, 71, 20))
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.spinBox_3 = QtWidgets.QSpinBox(self.tab_3)
        self.spinBox_3.setGeometry(QtCore.QRect(1570, 440, 42, 22))
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setObjectName("spinBox_3")
        self.label_coordinate_y = QtWidgets.QLabel(self.tab_3)
        self.label_coordinate_y.setGeometry(QtCore.QRect(1360, 20, 100, 21))
        self.label_coordinate_y.setText("")
        self.label_coordinate_y.setObjectName("label_coordinate_y")
        self.label_coordinate_x = QtWidgets.QLabel(self.tab_3)
        self.label_coordinate_x.setGeometry(QtCore.QRect(1250, 20, 100, 21))
        self.label_coordinate_x.setText("")
        self.label_coordinate_x.setObjectName("label_coordinate_x")
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1656, 21))
        self.menubar.setObjectName("menubar")
        self.menuQuit = QtWidgets.QMenu(self.menubar)
        self.menuQuit.setObjectName("menuQuit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionRecent = QtWidgets.QAction(MainWindow)
        self.actionRecent.setObjectName("actionRecent")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menuQuit.addAction(self.actionRecent)
        self.menuQuit.addAction(self.actionOpen)
        self.menuQuit.addSeparator()
        self.menuQuit.addAction(self.actionQuit)
        self.menubar.addAction(self.menuQuit.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QMeas"))
        self.label_4.setText(_translate("MainWindow", "Information"))
        self.label.setText(_translate("MainWindow", "Available VISA Address"))
        self.label_2.setText(_translate("MainWindow", "Define the intrument type"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'PMingLiU\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Please choose a VISA address and the corresponding Intrument.</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Refresh"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Instrument name"))
        self.pushButton_2.setText(_translate("MainWindow", "Connect"))
        self.label_3.setText(_translate("MainWindow", "Connected  Instrument"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Type"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "VISA Address"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_10.setText(_translate("MainWindow", "Delete"))
        self.nextButton.setText(_translate("MainWindow", "Next"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Connection"))
        self.label_7.setText(_translate("MainWindow", "Methods"))
        self.pushButton_9.setText(_translate("MainWindow", "Delete"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", " Please type the name file here."))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Time (s)"))
        self.pushButton_7.setText(_translate("MainWindow", "Read"))
        self.pushButton_3.setText(_translate("MainWindow", "Conrtol"))
        self.tableWidget_2.setSortingEnabled(False)
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Type"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        self.pushButton_5.setText(_translate("MainWindow", "RUN"))
        self.label_11.setText(_translate("MainWindow", "Read"))
        self.pushButton_6.setText(_translate("MainWindow", "STOP"))
        self.label_8.setText(_translate("MainWindow", "Control"))
        self.tableWidget_4.setSortingEnabled(False)
        item = self.tableWidget_4.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Type"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Read property"))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Magnification"))
        item = self.tableWidget_4.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Unit"))
        __sortingEnabled = self.tableWidget_4.isSortingEnabled()
        self.tableWidget_4.setSortingEnabled(False)
        self.tableWidget_4.setSortingEnabled(__sortingEnabled)
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Level"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Name"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Type"))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "Property"))
        self.treeWidget.headerItem().setText(4, _translate("MainWindow", "Target value"))
        self.treeWidget.headerItem().setText(5, _translate("MainWindow", "Speed"))
        self.treeWidget.headerItem().setText(6, _translate("MainWindow", "Increment"))
        self.treeWidget.headerItem().setText(7, _translate("MainWindow", "Ins_Label (test)"))
        self.label_6.setText(_translate("MainWindow", "Connected  Instrument"))
        self.label_9.setText(_translate("MainWindow", "Information"))
        self.pushButton_26.setText(_translate("MainWindow", "Time Add level"))
        self.pushButton_27.setText(_translate("MainWindow", "Time Add Child"))
        self.pushButton_8.setText(_translate("MainWindow", "Delete"))
        self.pushButton_4.setText(_translate("MainWindow", "Select the folder"))
        self.label_17.setText(_translate("MainWindow", "Current folder:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Measurement"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.pushButton_12.setText(_translate("MainWindow", "Auto range"))
        self.pushButton_13.setText(_translate("MainWindow", "Cursor Position"))
        self.label_10.setText(_translate("MainWindow", "Information"))
        self.tableWidget_5.setSortingEnabled(False)
        item = self.tableWidget_5.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_5.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Read property"))
        item = self.tableWidget_5.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Value"))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_5.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        self.sweepButton.setText(_translate("MainWindow", "Quit sweep"))
        self.pauseButton.setText(_translate("MainWindow", "Pause"))
        self.pushButton_16.setText(_translate("MainWindow", "Save figure"))
        self.loopButton.setText(_translate("MainWindow", "Quit loop"))
        self.label_5.setText(_translate("MainWindow", "Command"))
        self.label_12.setText(_translate("MainWindow", "Figure"))
        self.label_13.setText(_translate("MainWindow", "Control"))
        self.label_14.setText(_translate("MainWindow", "First sweep"))
        self.label_15.setText(_translate("MainWindow", "# sweeps/0"))
        self.label_16.setText(_translate("MainWindow", "Sweep inc"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Graph"))
        self.menuQuit.setTitle(_translate("MainWindow", "Options"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionRecent.setText(_translate("MainWindow", "Recent"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
