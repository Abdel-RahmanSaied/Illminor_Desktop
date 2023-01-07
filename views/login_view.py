# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/login_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login_Form(object):
    def setupUi(self, login_Form):
        login_Form.setObjectName("login_Form")
        login_Form.resize(1164, 710)
        login_Form.setStyleSheet("background-color: rgb(239, 243, 252);\n"
"color: rgb(18, 32, 62);")
        self.gridLayout_2 = QtWidgets.QGridLayout(login_Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(login_Form)
        self.groupBox_2.setMinimumSize(QtCore.QSize(615, 692))
        self.groupBox_2.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(3, 67, 165, 255), stop:1 rgba(12, 148, 207, 255));")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(login_Form)
        self.groupBox.setMaximumSize(QtCore.QSize(526, 16777215))
        self.groupBox.setStyleSheet("")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(130, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 7, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 8, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem2, 4, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(119, 118, 123);\n"
"background-color: rgb(246, 211, 45,0);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.password_lin = QtWidgets.QLineEdit(self.groupBox)
        self.password_lin.setMinimumSize(QtCore.QSize(441, 41))
        self.password_lin.setSizeIncrement(QtCore.QSize(5, 0))
        self.password_lin.setStyleSheet("border-radius: 10% 10%;\n"
"padding-left:5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(18, 32, 62);")
        self.password_lin.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lin.setObjectName("password_lin")
        self.verticalLayout_2.addWidget(self.password_lin)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 5, 0, 1, 3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(119, 118, 123);\n"
"background-color: rgb(246, 211, 45,0);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.username_lin = QtWidgets.QLineEdit(self.groupBox)
        self.username_lin.setMinimumSize(QtCore.QSize(441, 41))
        self.username_lin.setStyleSheet("border-radius: 10% 10%;\n"
"padding-left:5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(18, 32, 62);")
        self.username_lin.setPlaceholderText("")
        self.username_lin.setClearButtonEnabled(True)
        self.username_lin.setObjectName("username_lin")
        self.verticalLayout.addWidget(self.username_lin)
        self.gridLayout_3.addLayout(self.verticalLayout, 3, 0, 1, 3)
        self.login_btn = QtWidgets.QPushButton(self.groupBox)
        self.login_btn.setMinimumSize(QtCore.QSize(221, 51))
        self.login_btn.setMaximumSize(QtCore.QSize(221, 51))
        self.login_btn.setStyleSheet("QPushButton {\n"
"    background-color:rgba(6,103,184,255);\n"
"    color: #FFFFFF;\n"
"    padding: 2px;\n"
"    font: bold 15px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #2752B8;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #827397;\n"
"}")
        self.login_btn.setObjectName("login_btn")
        self.gridLayout_3.addWidget(self.login_btn, 7, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(132, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 7, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem4, 6, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 90, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_3.addItem(spacerItem5, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_3.addItem(spacerItem6, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 1, 1, 1)

        self.retranslateUi(login_Form)
        QtCore.QMetaObject.connectSlotsByName(login_Form)

    def retranslateUi(self, login_Form):
        _translate = QtCore.QCoreApplication.translate
        login_Form.setWindowTitle(_translate("login_Form", "Form"))
        self.label_3.setText(_translate("login_Form", "Password"))
        self.label_2.setText(_translate("login_Form", "Email"))
        self.login_btn.setText(_translate("login_Form", " LOGIN"))
        self.label_4.setText(_translate("login_Form", "Login"))
