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
        login_Form.resize(1108, 782)
        login_Form.setStyleSheet("background-color: rgb(239, 243, 252);\n"
"color: rgb(18, 32, 62);\n"
"font-family:Ubuntu;\n"
"font-size: 20px;")
        self.gridLayout_2 = QtWidgets.QGridLayout(login_Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(login_Form)
        self.groupBox_2.setMinimumSize(QtCore.QSize(615, 692))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_2.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(3, 67, 165, 255), stop:1 rgba(12, 148, 207, 255));")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/ICONS/icons/LOGO.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(login_Form)
        self.groupBox.setMaximumSize(QtCore.QSize(720, 16777215))
        self.groupBox.setStyleSheet("")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 6, 1, 1, 1)
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
        self.gridLayout_3.addWidget(self.login_btn, 5, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(191, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 5, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem2, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setMaximumSize(QtCore.QSize(135, 16777215))
        font = QtGui.QFont()
        font.setFamily("arow")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(239, 243, 252,0);\n"
"font-family:arow;\n"
"font-size:30px;\n"
"color:rgb(18,32,62,255);\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem3, 4, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 130, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_3.addItem(spacerItem4, 2, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(190, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 5, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.email = QtWidgets.QVBoxLayout()
        self.email.setObjectName("email")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(-1)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(171, 175, 183);\n"
"background-color: rgb(246, 211, 45,0);")
        self.label_2.setObjectName("label_2")
        self.email.addWidget(self.label_2)
        self.username_lin = QtWidgets.QLineEdit(self.groupBox)
        self.username_lin.setMinimumSize(QtCore.QSize(350, 40))
        self.username_lin.setStyleSheet("border-radius: 10% 10%;\n"
"padding-left:5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(18, 32, 62);")
        self.username_lin.setPlaceholderText("")
        self.username_lin.setClearButtonEnabled(True)
        self.username_lin.setObjectName("username_lin")
        self.email.addWidget(self.username_lin)
        self.verticalLayout.addLayout(self.email)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem6)
        self.password = QtWidgets.QVBoxLayout()
        self.password.setObjectName("password")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(-1)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(171, 175, 183);\n"
"background-color: rgb(246, 211, 45,0);")
        self.label_3.setObjectName("label_3")
        self.password.addWidget(self.label_3)
        self.password_lin = QtWidgets.QLineEdit(self.groupBox)
        self.password_lin.setMinimumSize(QtCore.QSize(350, 40))
        self.password_lin.setSizeIncrement(QtCore.QSize(5, 0))
        self.password_lin.setStyleSheet("border-radius: 10% 10%;\n"
"padding-left:5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(18, 32, 62);")
        self.password_lin.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lin.setObjectName("password_lin")
        self.password.addWidget(self.password_lin)
        self.verticalLayout.addLayout(self.password)
        self.signup = QtWidgets.QGridLayout()
        self.signup.setObjectName("signup")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(-1)
        font.setUnderline(False)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font-size:15px;\n"
"color:rgb(18,32,62,255);")
        self.label_5.setObjectName("label_5")
        self.signup.addWidget(self.label_5, 0, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.signup.addItem(spacerItem7, 0, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.signup.addItem(spacerItem8, 0, 3, 1, 1)
        self.signup_btn = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.signup_btn.setFont(font)
        self.signup_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signup_btn.setStyleSheet("border-color: rgb(255, 255, 255,0);\n"
"background-color: rgb(255, 255, 255,0);\n"
"border-radius:30px;\n"
"font-size:16px;\n"
"")
        self.signup_btn.setObjectName("signup_btn")
        self.signup.addWidget(self.signup_btn, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.signup)
        self.gridLayout_3.addLayout(self.verticalLayout, 3, 0, 1, 3)
        self.gridLayout_2.addWidget(self.groupBox, 0, 1, 1, 1)

        self.retranslateUi(login_Form)
        QtCore.QMetaObject.connectSlotsByName(login_Form)

    def retranslateUi(self, login_Form):
        _translate = QtCore.QCoreApplication.translate
        login_Form.setWindowTitle(_translate("login_Form", "Form"))
        self.login_btn.setText(_translate("login_Form", " LOGIN"))
        self.label_4.setText(_translate("login_Form", "Login"))
        self.label_2.setText(_translate("login_Form", "Email"))
        self.label_3.setText(_translate("login_Form", "Password"))
        self.label_5.setText(_translate("login_Form", "you don\'t have ac account ? "))
        self.signup_btn.setText(_translate("login_Form", "SIGNUP"))
import app_resources_rc
