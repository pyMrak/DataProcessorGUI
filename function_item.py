# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'function_item1.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        if not StackedWidget.objectName():
            StackedWidget.setObjectName(u"StackedWidget")
        StackedWidget.resize(747, 230)
        StackedWidget.setMinimumSize(QSize(0, 230))
        StackedWidget.setMaximumSize(QSize(16777215, 230))
        StackedWidget.setStyleSheet(u"QFrame {\n"
"	background:rgb(90,90,90);\n"
"}")
        StackedWidget.setLineWidth(0)
        self.page_add = QWidget()
        self.page_add.setObjectName(u"page_add")
        self.page_add.setMinimumSize(QSize(0, 30))
        self.page_add.setMaximumSize(QSize(16777215, 30))
        self.page_add.setStyleSheet(u"QFrame {\n"
"	background:rgb(90,90,90);\n"
"}")
        self.verticalLayout_page_add = QVBoxLayout(self.page_add)
        self.verticalLayout_page_add.setSpacing(0)
        self.verticalLayout_page_add.setObjectName(u"verticalLayout_page_add")
        self.verticalLayout_page_add.setContentsMargins(0, 0, 0, 0)
        self.frame_add = QFrame(self.page_add)
        self.frame_add.setObjectName(u"frame_add")
        self.frame_add.setMinimumSize(QSize(0, 200))
        self.frame_add.setMaximumSize(QSize(16777215, 200))
        self.frame_add.setFrameShape(QFrame.NoFrame)
        self.frame_add.setFrameShadow(QFrame.Plain)
        self.frame_add.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.frame_add)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.bn_add_function = QPushButton(self.frame_add)
        self.bn_add_function.setObjectName(u"bn_add_function")
        self.bn_add_function.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bn_add_function.sizePolicy().hasHeightForWidth())
        self.bn_add_function.setSizePolicy(sizePolicy)
        self.bn_add_function.setMinimumSize(QSize(120, 30))
        self.bn_add_function.setMaximumSize(QSize(16777215, 30))
        self.bn_add_function.setStyleSheet(u"QPushButton {\n"
"    color: rgba(255,255,255,255);\n"
"    font-weight: 900;\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(55,55,55);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon = QIcon()
        icon.addFile(u"icons/1x/addAsset.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_add_function.setIcon(icon)
        self.bn_add_function.setIconSize(QSize(22, 22))
        self.bn_add_function.setFlat(True)

        self.verticalLayout.addWidget(self.bn_add_function)

        self.frame_blank = QFrame(self.frame_add)
        self.frame_blank.setObjectName(u"frame_blank")
        self.frame_blank.setFrameShape(QFrame.StyledPanel)
        self.frame_blank.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_blank)


        self.verticalLayout_page_add.addWidget(self.frame_add)

        StackedWidget.addWidget(self.page_add)
        self.page_define = QWidget()
        self.page_define.setObjectName(u"page_define")
        self.page_define.setMinimumSize(QSize(0, 230))
        self.page_define.setMaximumSize(QSize(16777215, 230))
        self.page_define.setStyleSheet(u"QWidget{\n"
"	background:rgb(91,90,90);\n"
"}\n"
"")
        self.verticalLayout_page_add1 = QVBoxLayout(self.page_define)
        self.verticalLayout_page_add1.setSpacing(0)
        self.verticalLayout_page_add1.setObjectName(u"verticalLayout_page_add1")
        self.verticalLayout_page_add1.setContentsMargins(2, 2, 2, 2)
        self.groupBox = QGroupBox(self.page_define)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 200))
        self.groupBox.setMaximumSize(QSize(16777215, 230))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(9)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"QGroupBox{\n"
