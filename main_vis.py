#!/usr/bin/env python
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QThread, Qt
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QTreeWidgetItem, QTreeWidgetItemIterator, QApplication, QMainWindow, QTableWidgetItem, QDialog, QVBoxLayout
from ui import Vis_Window, Control_Window, Read_Window
from PyQt5 import sip
import pyvisa as visa
import os
from utils import load_drivers, TxtFunction, MeasurementVis
import qdarkstyle
from nidaqmx.system import System
import logging
from vispy import app, scene
import numpy as np
import itertools
from vispy.color import get_colormaps


# logging.basicConfig(format="%(message)s", level=logging.INFO)   # debug mode


class MainWindow(QMainWindow):
    """Main class"""
    # pointer
    name_count = 1
    row_count = 1
    read_row_count = 1
    save_plot_count = 0
    click = 1
    time_unit = 0.1  # 0.1s

    # instruments
    instruments = []
    instruments_read = []
    instruments_magnification = []
    options_control = []
    options_read = []

    # plot space
    data_line = []
    saved_line = []
    lines_data = []

    # color array
    colormaps = itertools.cycle(get_colormaps())
    color_save = []

    # measurement & database module
    measurement = MeasurementProcess([], [], [], [])
    database = TxtFunction()

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # vispy plot widget
        canvas = scene.SceneCanvas(keys='interactive', show=True)
        grid = canvas.central_widget.add_grid(spacing=0)
        self.viewbox = grid.add_view(row=0, col=1, camera='panzoom')
        lay = QVBoxLayout(self.ui.frame)  # create layout
        lay.addWidget(canvas.native)
        # add some axes
        x_axis = scene.AxisWidget(orientation='bottom')
        x_axis.stretch = (1, 0.05)
        grid.add_widget(x_axis, row=1, col=1)
        x_axis.link_view(self.viewbox)
        y_axis = scene.AxisWidget(orientation='left')
        y_axis.stretch = (0.035, 1)
        grid.add_widget(y_axis, row=0, col=0)
        y_axis.link_view(self.viewbox)
        # auto-scale to see the whole line
        self.viewbox.camera.set_range()

        # control panel & read panel
        self.control_panel = ControlPanel()
        self.read_panel = ReadlPanel()

        # Pre-run functions
        try:
            self.visaList()
            self.intrumentList()
        except:
            logging.error('detect available address fail')

        # page 1
        # Buttons
        self.ui.pushButton.clicked.connect(self.visaList)
        self.ui.pushButton_2.clicked.connect(self.connection)
        self.ui.pushButton_10.clicked.connect(self.deleteConnectedInstrument)
        # Tables
        self.ui.tableWidget.setColumnWidth(0, 100)
        self.ui.tableWidget.setColumnWidth(1, 200)

        # page 2
        # Buttons
        self.ui.pushButton_7.clicked.connect(self.readPanelShow)
        self.read_panel.read_ui.pushButton_5.clicked.connect(self.readConfirm)
        self.read_panel.read_ui.pushButton_5.clicked.connect(self.read_panel.close)
        self.read_panel.read_ui.pushButton_6.clicked.connect(self.read_panel.close)

        self.ui.pushButton_3.clicked.connect(self.readPanelShow)
        self.control_panel.ctr_ui.pushButton_9.clicked.connect(self.addLevel)
        self.control_panel.ctr_ui.pushButton_9.clicked.connect(self.control_panel.close)
        self.control_panel.ctr_ui.pushButton_8.clicked.connect(self.chooseAddChild)
        self.control_panel.ctr_ui.pushButton_8.clicked.connect(self.control_panel.close)
        self.control_panel.ctr_ui.pushButton_6.clicked.connect(self.control_panel.close)

        self.ui.pushButton_8.clicked.connect(self.deleteReadRow)
        self.ui.pushButton_9.clicked.connect(self.chooseDelete)
        self.ui.pushButton_5.clicked.connect(self.timeGo)
        self.ui.pushButton_26.clicked.connect(self.timeAddLevel)
        self.ui.pushButton_27.clicked.connect(self.timeAddChild)
        self.ui.pushButton_4.clicked.connect(self.folderMessage)

        # check box
        self.control_panel.ctr_ui.checkBox.stateChanged.connect(self.checkFunctionIncrement)

        # Tables
        self.ui.tableWidget_2.cellClicked.connect(self.showMethod)

        # treeWidget init
        self.tree = self.ui.treeWidget
        self.tree.itemClicked.connect(self.checkState)

        # page 3
        # Buttons
        self.ui.pushButton_13.clicked.connect(self.displayCursorCrossHair)
        self.ui.pushButton_12.clicked.connect(self.autoPlotRange)
        self.ui.pushButton_11.clicked.connect(self.procedureStop)
        self.ui.pushButton_15.clicked.connect(self.measurement.resumePauseMeasure)
        self.ui.pushButton_17.clicked.connect(self.measurement.quitLoopMeasure)
        self.ui.pushButton_14.clicked.connect(self.measurement.quitSweepMeasure)
        self.ui.pushButton_16.clicked.connect(self.plotSave)

        # Tables
        self.ui.tableWidget_5.cellClicked.connect(self.lineDisplaySwitch)

        # Menu
        self.ui.retranslateUi(self)
        self.ui.actionQuit.setShortcut('Ctrl+Q')
        self.ui.actionQuit.triggered.connect(self.timeStop)
        self.ui.actionQuit.triggered.connect(self.shutdownInstruments)
        self.ui.actionQuit.triggered.connect(application.exit)
        self.ui.actionQuit.triggered.connect(self.close)

        # Set Window Icon
        self.setWindowIcon(QIcon('./ui/Qfort.png'))

        # Set Window style
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    # =============================================================================
    # Page 1
    # =============================================================================
    def visaList(self):
        """ detect available address """
        resource_manager = visa.ResourceManager()
        self.pyvisa_list = resource_manager.list_resources()
        self.ui.listWidget.clear()
        self.ui.listWidget.addItems(self.pyvisa_list)

        # DAQ TODO:only one daq is available now 20210916
        system = System.local()
        for i, device in enumerate(system.devices):
            if i > 0:
                self.ui.listWidget.addItem(device.name)
        self.ui.listWidget.addItem("default")

    def intrumentList(self):
        """ detect available drivers """
        self.driver_list = load_drivers()
        self.ui.listWidget_2.clear()
        self.ui.listWidget_2.addItems(self.driver_list.keys())

    def pageOneInformation(self, string):
        """ put some word in the information board """
        self.ui.textBrowser.append(str(string))

    def deleteConnectedInstrument(self):
        """ delete connected instrument from page1 """
        row = self.ui.tableWidget.currentRow()
        self.ui.tableWidget.removeRow(row)
        self.ui.tableWidget_2.removeRow(row)
        self.row_count -= 1
        self.instruments.pop(row)

    def connection(self):
        """ add instruments into table_instrList """
        # Get info from lists and construct new object later
        visa_address = self.ui.listWidget.currentItem().text()
        instrument_type = self.ui.listWidget_2.currentItem().text()
        instrument_personal_name = self.ui.lineEdit.text()

        row_len = self.ui.tableWidget.rowCount()
        # Check existance
        if self.ui.tableWidget.findItems(visa_address, Qt.MatchExactly) != [] or \
                self.ui.tableWidget.findItems(instrument_personal_name, Qt.MatchExactly) != []:
            self.pageOneInformation('This VISA address or name has been used.')
        else:
            if instrument_type in self.driver_list.keys():
                try:
                    instrument_name = f'{instrument_type}_{self.name_count}'
                    self.name_count += 1

                    instrument = self.driver_list[instrument_type](visa_address)
                    instrument.setProperty(visa_address, instrument_name, instrument_type)
                    self.instruments.append(instrument)

                    # TODO: add some condition to check if Connection is successful
                    self.pageOneInformation(f'self.{instrument_name} = {instrument_type}("{visa_address}")')
                    self.pageOneInformation(f'{instrument_type} has been connected successfully.')
                    # TODO: add initialization option on messagebox and show the related info

                    # Add new row if necessary
                    if self.row_count > row_len:
                        self.ui.tableWidget.insertRow(row_len)
                        self.ui.tableWidget_2.insertRow(row_len)

                    # Assign varibales to current var
                    instrument_property = [instrument_personal_name, instrument_type, visa_address]
                    for i, p in enumerate(instrument_property):
                        if p == '':
                            p = instrument_name
                        # Update the info to the table in page 1
                        self.ui.tableWidget.setItem(self.row_count - 1, i, QTableWidgetItem(p))

                    # Update the left top table in page 2
                    if instrument_personal_name == '':
                        instrument_personal_name = instrument_name
                    self.ui.tableWidget_2.setItem(self.row_count - 1, 0, QTableWidgetItem(instrument_personal_name))
                    self.ui.tableWidget_2.setItem(self.row_count - 1, 1, QTableWidgetItem(instrument_type))
                    self.row_count += 1

                except visa.VisaIOError or AttributeError:
                    self.pageOneInformation(f"{instrument_type} connect fail")
        self.ui.lineEdit.clear()

    # =============================================================================
    # Page 2
    # =============================================================================

    def pageTwoInformation(self, string):
        """ information in page2 """
        self.ui.textBrowser_2.append(str(string))

    def readPanelShow(self):
        """ popup panel from read button """
        if self.ui.listWidget_3.currentItem() == None:
            self.pageTwoInformation('Please select a method.')
        else:
            self.read_panel.show()

    def controlPanelShow(self):
        """ popup panel from control button """
        if self.ui.listWidget_3.currentItem() == None:
            self.pageTwoInformation('Please select a method.')
        else:
            self.control_panel.show()

    def deleteReadRow(self):
        """ delete read instruments from page2 """
        row = self.ui.tableWidget_4.currentRow()
        self.ui.tableWidget_4.removeRow(row)
        self.ui.tableWidget_5.removeColumn(row+1)
        self.read_row_count -= 1
        self.instruments_read.pop(row)
        self.options_read.pop(row)

    def showMethod(self):
        """ show instruments method in page2 """
        row = self.ui.tableWidget_2.currentRow()
        instrument = self.instruments[row]
        self.ui.listWidget_3.clear()
        # show the method of the chosen itesm to the list
        self.ui.listWidget_3.addItems(instrument.METHOD)
        # TODO: add the waiting-time measurement to the option

    def readConfirm(self):
        """ confirm button in read panel """
        # Get the necessary info of the chosen item
        row = self.ui.tableWidget_2.currentRow()
        instrument_name = self.ui.tableWidget_2.item(row, 0).text()
        instrument_type = self.ui.tableWidget_2.item(row, 1).text()
        read_method = self.ui.listWidget_3.currentItem().text()
        magnification = self.read_panel.read_ui.lineEdit_2.text()
        Unit = self.read_panel.read_ui.lineEdit_3.text()

        # Add new row if necessary
        row_len = self.ui.tableWidget_4.rowCount()
        if self.read_row_count > row_len:
            self.ui.tableWidget_4.insertRow(row_len)
            self.ui.tableWidget_5.insertColumn(row_len + 1)

        # Assign the variables to the table in page 2
        self.ui.tableWidget_4.setItem(self.read_row_count - 1, 0, QTableWidgetItem(instrument_name))
        self.ui.tableWidget_4.setItem(self.read_row_count - 1, 1, QTableWidgetItem(instrument_type))
        self.ui.tableWidget_4.setItem(self.read_row_count - 1, 2, QTableWidgetItem(read_method))
        self.ui.tableWidget_4.setItem(self.read_row_count - 1, 3, QTableWidgetItem(magnification))
        self.ui.tableWidget_4.setItem(self.read_row_count - 1, 4, QTableWidgetItem(Unit))

        # initialize the blocks in the read option
        self.read_panel.read_ui.lineEdit_2.setText("1")
        self.read_panel.read_ui.lineEdit_3.clear()

        # Assign the variables to the table in page 3
        self.ui.tableWidget_5.setItem(0, self.read_row_count, QTableWidgetItem(instrument_name))
        self.ui.tableWidget_5.setItem(1, self.read_row_count, QTableWidgetItem(read_method))

        method_row_len = self.ui.tableWidget_4.rowCount()
        self.pageTwoInformation(method_row_len)

        self.read_row_count += 1

        self.instruments_read.append(self.instruments[row])
        self.options_read.append(read_method)
        self.instruments_magnification.append(int(magnification))

    def switchToPlotTab(self):
        """ switch to page3 """
        self.ui.tabWidget.setCurrentIndex(2)

    def timeAddLevel(self):
        """ Provide another option to do the time measurement """
        wait_time = self.ui.lineEdit_5.text()

        if wait_time.isnumeric():
            self.root = QTreeWidgetItem(self.tree)
            self.root.setText(0, '0')
            self.root.setFlags(self.root.flags() | Qt.ItemIsUserCheckable)
            self.root.setCheckState(0, Qt.Checked)
            self.root.setExpanded(True)
            self.updateTimeMeasurement(self.root)
            self.checkState()
        else:
            self.pageTwoInformation('Time measurement - Please enter a number.')

        self.ui.lineEdit_5.clear()

    def timeAddChild(self):
        """ Provide another option to do the time measurement """
        wait_time = self.ui.lineEdit_5.text()

        if wait_time.isnumeric():
            item = self.tree.currentItem()
            self.child1 = QTreeWidgetItem(item)
            self.child1.setText(0, '1')
            self.child1.setExpanded(True)
            self.updateTimeMeasurement(self.child1)
            self.child1.setFlags(self.child1.flags() | Qt.ItemIsUserCheckable)
            self.child1.setCheckState(0, Qt.Checked)
            self.control_panel.ctr_ui.checkBox.setChecked(False)
            self.checkState()
        else:
            self.pageTwoInformation('Time measurement - Please enter a number.')

        self.ui.lineEdit_5.clear()

    # treeWidget
    def addLevel(self):
        """ add level button in control panel """
        self.root = QTreeWidgetItem(self.tree)
        self.root.setText(0, '0')
        self.root.setFlags(self.root.flags() | Qt.ItemIsUserCheckable)
        self.root.setCheckState(0, Qt.Checked)
        self.root.setExpanded(True)
        self.updateInfo(self.root)
        self.control_panel.ctr_ui.checkBox.setChecked(False)
        self.control_panel.ctr_ui.lineEdit_5.setText('0')
        self.checkState()

    def chooseAddChild(self):
        """ add child button in control panel """
        # QTreeWidgetItem括號內放的物件是作為基礎(root)，child會往下一層放
        item = self.tree.currentItem()
        if self.tree.indexOfTopLevelItem(item) >= 0:
            target_item = item
        else:
            _, _, child_num, _, _, _ = self.getIndexs(item.parent())
            target_item = item.parent().child(child_num - 1)

        self.child1 = QTreeWidgetItem(target_item)
        self.child1.setText(0, '1')
        self.child1.setExpanded(True)
        self.updateInfo(self.child1)
        self.child1.setFlags(self.child1.flags() | Qt.ItemIsUserCheckable)
        self.child1.setCheckState(0, Qt.Checked)
        self.control_panel.ctr_ui.checkBox.setChecked(False)
        self.control_panel.ctr_ui.lineEdit_5.setText('0')
        self.checkState()

    def checkFunctionIncrement(self):
        if self.control_panel.ctr_ui.checkBox.isChecked():
            self.control_panel.ctr_ui.lineEdit_5.setEnabled(True)
        else:
            self.control_panel.ctr_ui.lineEdit_5.setEnabled(False)

    def updateInfo(self, item):
        row = self.ui.tableWidget_2.currentRow()
        Ins_name = self.ui.tableWidget_2.item(row, 0).text()
        Ins_type = self.ui.tableWidget_2.item(row, 1).text()
        control_method = self.ui.listWidget_3.currentItem().text()

        # TODO: restrict the the value to integer only or something related to the unit
        target = self.control_panel.ctr_ui.lineEdit_2.text()
        speed = self.control_panel.ctr_ui.lineEdit_3.text()

        # check box
        increment = self.control_panel.ctr_ui.lineEdit_5.text()
        control_list = [Ins_name, Ins_type, control_method, target, speed, increment]

        for i, element in enumerate(control_list):
            item.setText((i+1), element)
        item.setText(7, str(row))

    def updateTimeMeasurement(self, item):
        row = str(-1)
        Ins_name = 'Time Meas'
        Ins_type = 'Timer'
        control_method = '-'

        # TODO: restrict the the value to integer only or something related to the unit
        target = self.ui.lineEdit_5.text()
        speed = '-'
        increment = '-'
        control_list = [Ins_name, Ins_type, control_method, target, speed, increment]
        for i, element in enumerate(control_list):
            item.setText((i+1), element)
        item.setText(7, row)

    def checkState(self):
        global checklist
        iterator = QTreeWidgetItemIterator(self.tree)
        checklist = []
        for _ in range(11):
            checklist.append([])

        while iterator.value():
            item = iterator.value()
            treeindex, childindex, child_num, method, ins_label, target, speed, increment = self.getIndexs(item)
            checkstate = item.checkState(0)

            # tree index
            checklist[0].append(treeindex)
            # item's child number
            checklist[1].append(child_num)
            # item index in parents view
            checklist[2].append(childindex)
            # ischild or not, if not, it shows how many child it has; if yes, it shows -1,
            checklist[3].append(child_num)
            # check
            checklist[4].append(checkstate)
            # temp
            checklist[5].append(treeindex)
            # method
            checklist[6].append(method)
            # ins_label
            checklist[7].append(ins_label)
            # target
            checklist[8].append(target)
            # speed
            checklist[9].append(speed)
            # increment
            checklist[10].append(increment)

            iterator += 1

        for i in range(len(checklist[3])):
            if checklist[0][i] == -1:
                checklist[0][i] = checklist[0][i-1]
            else:
                checklist[0][i] = checklist[0][i]

            if checklist[2][i] == -1:
                checklist[2][i] = 0

            if checklist[1][i] == 0 and checklist[5][i] == -1:
                checklist[3][i] = checklist[5][i]
        del(checklist[5])
        del(checklist[1])
        self.tree_num, self.leve_position, self.child_num, self.check, self.method, self.ins_label, self.target, self.speed, self.increment = checklist[
            0], checklist[1], checklist[2], checklist[3], checklist[4], checklist[5], checklist[6], checklist[7], checklist[8]

    def getIndexs(self, item):
        """ Returns Current top level item and child index.
            If no child is selected, returns -1. 
        """
        # Check if top level item is selected or child selected
        if self.tree.indexOfTopLevelItem(item) == -1:
            return self.tree.indexOfTopLevelItem(item), item.parent().indexOfChild(item), item.childCount(), item.text(3), item.text(7), item.text(4), item.text(5), item.text(6)
        else:
            return self.tree.indexOfTopLevelItem(item), -1, item.childCount(), item.text(3), item.text(7), item.text(4), item.text(5), item.text(6)

    def chooseDelete(self):
        item = self.tree.currentItem()
        sip.delete(item)
        self.checkState()

    # =============================================================================
    # Page 3
    # =============================================================================

    def pageThreeInformation(self, string):
        self.ui.textBrowser_3.clear
        self.ui.textBrowser_3.append(str(string))

    def displayCursorCrossHair(self):
        """Add crosshair lines."""
        pass
        # if self.ui.pushButton_13.isChecked():
        #     self.crosshair_v = pg.InfiniteLine(angle=90, movable=False)
        #     self.crosshair_h = pg.InfiniteLine(angle=0, movable=False)
        #     self.ui.graphWidget.addItem(self.crosshair_v, ignoreBounds=True)
        #     self.ui.graphWidget.addItem(self.crosshair_h, ignoreBounds=True)
        #     self.proxy = pg.SignalProxy(self.ui.graphWidget.scene(
        #     ).sigDisplayCursorCoordinate, rateLimit=60, slot=self.displayCursorCoordinate)
        # else:
        #     self.ui.graphWidget.removeItem(self.crosshair_h)
        #     self.ui.graphWidget.removeItem(self.crosshair_v)
        #     self.proxy = []

    def displayCursorCoordinate(self, e):
        pass
        # pos = e[0]
        # if self.ui.graphWidget.sceneBoundingRect().contains(pos):
        #     mousePoint = self.ui.graphWidget.getPlotItem().vb.mapSceneToView(pos)
        #     self.crosshair_v.setPos(mousePoint.x())
        #     self.crosshair_h.setPos(mousePoint.y())

    def setProgressBar(self):
        self.progress += 1
        self.ui.progressBar.setValue(self.progress)

    def clearProgressBar(self, max):
        self.progress = 0
        self.ui.progressBar.setValue(0)
        self.ui.progressBar.setMaximum(max)

    # =============================================================================
    #  Start and stop function
    # =============================================================================
    def folderMessage(self):
        global folder_address
        # folder Path
        cwd = os.getcwd()
        folder_address = QFileDialog.getExistingDirectory(self, "Please define the file name", cwd)

        if folder_address != '':
            self.folder_name = folder_address
            self.ui.label_18.setText(self.folder_name)
            cwd = folder_address

    def timeGo(self):
        """ TimeGo is the first activating function when "run" the project
            At first, the name of the project will be test if it has existed.
            if you ignore the warning and choose overwrite the file, the project
            will start immediately. The txt file as well as the plot items will
            be created.
        """
        if self.ui.label_18.text() == '':
            QMessageBox.information(self, "Wrong!.", "Please select the folder.")
        else:
            self.name = self.ui.lineEdit_2.text()
            if self.name == '':
                QMessageBox.information(self, "Wrong!.", "Please type the file name.")
            else:
                file_name = f'{self.name}.txt'
                List = os.listdir(folder_address)
                if file_name in List:
                    reply = QMessageBox.information(
                        self, "Wrong!.", "The file has existed. Do you want to overwrite it?",
                        QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)
                    if reply == QMessageBox.Close:
                        QMessageBox.information(self, "Wrong!.", "Please adjust the file name.")
                    elif reply == QMessageBox.Ok:
                        self.procedureGo()
                else:
                    self.procedureGo()

    def procedureGo(self):
        """"measure start"""
        # file name
        self.full_address = self.folder_name + '/' + self.name
        # save plot count
        self.save_plot_count = 0
        self.switchToPlotTab()
        # plotlines init
        self.createEmptyLines()
        self.lineDisplaySwitchCreat()
        # Create a QThread object
        self.exp_thread = QThread()
        # Create a worker object
        self.measurement = None
        self.measurement = MeasurementProcess(self.instruments, self.instruments_read, self.options_read, self.instruments_magnification)
        # Move worker to the thread
        self.database.moveToThread(self.exp_thread)
        self.measurement.moveToThread(self.exp_thread)
        # porcedure start
        self.measurement.schedule(self.tree_num, self.child_num, self.leve_position, self.check,
                                  self.method, self.ins_label, self.target, self.speed, self.increment)
        self.exp_thread.started.connect(self.measurement.startMeasure)
        # Connect signals and slots
        self.measurement.finished.connect(self.timeStop)
        self.measurement.signal_txt.connect(self.database.txtUpdate)
        self.measurement.signal_axis.connect(self.axisUpdate)
        self.measurement.signal_plot.connect(self.plotUpdate)
        self.measurement.signal_lines.connect(self.saveLines)
        self.measurement.signal_progress.connect(self.setProgressBar)
        self.measurement.clear_progress.connect(self.clearProgressBar)
        # Start the thread
        self.exp_thread.start()
        # final resets
        self.ui.pushButton_5.setEnabled(False)
        self.exp_thread.finished.connect(
            lambda: self.ui.pushButton_5.setEnabled(True))

    def timeStop(self, file_count):
        """measure stop"""
        # time stop
        logging.info('measure stop')
        try:
            self.procedureStop()
            self.exp_thread.quit()
            self.exp_thread.wait()
            self.shutdownInstruments()
            self.measurement = None
            self.database.txtMerger(self.full_address, file_count, len(self.instruments_read)+1)
            self.database.txtDeleter(file_count)
        except AttributeError:
            pass

    def procedureStop(self):
        self.measurement.stopMeasure()
        self.ui.pushButton_5.setEnabled(True)

    def shutdownInstruments(self):
        for i in self.instruments:
            i.performClose()

    # =============================================================================
    # plot setting
    # =============================================================================

    def plotUpdate(self, n, x_y):
        self.lines_data[n] = np.vstack([self.lines_data[n], np.array(x_y)])
        # setData to the PlotItems
        if self.switch_list[n] == True:
            pos = self.lines_data[n]
            self.data_line[n].set_data(pos)
        else:
            self.data_line[n].set_data(np.array([[np.nan, np.nan]]))

    def saveLines(self, file_count):
        # vertex positions of data to draw
        for i in range(self.read_len):
            color = next(self.colormaps)
            pos = self.lines_data[i]
            self.saved_line.append(scene.Line(parent=self.viewbox.scene))
            self.saved_line[i + self.read_len * (file_count)].set_data(pos, color)
            self.data_line[i].set_data(np.array([[np.nan, np.nan]]))

    def createEmptyLines(self):
        """ creat the plotDataItem as data_line[i] where i = 0, 1, 2... (reference)
            the x y value will be set later within the function plot_update()
        """
        # self.plt.clear()
        self.data_line = []
        self.saved_line = []
        self.read_len = len(self.instruments_read)
        for _ in range(self.read_len):
            self.data_line.append(scene.Line(parent=self.viewbox.scene))
        # save data
        self.lines_data = []
        for _ in range(self.read_len):
            # , dtype=np.float32
            self.lines_data.append(np.array([[np.nan, np.nan]]))

    def autoPlotRange(self):
        """ auto-scale to see the whole line """
        self.viewbox.camera.set_range()

    def plotSave(self):
        pass
        # exporter = pg.exporters.ImageExporter(self.plt.scene())
        # exporter.export(self.full_address + '_%d.png' % self.save_plot_count)
        # QMessageBox.information(
        #     self, "Done.", "The figure No.%d has been saved." % self.save_plot_count)
        # self.save_plot_count += 1

    def lineDisplaySwitchCreat(self):
        self.switch_list = []
        for _ in range(len(self.instruments_read)):
            self.switch_list.append(True)

    def lineDisplaySwitch(self):
        """ this function is connected to tableWidget_5 on page 3
            the function activates whenever the tablewidge_5 is clicked
        """
        col = self.ui.tableWidget_5.currentColumn()-1
        if col != -1:    # ignore x_show column
            if self.switch_list[col]:
                self.switch_list[col] = False
            else:
                self.switch_list[col] = True

    # =============================================================================
    # axis setting
    # =============================================================================

    def axisUpdate(self, x_show, y_show):
        # update x title (instrument name and method)
        # insturement name
        self.ui.tableWidget_5.setItem(0, 0, QTableWidgetItem(f'{x_show[1]}'))
        # method
        self.ui.tableWidget_5.setItem(1, 0, QTableWidgetItem(f'{x_show[2]}'))

        # update x value
        self.ui.tableWidget_5.setItem(2, 0, QTableWidgetItem(f'{x_show[0]:g}'))
        # update y value
        logging.info(f'len:{len(self.instruments_read)}')
        logging.info(f'x:{x_show}')
        logging.info(f'y:{y_show}')
        i = 0
        for i in range(len(self.instruments_read)):
            self.ui.tableWidget_5.setItem(2, (i + 1), QTableWidgetItem(f'{y_show[i]}'))  # :.6g


class ControlPanel(QDialog):
    """Page 2 subwindow Control option panel"""

    def __init__(self):
        super(ControlPanel, self).__init__()
        self.ctr_ui = Control_Window()
        self.ctr_ui.setupUi(self)


class ReadlPanel(QDialog):
    """Page 2 subwindow Read option panel"""

    def __init__(self):
        super(ReadlPanel, self).__init__()
        self.read_ui = Read_Window()
        self.read_ui.setupUi(self)


if __name__ == '__main__':
    application = QApplication([])
    window = MainWindow()
    window.show()
    app.run()