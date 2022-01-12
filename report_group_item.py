# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'report_group_item.ui'
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
        StackedWidget.resize(879, 50)
        StackedWidget.setMinimumSize(QSize(0, 50))
        StackedWidget.setMaximumSize(QSize(16777215, 50))
        StackedWidget.setStyleSheet(u"QFrame {\n"
"	background:rgb(90,90,90);\n"
"}")
        StackedWidget.setLineWidth(0)
        self.page_group_choose = QWidget()
        self.page_group_choose.setObjectName(u"page_group_choose")
        self.page_group_choose.setMinimumSize(QSize(0, 50))
        self.page_group_choose.setMaximumSize(QSize(16777215, 50))
        self.page_group_choose.setStyleSheet(u"QFrame {\n"
"	background:rgb(90,90,90);\n"
"}")
        self.verticalLayout_group_choose = QVBoxLayout(self.page_group_choose)
        self.verticalLayout_group_choose.setSpacing(0)
        self.verticalLayout_group_choose.setObjectName(u"verticalLayout_group_choose")
        self.verticalLayout_group_choose.setContentsMargins(0, 0, 0, 0)
        self.frame_group_choose = QFrame(self.page_group_choose)
        self.frame_group_choose.setObjectName(u"frame_group_choose")
        self.frame_group_choose.setMinimumSize(QSize(0, 50))
        self.frame_group_choose.setMaximumSize(QSize(16777215, 50))
        self.frame_group_choose.setFrameShape(QFrame.NoFrame)
        self.frame_group_choose.setFrameShadow(QFrame.Plain)
        self.frame_group_choose.setLineWidth(0)
        self.horizontalLayout_group_choose = QHBoxLayout(self.frame_group_choose)
        self.horizontalLayout_group_choose.setSpacing(6)
        self.horizontalLayout_group_choose.setObjectName(u"horizontalLayout_group_choose")
        self.horizontalLayout_group_choose.setContentsMargins(-1, 0, 0, 0)
        self.lab_excel_report_load = QLabel(self.frame_group_choose)
        self.lab_excel_report_load.setObjectName(u"lab_excel_report_load")
        self.lab_excel_report_load.setMinimumSize(QSize(150, 20))
        self.lab_excel_report_load.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(16)
        self.lab_excel_report_load.setFont(font)
        self.lab_excel_report_load.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_excel_report_load.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_group_choose.addWidget(self.lab_excel_report_load)

        self.combo_excel_group_choose = QComboBox(self.frame_group_choose)
        self.combo_excel_group_choose.setObjectName(u"combo_excel_group_choose")
        self.combo_excel_group_choose.setMinimumSize(QSize(300, 25))
        self.combo_excel_group_choose.setMaximumSize(QSize(500, 25))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        self.combo_excel_group_choose.setFont(font1)
        self.combo_excel_group_choose.setStyleSheet(u"QComboBox {\n"
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
        self.combo_excel_group_choose.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.combo_excel_group_choose.setFrame(False)
        self.combo_excel_group_choose.setModelColumn(0)

        self.horizontalLayout_group_choose.addWidget(self.combo_excel_group_choose)

        self.horizontalSpacer = QSpacerItem(355, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_group_choose.addItem(self.horizontalSpacer)


        self.verticalLayout_group_choose.addWidget(self.frame_group_choose)

        StackedWidget.addWidget(self.page_group_choose)
        self.page_other = QWidget()
        self.page_other.setObjectName(u"page_other")
        self.page_other.setMinimumSize(QSize(0, 50))
        self.page_other.setMaximumSize(QSize(16777215, 50))
        self.page_other.setStyleSheet(u"QWidget{\n"
"	background:rgb(91,90,90);\n"
"}\n"
"")
        self.verticalLayout_page_other = QVBoxLayout(self.page_other)
        self.verticalLayout_page_other.setSpacing(0)
        self.verticalLayout_page_other.setObjectName(u"verticalLayout_page_other")
        self.verticalLayout_page_other.setContentsMargins(2, 2, 2, 2)
        StackedWidget.addWidget(self.page_other)

        self.retranslateUi(StackedWidget)

        StackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(StackedWidget)
    # setupUi

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(QCoreApplication.translate("StackedWidget", u"StackedWidget", None))
        self.lab_excel_report_load.setText(QCoreApplication.translate("StackedWidget", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Skupina 1:</span></p></body></html>", None))
    # retranslateUi