"	border:1px solid rgb(51,51,51);	\n"
"	border-radius:4px;\n"
"	color:white;\n"
"	background:rgb(91,90,90);\n"
"}\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 15, 0, 15)
        self.frame_1 = QFrame(self.groupBox)
        self.frame_1.setObjectName(u"frame_1")
        self.frame_1.setMinimumSize(QSize(0, 30))
        self.frame_1.setMaximumSize(QSize(16777215, 30))
        self.frame_1.setFrameShape(QFrame.NoFrame)
        self.frame_1.setFrameShadow(QFrame.Plain)
        self.frame_1.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.frame_1)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lab_function_name = QLabel(self.frame_1)
        self.lab_function_name.setObjectName(u"lab_function_name")
        self.lab_function_name.setMinimumSize(QSize(150, 20))
        self.lab_function_name.setMaximumSize(QSize(150, 30))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(16)
        self.lab_function_name.setFont(font1)
        self.lab_function_name.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_function_name.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.lab_function_name)

        self.line_function_name = QLineEdit(self.frame_1)
        self.line_function_name.setObjectName(u"line_function_name")
        self.line_function_name.setEnabled(True)
        self.line_function_name.setMinimumSize(QSize(300, 25))
        self.line_function_name.setMaximumSize(QSize(500, 25))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        self.line_function_name.setFont(font2)
        self.line_function_name.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.horizontalLayout.addWidget(self.line_function_name)

        self.horizontalSpacer = QSpacerItem(162, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.bn_function_delete = QPushButton(self.frame_1)
        self.bn_function_delete.setObjectName(u"bn_function_delete")
        self.bn_function_delete.setMinimumSize(QSize(40, 25))
        self.bn_function_delete.setMaximumSize(QSize(40, 25))
        self.bn_function_delete.setFont(font2)
        self.bn_function_delete.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.bn_function_delete.setCheckable(False)
        self.bn_function_delete.setFlat(True)

        self.horizontalLayout.addWidget(self.bn_function_delete)


        self.verticalLayout_2.addWidget(self.frame_1)

        self.frame_2 = QFrame(self.groupBox)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 30))
        self.frame_2.setMaximumSize(QSize(16777215, 30))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.frame_2.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lab_function_type = QLabel(self.frame_2)
        self.lab_function_type.setObjectName(u"lab_function_type")
        self.lab_function_type.setMinimumSize(QSize(150, 20))
        self.lab_function_type.setMaximumSize(QSize(150, 30))
        self.lab_function_type.setFont(font1)
        self.lab_function_type.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_function_type.setMidLineWidth(0)
        self.lab_function_type.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.lab_function_type)

        self.combo_function_type = QComboBox(self.frame_2)
        self.combo_function_type.setObjectName(u"combo_function_type")
        self.combo_function_type.setMinimumSize(QSize(300, 25))
        self.combo_function_type.setMaximumSize(QSize(500, 25))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        self.combo_function_type.setFont(font3)
        self.combo_function_type.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	border: 2px solid rgb(0,143,170);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(0,143,170);\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"	background: rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 5px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 5px;\n"
