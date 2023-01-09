# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/parkinson_molde.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1220, 945)
        Form.setStyleSheet("\n"
"font-family:Ubuntu;\n"
"font-size: 20px;\n"
"    color:black;\n"
"")
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ICONS/icons/back-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_btn.setIcon(icon)
        self.back_btn.setIconSize(QtCore.QSize(30, 30))
        self.back_btn.setFlat(True)
        self.back_btn.setObjectName("back_btn")
        self.gridLayout_2.addWidget(self.back_btn, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(467, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 4, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem1, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(467, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 4, 4, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(415, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 5, 1, 1)
        self.label_25 = QtWidgets.QLabel(Form)
        self.label_25.setStyleSheet("background-color: rgb(85, 255, 127,0);\n"
"font-size:40px")
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout_2.addWidget(self.label_25, 0, 2, 1, 3)
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
        self.gridLayout_2.addWidget(self.show_result_btn, 4, 3, 1, 1)
        self.elements = QtWidgets.QGroupBox(Form)
        self.elements.setMinimumSize(QtCore.QSize(330, 450))
        self.elements.setAutoFillBackground(False)
        self.elements.setStyleSheet("")
        self.elements.setTitle("")
        self.elements.setFlat(True)
        self.elements.setCheckable(False)
        self.elements.setObjectName("elements")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.elements)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 0, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem5, 0, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem6, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_15 = QtWidgets.QLabel(self.elements)
        self.label_15.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 8, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem7, 5, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.elements)
        self.label_17.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 12, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem8, 1, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem9, 9, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem10, 7, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.elements)
        self.label_16.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 10, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.elements)
        self.label_14.setMinimumSize(QtCore.QSize(171, 0))
        self.label_14.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 6, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.elements)
        self.label_12.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 2, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem11, 11, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem12, 3, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.elements)
        self.label_13.setMinimumSize(QtCore.QSize(171, 0))
        self.label_13.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 4, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem13, 17, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.elements)
        self.label_22.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_22.setObjectName("label_22")
        self.gridLayout_3.addWidget(self.label_22, 20, 0, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem14, 15, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.elements)
        self.label_18.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 14, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.elements)
        self.label_20.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 18, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.elements)
        self.label_11.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 0, 0, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem15, 13, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.elements)
        self.label_19.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 16, 0, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem16, 19, 1, 1, 1)
        self.doubleSpinBox_11 = QtWidgets.QDoubleSpinBox(self.elements)
        self.doubleSpinBox_11.setStyleSheet("background-color: rgb(119, 118, 123,0);\n"
"  cursor: pointer;\n"
"  float: right;\n"
"  padding: 5px 20px;\n"
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
        self.doubleSpinBox_11.setObjectName("doubleSpinBox_11")
        self.gridLayout_3.addWidget(self.doubleSpinBox_11, 0, 1, 1, 1)
        self.doubleSpinBox_12 = QtWidgets.QDoubleSpinBox(self.elements)
        self.doubleSpinBox_12.setStyleSheet("background-color: rgb(119, 118, 123,0);\n"
"  cursor: pointer;\n"
"  float: right;\n"
"  padding: 5px 20px;\n"
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
        self.doubleSpinBox_12.setObjectName("doubleSpinBox_12")
        self.gridLayout_3.addWidget(self.doubleSpinBox_12, 2, 1, 1, 1)
        self.doubleSpinBox_13 = QtWidgets.QDoubleSpinBox(self.elements)
        self.doubleSpinBox_13.setStyleSheet("background-color: rgb(119, 118, 123,0);\n"
"  cursor: pointer;\n"
"  float: right;\n"
"  padding: 5px 20px;\n"
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
        self.doubleSpinBox_13.setObjectName("doubleSpinBox_13")
        self.gridLayout_3.addWidget(self.doubleSpinBox_13, 4, 1, 1, 1)
        self.doubleSpinBox_14 = QtWidgets.QDoubleSpinBox(self.elements)
        self.doubleSpinBox_14.setStyleSheet("background-color: rgb(119, 118, 123,0);\n"
"  cursor: pointer;\n"
"  float: right;\n"
"  padding: 5px 20px;\n"
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
        self.doubleSpinBox_14.setObjectName("doubleSpinBox_14")
        self.gridLayout_3.addWidget(self.doubleSpinBox_14, 6, 1, 1, 1)
        self.doubleSpinBox_15 = QtWidgets.QDoubleSpinBox(self.elements)
        self.doubleSpinBox_15.setStyleSheet("background-color: rgb(119, 118, 123,0);\n"
"  cursor: pointer;\n"
"  float: right;\n"
"  padding: 5px 20px;\n"
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
        self.doubleSpinBox_15.setObjectName("doubleSpinBox_15")
        self.gridLayout_3.addWidget(self.doubleSpinBox_15, 8, 1, 1, 1)
        self.doubleSpinBox_16 = QtWidgets.QDoubleSpinBox(self.elements)
        self.doubleSpinBox_16.setStyleSheet("background-color: rgb(119, 118, 123,0);\n"
"  cursor: pointer;\n"
"  float: right;\n"
"  padding: 5px 20px;\n"
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
        self.doubleSpinBox_16.setObjectName("doubleSpinBox_16")
        self.gridLayout_3.addWidget(self.doubleSpinBox_16, 10, 1, 1, 1)
        self.doubleSpinBox_17 = QtWidgets.QDoubleSpinBox(self.elements)
        self.doubleSpinBox_17.setStyleSheet("background-color: rgb(119, 118, 123,0);\n"
"  cursor: pointer;\n"
"  float: right;\n"
"  padding: 5px 20px;\n"
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
        self.doubleSpinBox_17.setObjectName("doubleSpinBox_17")
        self.gridLayout_3.addWidget(self.doubleSpinBox_17, 12, 1, 1, 1)
        self.doubleSpinBox_18 = QtWidgets.QDoubleSpinBox(self.elements)
        self.doubleSpinBox_18.setStyleSheet("background-color: rgb(119, 118, 123,0);\n"
"  cursor: pointer;\n"
"  float: right;\n"
"  padding: 5px 20px;\n"
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
        self.doubleSpinBox_18.setObjectName("doubleSpinBox_18")
        self.gridLayout_3.addWidget(self.doubleSpinBox_18, 14, 1, 1, 1)
        self.doubleSpinBox_19 = QtWidgets.QDoubleSpinBox(self.elements)
        self.doubleSpinBox_19.setStyleSheet("background-color: rgb(119, 118, 123,0);\n"
"  cursor: pointer;\n"
"  float: right;\n"
"  padding: 5px 20px;\n"
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
        self.doubleSpinBox_19.setObjectName("doubleSpinBox_19")
        self.gridLayout_3.addWidget(self.doubleSpinBox_19, 16, 1, 1, 1)
        self.doubleSpinBox_20 = QtWidgets.QDoubleSpinBox(self.elements)
        self.doubleSpinBox_20.setStyleSheet("background-color: rgb(119, 118, 123,0);\n"
"  cursor: pointer;\n"
"  float: right;\n"
"  padding: 5px 20px;\n"
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
        self.doubleSpinBox_20.setObjectName("doubleSpinBox_20")
        self.gridLayout_3.addWidget(self.doubleSpinBox_20, 18, 1, 1, 1)
        self.doubleSpinBox_21 = QtWidgets.QDoubleSpinBox(self.elements)
        self.doubleSpinBox_21.setStyleSheet("background-color: rgb(119, 118, 123,0);\n"
"  cursor: pointer;\n"
"  float: right;\n"
"  padding: 5px 20px;\n"
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
        self.doubleSpinBox_21.setObjectName("doubleSpinBox_21")
        self.gridLayout_3.addWidget(self.doubleSpinBox_21, 20, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 3, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.elements)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.elements)
        self.label_21.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 16, 0, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem17, 9, 1, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem18, 11, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.elements)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem19, 7, 1, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem20, 5, 1, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem21, 15, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.elements)
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.elements)
        self.label_10.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 12, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.elements)
        self.label_9.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 14, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.elements)
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem22, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.elements)
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 8, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.elements)
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 10, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.elements)
        self.label_23.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 18, 0, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem23, 3, 1, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem24, 13, 1, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem25, 17, 1, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.elements)
        self.doubleSpinBox.setStyleSheet("background-color: rgb(119, 118, 123,0);\n"
"  cursor: pointer;\n"
"  float: right;\n"
"  padding: 5px 20px;\n"
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
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout.addWidget(self.doubleSpinBox, 0, 1, 1, 1)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.elements)
        self.doubleSpinBox_2.setStyleSheet("background-color: rgb(119, 118, 123,0);\n"
"  cursor: pointer;\n"
"  float: right;\n"
"  padding: 5px 20px;\n"
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
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.gridLayout.addWidget(self.doubleSpinBox_2, 2, 1, 1, 1)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.elements)
        self.doubleSpinBox_3.setStyleSheet("background-color: rgb(119, 118, 123,0);\n"
"  cursor: pointer;\n"
"  float: right;\n"
"  padding: 5px 20px;\n"
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
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.gridLayout.addWidget(self.doubleSpinBox_3, 4, 1, 1, 1)
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.elements)
        self.doubleSpinBox_4.setStyleSheet("background-color: rgb(119, 118, 123,0);\n"
"  cursor: pointer;\n"
"  float: right;\n"
"  padding: 5px 20px;\n"
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
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.gridLayout.addWidget(self.doubleSpinBox_4, 6, 1, 1, 1)
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.elements)
        self.doubleSpinBox_5.setStyleSheet("background-color: rgb(119, 118, 123,0);\n"
"  cursor: pointer;\n"
"  float: right;\n"
"  padding: 5px 20px;\n"
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
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.gridLayout.addWidget(self.doubleSpinBox_5, 8, 1, 1, 1)
        self.doubleSpinBox_6 = QtWidgets.QDoubleSpinBox(self.elements)
        self.doubleSpinBox_6.setStyleSheet("background-color: rgb(119, 118, 123,0);\n"
"  cursor: pointer;\n"
"  float: right;\n"
"  padding: 5px 20px;\n"
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
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.gridLayout.addWidget(self.doubleSpinBox_6, 10, 1, 1, 1)
        self.doubleSpinBox_7 = QtWidgets.QDoubleSpinBox(self.elements)
        self.doubleSpinBox_7.setStyleSheet("background-color: rgb(119, 118, 123,0);\n"
"  cursor: pointer;\n"
"  float: right;\n"
"  padding: 5px 20px;\n"
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
        self.doubleSpinBox_7.setObjectName("doubleSpinBox_7")
        self.gridLayout.addWidget(self.doubleSpinBox_7, 12, 1, 1, 1)
        self.doubleSpinBox_8 = QtWidgets.QDoubleSpinBox(self.elements)
        self.doubleSpinBox_8.setStyleSheet("background-color: rgb(119, 118, 123,0);\n"
"  cursor: pointer;\n"
"  float: right;\n"
"  padding: 5px 20px;\n"
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
        self.doubleSpinBox_8.setObjectName("doubleSpinBox_8")
        self.gridLayout.addWidget(self.doubleSpinBox_8, 14, 1, 1, 1)
        self.doubleSpinBox_9 = QtWidgets.QDoubleSpinBox(self.elements)
        self.doubleSpinBox_9.setStyleSheet("background-color: rgb(119, 118, 123,0);\n"
"  cursor: pointer;\n"
"  float: right;\n"
"  padding: 5px 20px;\n"
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
        self.doubleSpinBox_9.setObjectName("doubleSpinBox_9")
        self.gridLayout.addWidget(self.doubleSpinBox_9, 16, 1, 1, 1)
        self.doubleSpinBox_10 = QtWidgets.QDoubleSpinBox(self.elements)
        self.doubleSpinBox_10.setStyleSheet("background-color: rgb(119, 118, 123,0);\n"
"  cursor: pointer;\n"
"  float: right;\n"
"  padding: 5px 20px;\n"
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
        self.doubleSpinBox_10.setObjectName("doubleSpinBox_10")
        self.gridLayout.addWidget(self.doubleSpinBox_10, 18, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.elements, 2, 0, 1, 6)
        spacerItem26 = QtWidgets.QSpacerItem(348, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem26, 0, 1, 1, 1)
        spacerItem27 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem27, 3, 3, 1, 1)
        spacerItem28 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem28, 5, 3, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_25.setText(_translate("Form", "CHECK PARKINSON"))
        self.show_result_btn.setText(_translate("Form", "Show result"))
        self.label_15.setText(_translate("Form", "MDVP_APQ"))
        self.label_17.setText(_translate("Form", "DFA"))
        self.label_16.setText(_translate("Form", "HNR"))
        self.label_14.setText(_translate("Form", "Shimmer_APQ5"))
        self.label_12.setText(_translate("Form", "Shimmer_DDA"))
        self.label_13.setText(_translate("Form", "Shimmer_APQ3"))
        self.label_22.setText(_translate("Form", "PPE"))
        self.label_18.setText(_translate("Form", "spread1"))
        self.label_20.setText(_translate("Form", "D2"))
        self.label_11.setText(_translate("Form", "MDVP_Shimmer_dB"))
        self.label_19.setText(_translate("Form", "spread2"))
        self.label_3.setText(_translate("Form", "MDVP_Fo_Hz"))
        self.label_21.setText(_translate("Form", "NHR"))
        self.label_4.setText(_translate("Form", "MDVP_Flo_Hz"))
        self.label_6.setText(_translate("Form", "MDVP_Jitter_Abs"))
        self.label_10.setText(_translate("Form", "Jitter_DDP"))
        self.label_9.setText(_translate("Form", "MDVP_Shimmer"))
        self.label_5.setText(_translate("Form", "MDVP_Jitter"))
        self.label_7.setText(_translate("Form", "MDVP_RAP"))
        self.label_8.setText(_translate("Form", "MDVP_PPQ"))
        self.label_23.setText(_translate("Form", "RPDE"))
import app_resources_rc
