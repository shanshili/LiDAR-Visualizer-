# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serialshow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SerialShow(object):
    def setupUi(self, SerialShow):
        SerialShow.setObjectName("SerialShow")
        SerialShow.resize(840, 664)
        self.WaveformDisplay = QtWidgets.QGroupBox(SerialShow)
        self.WaveformDisplay.setGeometry(QtCore.QRect(10, 10, 821, 371))
        self.WaveformDisplay.setObjectName("WaveformDisplay")
        self.WaveDosplay = QtWidgets.QOpenGLWidget(self.WaveformDisplay)
        self.WaveDosplay.setGeometry(QtCore.QRect(10, 20, 801, 341))
        self.WaveDosplay.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.WaveDosplay.setObjectName("WaveDosplay")
        self.SerialReceive = QtWidgets.QGroupBox(SerialShow)
        self.SerialReceive.setGeometry(QtCore.QRect(260, 390, 561, 261))
        self.SerialReceive.setObjectName("SerialReceive")
        self.ReceiveDisplay = QtWidgets.QListWidget(self.SerialReceive)
        self.ReceiveDisplay.setGeometry(QtCore.QRect(10, 20, 541, 231))
        self.ReceiveDisplay.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.ReceiveDisplay.setObjectName("ReceiveDisplay")
        self.SerialSetting = QtWidgets.QGroupBox(SerialShow)
        self.SerialSetting.setGeometry(QtCore.QRect(10, 390, 241, 261))
        self.SerialSetting.setObjectName("SerialSetting")
        self.ScanPort = QtWidgets.QPushButton(self.SerialSetting)
        self.ScanPort.setGeometry(QtCore.QRect(150, 39, 81, 66))
        self.ScanPort.setObjectName("ScanPort")
        self.Port = QtWidgets.QLabel(self.SerialSetting)
        self.Port.setGeometry(QtCore.QRect(16, 45, 41, 20))
        self.Port.setObjectName("Port")
        self.Baud = QtWidgets.QLabel(self.SerialSetting)
        self.Baud.setGeometry(QtCore.QRect(16, 86, 41, 20))
        self.Baud.setObjectName("Baud")
        self.Open = QtWidgets.QPushButton(self.SerialSetting)
        self.Open.setGeometry(QtCore.QRect(20, 180, 91, 31))
        self.Open.setObjectName("Open")
        self.Close = QtWidgets.QPushButton(self.SerialSetting)
        self.Close.setGeometry(QtCore.QRect(130, 180, 91, 31))
        self.Close.setObjectName("Close")
        self.label = QtWidgets.QLabel(self.SerialSetting)
        self.label.setGeometry(QtCore.QRect(70, 140, 131, 20))
        self.label.setObjectName("label")
        self.comPort = QtWidgets.QComboBox(self.SerialSetting)
        self.comPort.setGeometry(QtCore.QRect(50, 40, 91, 25))
        self.comPort.setObjectName("comPort")
        self.comPort.addItem("")
        self.comPort.addItem("")
        self.comPort.addItem("")
        self.comPort.addItem("")
        self.comPort.addItem("")
        self.comBaud = QtWidgets.QComboBox(self.SerialSetting)
        self.comBaud.setGeometry(QtCore.QRect(50, 80, 91, 25))
        self.comBaud.setObjectName("comBaud")
        self.comBaud.addItem("")
        self.comBaud.addItem("")
        self.comBaud.addItem("")

        self.retranslateUi(SerialShow)
        QtCore.QMetaObject.connectSlotsByName(SerialShow)

    def retranslateUi(self, SerialShow):
        _translate = QtCore.QCoreApplication.translate
        SerialShow.setWindowTitle(_translate("SerialShow", "Form"))
        self.WaveformDisplay.setTitle(_translate("SerialShow", "Waveform Display"))
        self.SerialReceive.setTitle(_translate("SerialShow", "Serial Receive"))
        self.SerialSetting.setTitle(_translate("SerialShow", "Serial Setting"))
        self.ScanPort.setText(_translate("SerialShow", "Scan Port"))
        self.Port.setText(_translate("SerialShow", "Port:"))
        self.Baud.setText(_translate("SerialShow", "Baud:"))
        self.Open.setText(_translate("SerialShow", "Open Port"))
        self.Close.setText(_translate("SerialShow", "Close Port"))
        self.label.setText(_translate("SerialShow", "Connect Sucess !"))
        self.comPort.setItemText(0, _translate("SerialShow", "COM3"))
        self.comPort.setItemText(1, _translate("SerialShow", "COM4"))
        self.comPort.setItemText(2, _translate("SerialShow", "COM5"))
        self.comPort.setItemText(3, _translate("SerialShow", "COM6"))
        self.comPort.setItemText(4, _translate("SerialShow", "COM8"))
        self.comBaud.setItemText(0, _translate("SerialShow", "115200"))
        self.comBaud.setItemText(1, _translate("SerialShow", "128000"))
        self.comBaud.setItemText(2, _translate("SerialShow", "921600"))