""
                        "}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/1x/arrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"")
        self.combo_function_type.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.combo_function_type.setFrame(False)
        self.combo_function_type.setModelColumn(0)

        self.horizontalLayout_2.addWidget(self.combo_function_type)

        self.horizontalSpacer_2 = QSpacerItem(162, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.groupBox)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setMinimumSize(QSize(0, 30))
        self.frame_3.setMaximumSize(QSize(16777215, 30))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.frame_3.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lab_function_par1 = QLabel(self.frame_3)
        self.lab_function_par1.setObjectName(u"lab_function_par1")
        self.lab_function_par1.setMinimumSize(QSize(80, 20))
        self.lab_function_par1.setMaximumSize(QSize(80, 30))
        self.lab_function_par1.setFont(font1)
        self.lab_function_par1.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_function_par1.setMidLineWidth(0)
        self.lab_function_par1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lab_function_par1)

        self.line_function_par1 = QLineEdit(self.frame_3)
        self.line_function_par1.setObjectName(u"line_function_par1")
        self.line_function_par1.setEnabled(True)
        self.line_function_par1.setMinimumSize(QSize(100, 25))
        self.line_function_par1.setMaximumSize(QSize(300, 25))
        self.line_function_par1.setFont(font2)
        self.line_function_par1.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.horizontalLayout_3.addWidget(self.line_function_par1)

        self.lab_function_val1 = QLabel(self.frame_3)
        self.lab_function_val1.setObjectName(u"lab_function_val1")
        self.lab_function_val1.setMinimumSize(QSize(150, 20))
        self.lab_function_val1.setMaximumSize(QSize(200, 30))
        self.lab_function_val1.setFont(font1)
        self.lab_function_val1.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_function_val1.setMidLineWidth(0)
        self.lab_function_val1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lab_function_val1)

        self.line_function_val1 = QLineEdit(self.frame_3)
        self.line_function_val1.setObjectName(u"line_function_val1")
        self.line_function_val1.setEnabled(True)
        self.line_function_val1.setMinimumSize(QSize(100, 25))
        self.line_function_val1.setMaximumSize(QSize(300, 25))
        self.line_function_val1.setFont(font2)
        self.line_function_val1.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.horizontalLayout_3.addWidget(self.line_function_val1)

        self.horizontalSpacer_3 = QSpacerItem(172, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.groupBox)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 30))
        self.frame_4.setMaximumSize(QSize(16777215, 30))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.frame_4.setLineWidth(0)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lab_function_val2 = QLabel(self.frame_4)
        self.lab_function_val2.setObjectName(u"lab_function_val2")
        self.lab_function_val2.setMinimumSize(QSize(80, 20))
        self.lab_function_val2.setMaximumSize(QSize(80, 30))
        self.lab_function_val2.setFont(font1)
        self.lab_function_val2.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_function_val2.setMidLineWidth(0)
        self.lab_function_val2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lab_function_val2)

        self.line_function_par2 = QLineEdit(self.frame_4)
        self.line_function_par2.setObjectName(u"line_function_par2")
        self.line_function_par2.setEnabled(True)
        self.line_function_par2.setMinimumSize(QSize(100, 25))
        self.line_function_par2.setMaximumSize(QSize(300, 25))
        self.line_function_par2.setFont(font2)
        self.line_function_par2.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.horizontalLayout_4.addWidget(self.line_function_par2)

        self.lab_function_par2 = QLabel(self.frame_4)
        self.lab_function_par2.setObjectName(u"lab_function_par2")
        self.lab_function_par2.setMinimumSize(QSize(150, 20))
        self.lab_function_par2.setMaximumSize(QSize(200, 30))
        self.lab_function_par2.setFont(font1)
        self.lab_function_par2.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_function_par2.setMidLineWidth(0)
        self.lab_function_par2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lab_function_par2)

        self.line_function_val2 = QLineEdit(self.frame_4)
        self.line_function_val2.setObjectName(u"line_function_val2")
        self.line_function_val2.setEnabled(True)
        self.line_function_val2.setMinimumSize(QSize(100, 25))
        self.line_function_val2.setMaximumSize(QSize(300, 25))
        self.line_function_val2.setFont(font2)
        self.line_function_val2.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.horizontalLayout_4.addWidget(self.line_function_val2)

        self.horizontalSpacer_4 = QSpacerItem(172, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.groupBox)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 30))
        self.frame_5.setMaximumSize(QSize(16777215, 30))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lab_function_min = QLabel(self.frame_5)
        self.lab_function_min.setObjectName(u"lab_function_min")
        self.lab_function_min.setMinimumSize(QSize(80, 20))
        self.lab_function_min.setMaximumSize(QSize(80, 30))
        self.lab_function_min.setFont(font1)
        self.lab_function_min.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_function_min.setMidLineWidth(0)
        self.lab_function_min.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.lab_function_min)

        self.line_function_min = QLineEdit(self.frame_5)
        self.line_function_min.setObjectName(u"line_function_min")
        self.line_function_min.setEnabled(True)
        self.line_function_min.setMinimumSize(QSize(100, 25))
        self.line_function_min.setMaximumSize(QSize(300, 25))
        self.line_function_min.setFont(font2)
        self.line_function_min.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.horizontalLayout_5.addWidget(self.line_function_min)

        self.lab_function_max = QLabel(self.frame_5)
        self.lab_function_max.setObjectName(u"lab_function_max")
        self.lab_function_max.setMinimumSize(QSize(80, 20))
        self.lab_function_max.setMaximumSize(QSize(80, 30))
        self.lab_function_max.setFont(font1)
        self.lab_function_max.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_function_max.setMidLineWidth(0)
        self.lab_function_max.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.lab_function_max)

        self.line_function_max = QLineEdit(self.frame_5)
        self.line_function_max.setObjectName(u"line_function_max")
        self.line_function_max.setEnabled(True)
        self.line_function_max.setMinimumSize(QSize(100, 25))
        self.line_function_max.setMaximumSize(QSize(300, 25))
        self.line_function_max.setFont(font2)
        self.line_function_max.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.horizontalLayout_5.addWidget(self.line_function_max)

        self.horizontalSpacer_5 = QSpacerItem(188, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.groupBox)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 30))
        self.frame_6.setMaximumSize(QSize(16777215, 30))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 0, 0, 0)
        self.cb_evaluate = QCheckBox(self.frame_6)
        self.cb_evaluate.setObjectName(u"cb_evaluate")
        self.cb_evaluate.setMinimumSize(QSize(80, 0))
        self.cb_evaluate.setFont(font)
        self.cb_evaluate.setStyleSheet(u"QCheckBox {\n"
"    color:rgb(255,255,255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border:2px solid rgb(51,51,51);\n"
"	background:rgb(91,90,90);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"	border:2px solid rgb(51,51,51);\n"
"   	background:rgb(0,143,170);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:pressed {\n"
"    border:2px solid rgb(51,51,51);\n"
"	background:rgb(91,90,90);\n"
"}\n"
"\n"
"")
        self.cb_evaluate.setTristate(False)

        self.horizontalLayout_6.addWidget(self.cb_evaluate)

        self.horizontalSpacer_6 = QSpacerItem(646, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addWidget(self.frame_6)


        self.verticalLayout_page_add1.addWidget(self.groupBox)

        StackedWidget.addWidget(self.page_define)

        self.retranslateUi(StackedWidget)

        StackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(StackedWidget)
    # setupUi

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(QCoreApplication.translate("StackedWidget", u"StackedWidget", None))
        self.bn_add_function.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("StackedWidget", u"Funkcija", None))
        self.lab_function_name.setText(QCoreApplication.translate("StackedWidget", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Ime funkcije:</span></p></body></html>", None))
        self.line_function_name.setText("")
        self.bn_function_delete.setText(QCoreApplication.translate("StackedWidget", u"-", None))
        self.lab_function_type.setText(QCoreApplication.translate("StackedWidget", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Vrsta funkcije:</span></p></body></html>", None))
        self.lab_function_par1.setText(QCoreApplication.translate("StackedWidget", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Koli\u010dina 1:</span></p></body></html>", None))
        self.line_function_par1.setText("")
        self.lab_function_val1.setText(QCoreApplication.translate("StackedWidget", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Vrednost koli\u010dine 1:</span></p></body></html>", None))
        self.line_function_val1.setText("")
        self.lab_function_val2.setText(QCoreApplication.translate("StackedWidget", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Koli\u010dina 2:</span></p></body></html>", None))
        self.line_function_par2.setText("")
        self.lab_function_par2.setText(QCoreApplication.translate("StackedWidget", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Vrednost koli\u010dine 2:</span></p></body></html>", None))
        self.line_function_val2.setText("")
        self.lab_function_min.setText(QCoreApplication.translate("StackedWidget", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">min:</span></p></body></html>", None))
        self.line_function_min.setText("")
        self.lab_function_max.setText(QCoreApplication.translate("StackedWidget", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">max:</span></p></body></html>", None))
        self.line_function_max.setText("")
        self.cb_evaluate.setText(QCoreApplication.translate("StackedWidget", u"Ovrednoti", None))
    # retranslateUi

