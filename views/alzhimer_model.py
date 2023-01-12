# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/alzhimer_model.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(765, 810)
        Form.setStyleSheet("background-color: rgb(239, 243, 252);\n"
"font-family:Ubuntu;\n"
"font-size: 20px;\n"
"    color:black;\n"
"")
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 47, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 3, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(199, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 4, 0, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 98, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 5, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 2, 5, 1, 1)
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setStyleSheet("background-color: rgb(85, 255, 127,0);\n"
"font-size:40px")
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setMinimumSize(QtCore.QSize(300, 450))
        self.groupBox.setMaximumSize(QtCore.QSize(420, 16777215))
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet(" border-color:transparent;\n"
"background-color:transparent;")
        self.groupBox.setTitle("")
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.MDVP_Fo_Hz_SB_5 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.MDVP_Fo_Hz_SB_5.setStyleSheet("  height: 32px;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #959595;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  font-size: 20px;\n"
"  width: 80px;\n"
"  outline: none;\n"
"\n"
"  caret-color: transparent;;\n"
"\n"
"QLineEdit{\n"
"border: 1px solid #ABAFB7;\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #555;\n"
"}\n"
"\n"
"\n"
"QLineEdit{\n"
"border: 1px solid #ABAFB7;\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #555;\n"
"}\n"
"\n"
"")
        self.MDVP_Fo_Hz_SB_5.setObjectName("MDVP_Fo_Hz_SB_5")
        self.horizontalLayout_6.addWidget(self.MDVP_Fo_Hz_SB_5)
        self.gridLayout.addLayout(self.horizontalLayout_6, 5, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.sex_comboBox = QtWidgets.QComboBox(self.groupBox)
        self.sex_comboBox.setMinimumSize(QtCore.QSize(0, 49))
        self.sex_comboBox.setStyleSheet("background:transparent;\n"
"  border-radius: 20px;\n"
"color:#ffffff    ;\n"
" border: 2px solid  #ffffff;\n"
"font-size:20px;\n"
"padding:15px;\n"
"\n"
"")
        self.sex_comboBox.setObjectName("sex_comboBox")
        self.sex_comboBox.addItem("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/male.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sex_comboBox.addItem(icon, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/female.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sex_comboBox.addItem(icon1, "")
        self.horizontalLayout.addWidget(self.sex_comboBox)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.MDVP_Fo_Hz_SB_7 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.MDVP_Fo_Hz_SB_7.setStyleSheet("  height: 32px;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #959595;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  font-size: 20px;\n"
"  width: 80px;\n"
"  outline: none;\n"
"\n"
"  caret-color: transparent;;\n"
"\n"
"QLineEdit{\n"
"border: 1px solid #ABAFB7;\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #555;\n"
"}\n"
"\n"
"\n"
"QLineEdit{\n"
"border: 1px solid #ABAFB7;\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #555;\n"
"}\n"
"\n"
"")
        self.MDVP_Fo_Hz_SB_7.setObjectName("MDVP_Fo_Hz_SB_7")
        self.horizontalLayout_8.addWidget(self.MDVP_Fo_Hz_SB_7)
        self.gridLayout.addLayout(self.horizontalLayout_8, 7, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.MDVP_Fo_Hz_SB_2 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.MDVP_Fo_Hz_SB_2.setStyleSheet("  height: 32px;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #959595;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  font-size: 20px;\n"
"  width: 80px;\n"
"  outline: none;\n"
"\n"
"  caret-color: transparent;;\n"
"\n"
"QLineEdit{\n"
"border: 1px solid #ABAFB7;\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #555;\n"
"}\n"
"\n"
"\n"
"QLineEdit{\n"
"border: 1px solid #ABAFB7;\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #555;\n"
"}\n"
"\n"
"")
        self.MDVP_Fo_Hz_SB_2.setObjectName("MDVP_Fo_Hz_SB_2")
        self.horizontalLayout_3.addWidget(self.MDVP_Fo_Hz_SB_2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.MDVP_Fo_Hz_SB_3 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.MDVP_Fo_Hz_SB_3.setStyleSheet("  height: 32px;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #959595;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  font-size: 20px;\n"
"  width: 80px;\n"
"  outline: none;\n"
"\n"
"  caret-color: transparent;;\n"
"\n"
"QLineEdit{\n"
"border: 1px solid #ABAFB7;\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #555;\n"
"}\n"
"\n"
"\n"
"QLineEdit{\n"
"border: 1px solid #ABAFB7;\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #555;\n"
"}\n"
"\n"
"")
        self.MDVP_Fo_Hz_SB_3.setObjectName("MDVP_Fo_Hz_SB_3")
        self.horizontalLayout_4.addWidget(self.MDVP_Fo_Hz_SB_3)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.MDVP_Fo_Hz_SB_6 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.MDVP_Fo_Hz_SB_6.setStyleSheet("  height: 32px;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #959595;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  font-size: 20px;\n"
"  width: 80px;\n"
"  outline: none;\n"
"\n"
"  caret-color: transparent;;\n"
"\n"
"QLineEdit{\n"
"border: 1px solid #ABAFB7;\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #555;\n"
"}\n"
"\n"
"\n"
"QLineEdit{\n"
"border: 1px solid #ABAFB7;\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #555;\n"
"}\n"
"\n"
"")
        self.MDVP_Fo_Hz_SB_6.setObjectName("MDVP_Fo_Hz_SB_6")
        self.horizontalLayout_7.addWidget(self.MDVP_Fo_Hz_SB_6)
        self.gridLayout.addLayout(self.horizontalLayout_7, 6, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.MDVP_Fo_Hz_SB_4 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.MDVP_Fo_Hz_SB_4.setStyleSheet("  height: 32px;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #959595;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  font-size: 20px;\n"
"  width: 80px;\n"
"  outline: none;\n"
"\n"
"  caret-color: transparent;;\n"
"\n"
"QLineEdit{\n"
"border: 1px solid #ABAFB7;\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #555;\n"
"}\n"
"\n"
"\n"
"QLineEdit{\n"
"border: 1px solid #ABAFB7;\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #555;\n"
"}\n"
"\n"
"")
        self.MDVP_Fo_Hz_SB_4.setObjectName("MDVP_Fo_Hz_SB_4")
        self.horizontalLayout_5.addWidget(self.MDVP_Fo_Hz_SB_4)
        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.MDVP_Fo_Hz_SB = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.MDVP_Fo_Hz_SB.setStyleSheet("  height: 32px;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #959595;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  font-size: 20px;\n"
"  width: 80px;\n"
"  outline: none;\n"
"\n"
"  caret-color: transparent;;\n"
"\n"
"QLineEdit{\n"
"border: 1px solid #ABAFB7;\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #555;\n"
"}\n"
"\n"
"\n"
"QLineEdit{\n"
"border: 1px solid #ABAFB7;\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #555;\n"
"}\n"
"\n"
"")
        self.MDVP_Fo_Hz_SB.setObjectName("MDVP_Fo_Hz_SB")
        self.horizontalLayout_2.addWidget(self.MDVP_Fo_Hz_SB)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 2, 1, 1, 4)
        spacerItem5 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 4, 4, 1, 2)
        self.back_btn = QtWidgets.QPushButton(Form)
        self.back_btn.setMinimumSize(QtCore.QSize(60, 60))
        self.back_btn.setMaximumSize(QtCore.QSize(60, 60))
        self.back_btn.setStyleSheet("QPushButton {\n"
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
"}\n"
"QPushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-postion:calc(100% - 10px) center;}\n"
"")
        self.back_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ICONS/icons/back-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_btn.setIcon(icon2)
        self.back_btn.setIconSize(QtCore.QSize(30, 30))
        self.back_btn.setFlat(True)
        self.back_btn.setObjectName("back_btn")
        self.gridLayout_2.addWidget(self.back_btn, 0, 0, 1, 1)
        self.show_result_btn = QtWidgets.QPushButton(Form)
        self.show_result_btn.setMinimumSize(QtCore.QSize(250, 50))
        self.show_result_btn.setMaximumSize(QtCore.QSize(330, 50))
        self.show_result_btn.setStyleSheet("QPushButton {\n"
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
"}\n"
"QPushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-postion:calc(100% - 10px) center;}\n"
"")
        self.show_result_btn.setObjectName("show_result_btn")
        self.gridLayout_2.addWidget(self.show_result_btn, 4, 2, 1, 2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem6, 1, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_9.setText(_translate("Form", "Check Alzahimer"))
        self.label_6.setText(_translate("Form", "eTIV"))
        self.label_2.setText(_translate("Form", "Sex"))
        self.sex_comboBox.setItemText(0, _translate("Form", "Select"))
        self.sex_comboBox.setItemText(1, _translate("Form", "Male"))
        self.sex_comboBox.setItemText(2, _translate("Form", "Female"))
        self.label_8.setText(_translate("Form", "ASF"))
        self.label_3.setText(_translate("Form", "EDUC"))
        self.label_4.setText(_translate("Form", "SES"))
        self.label_7.setText(_translate("Form", "nWBV"))
        self.label_5.setText(_translate("Form", "MMSE"))
        self.label.setText(_translate("Form", "Age"))
        self.show_result_btn.setText(_translate("Form", "Show result"))
import app_resources_rc
