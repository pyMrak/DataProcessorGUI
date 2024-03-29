# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_my.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(903, 573)
        MainWindow.setMinimumSize(QSize(800, 550))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.centralwidget)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMaximumSize(QSize(16777215, 55))
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame_top)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toodle = QFrame(self.frame_top)
        self.frame_toodle.setObjectName(u"frame_toodle")
        self.frame_toodle.setMinimumSize(QSize(80, 55))
        self.frame_toodle.setMaximumSize(QSize(80, 55))
        self.frame_toodle.setStyleSheet(u"background:rgb(0,143,150);")
        self.frame_toodle.setFrameShape(QFrame.NoFrame)
        self.frame_toodle.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_toodle)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.toodle = QPushButton(self.frame_toodle)
        self.toodle.setObjectName(u"toodle")
        self.toodle.setMinimumSize(QSize(80, 55))
        self.toodle.setMaximumSize(QSize(80, 55))
        self.toodle.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,178,178);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon = QIcon()
        icon.addFile(u"icons/1x/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toodle.setIcon(icon)
        self.toodle.setIconSize(QSize(22, 12))
        self.toodle.setFlat(True)

        self.horizontalLayout_3.addWidget(self.toodle)


        self.horizontalLayout.addWidget(self.frame_toodle)

        self.frame_top_east = QFrame(self.frame_top)
        self.frame_top_east.setObjectName(u"frame_top_east")
        self.frame_top_east.setMaximumSize(QSize(16777215, 55))
        self.frame_top_east.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_top_east.setFrameShape(QFrame.NoFrame)
        self.frame_top_east.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_east)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_appname = QFrame(self.frame_top_east)
        self.frame_appname.setObjectName(u"frame_appname")
        self.frame_appname.setFrameShape(QFrame.NoFrame)
        self.frame_appname.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_appname)
        self.horizontalLayout_10.setSpacing(7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.lab_appname = QLabel(self.frame_appname)
        self.lab_appname.setObjectName(u"lab_appname")
        font = QFont()
        font.setFamily(u"Segoe UI Light")
        font.setPointSize(24)
        self.lab_appname.setFont(font)

        self.horizontalLayout_10.addWidget(self.lab_appname)


        self.horizontalLayout_4.addWidget(self.frame_appname)

        self.frame_user = QFrame(self.frame_top_east)
        self.frame_user.setObjectName(u"frame_user")
        self.frame_user.setFrameShape(QFrame.NoFrame)
        self.frame_user.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_user)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.lab_user = QLabel(self.frame_user)
        self.lab_user.setObjectName(u"lab_user")
        self.lab_user.setFont(font)
        self.lab_user.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_user.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.lab_user)


        self.horizontalLayout_4.addWidget(self.frame_user)

        self.frame_person = QFrame(self.frame_top_east)
        self.frame_person.setObjectName(u"frame_person")
        self.frame_person.setMinimumSize(QSize(55, 55))
        self.frame_person.setMaximumSize(QSize(55, 55))
        self.frame_person.setFrameShape(QFrame.NoFrame)
        self.frame_person.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_person)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lab_person = QLabel(self.frame_person)
        self.lab_person.setObjectName(u"lab_person")
        self.lab_person.setMaximumSize(QSize(55, 55))
        self.lab_person.setPixmap(QPixmap(u"icons/1x/peple.png"))
        self.lab_person.setScaledContents(False)
        self.lab_person.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.lab_person)


        self.horizontalLayout_4.addWidget(self.frame_person)

        self.frame_min = QFrame(self.frame_top_east)
        self.frame_min.setObjectName(u"frame_min")
        self.frame_min.setMinimumSize(QSize(55, 55))
        self.frame_min.setMaximumSize(QSize(55, 55))
        self.frame_min.setFrameShape(QFrame.NoFrame)
        self.frame_min.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_min)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.bn_min = QPushButton(self.frame_min)
        self.bn_min.setObjectName(u"bn_min")
        self.bn_min.setMaximumSize(QSize(55, 55))
        self.bn_min.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"icons/1x/hideAsset 53.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_min.setIcon(icon1)
        self.bn_min.setIconSize(QSize(22, 22))
        self.bn_min.setFlat(True)

        self.horizontalLayout_7.addWidget(self.bn_min)


        self.horizontalLayout_4.addWidget(self.frame_min)

        self.frame_max = QFrame(self.frame_top_east)
        self.frame_max.setObjectName(u"frame_max")
        self.frame_max.setMinimumSize(QSize(55, 55))
        self.frame_max.setMaximumSize(QSize(55, 55))
        self.frame_max.setFrameShape(QFrame.NoFrame)
        self.frame_max.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_max)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.bn_max = QPushButton(self.frame_max)
        self.bn_max.setObjectName(u"bn_max")
        self.bn_max.setMaximumSize(QSize(55, 55))
        self.bn_max.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"icons/1x/max.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_max.setIcon(icon2)
        self.bn_max.setIconSize(QSize(22, 22))
        self.bn_max.setFlat(True)

        self.horizontalLayout_6.addWidget(self.bn_max)


        self.horizontalLayout_4.addWidget(self.frame_max)

        self.frame_close = QFrame(self.frame_top_east)
        self.frame_close.setObjectName(u"frame_close")
        self.frame_close.setMinimumSize(QSize(55, 55))
        self.frame_close.setMaximumSize(QSize(55, 55))
        self.frame_close.setFrameShape(QFrame.NoFrame)
        self.frame_close.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_close)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.bn_close = QPushButton(self.frame_close)
        self.bn_close.setObjectName(u"bn_close")
        self.bn_close.setMaximumSize(QSize(55, 55))
        self.bn_close.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"icons/1x/closeAsset 43.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_close.setIcon(icon3)
        self.bn_close.setIconSize(QSize(22, 22))
        self.bn_close.setFlat(True)

        self.horizontalLayout_5.addWidget(self.bn_close)


        self.horizontalLayout_4.addWidget(self.frame_close)


        self.horizontalLayout.addWidget(self.frame_top_east)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_bottom = QFrame(self.centralwidget)
        self.frame_bottom.setObjectName(u"frame_bottom")
        self.frame_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_bottom.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_bottom)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_bottom_west = QFrame(self.frame_bottom)
        self.frame_bottom_west.setObjectName(u"frame_bottom_west")
        self.frame_bottom_west.setMinimumSize(QSize(80, 0))
        self.frame_bottom_west.setMaximumSize(QSize(80, 16777215))
        self.frame_bottom_west.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_bottom_west.setFrameShape(QFrame.NoFrame)
        self.frame_bottom_west.setFrameShadow(QFrame.Plain)
        self.frame_bottom_west.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.frame_bottom_west)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_measurements = QFrame(self.frame_bottom_west)
        self.frame_measurements.setObjectName(u"frame_measurements")
        self.frame_measurements.setMinimumSize(QSize(80, 55))
        self.frame_measurements.setMaximumSize(QSize(160, 55))
        self.frame_measurements.setFrameShape(QFrame.NoFrame)
        self.frame_measurements.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_measurements)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.bn_measurements = QPushButton(self.frame_measurements)
        self.bn_measurements.setObjectName(u"bn_measurements")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bn_measurements.sizePolicy().hasHeightForWidth())
        self.bn_measurements.setSizePolicy(sizePolicy)
        self.bn_measurements.setMinimumSize(QSize(80, 55))
        self.bn_measurements.setMaximumSize(QSize(160, 55))
        self.bn_measurements.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(80,180,180);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"icons/1x/paramAsset.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_measurements.setIcon(icon4)
        self.bn_measurements.setIconSize(QSize(23, 23))
        self.bn_measurements.setCheckable(False)
        self.bn_measurements.setChecked(False)
        self.bn_measurements.setFlat(True)

        self.horizontalLayout_30.addWidget(self.bn_measurements)


        self.verticalLayout_3.addWidget(self.frame_measurements)

        self.frame_functions = QFrame(self.frame_bottom_west)
        self.frame_functions.setObjectName(u"frame_functions")
        self.frame_functions.setMinimumSize(QSize(80, 55))
        self.frame_functions.setMaximumSize(QSize(160, 55))
        self.frame_functions.setFrameShape(QFrame.NoFrame)
        self.frame_functions.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_functions)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.bn_functions = QPushButton(self.frame_functions)
        self.bn_functions.setObjectName(u"bn_functions")
        self.bn_functions.setEnabled(True)
        sizePolicy.setHeightForWidth(self.bn_functions.sizePolicy().hasHeightForWidth())
        self.bn_functions.setSizePolicy(sizePolicy)
        self.bn_functions.setMinimumSize(QSize(80, 55))
        self.bn_functions.setMaximumSize(QSize(160, 55))
        self.bn_functions.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(80,180,180);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"icons/1x/functionAsset.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_functions.setIcon(icon5)
        self.bn_functions.setIconSize(QSize(30, 30))
        self.bn_functions.setCheckable(False)
        self.bn_functions.setFlat(True)

        self.horizontalLayout_49.addWidget(self.bn_functions)


        self.verticalLayout_3.addWidget(self.frame_functions)

        self.frame_reports = QFrame(self.frame_bottom_west)
        self.frame_reports.setObjectName(u"frame_reports")
        self.frame_reports.setMinimumSize(QSize(80, 55))
        self.frame_reports.setMaximumSize(QSize(160, 55))
        self.frame_reports.setFrameShape(QFrame.NoFrame)
        self.frame_reports.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_60 = QHBoxLayout(self.frame_reports)
        self.horizontalLayout_60.setSpacing(0)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.bn_reports = QPushButton(self.frame_reports)
        self.bn_reports.setObjectName(u"bn_reports")
        self.bn_reports.setEnabled(True)
        sizePolicy.setHeightForWidth(self.bn_reports.sizePolicy().hasHeightForWidth())
        self.bn_reports.setSizePolicy(sizePolicy)
        self.bn_reports.setMinimumSize(QSize(80, 55))
        self.bn_reports.setMaximumSize(QSize(160, 55))
        self.bn_reports.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(80,180,180);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"icons/1x/excelAsset.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_reports.setIcon(icon6)
        self.bn_reports.setIconSize(QSize(30, 30))
        self.bn_reports.setCheckable(False)
        self.bn_reports.setFlat(True)

        self.horizontalLayout_60.addWidget(self.bn_reports)


        self.verticalLayout_3.addWidget(self.frame_reports)

        self.frame_5 = QFrame(self.frame_bottom_west)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(80, 0))
        self.frame_5.setMaximumSize(QSize(80, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_5)


        self.horizontalLayout_2.addWidget(self.frame_bottom_west)

        self.frame_bottom_east = QFrame(self.frame_bottom)
        self.frame_bottom_east.setObjectName(u"frame_bottom_east")
        self.frame_bottom_east.setFrameShape(QFrame.NoFrame)
        self.frame_bottom_east.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame_bottom_east)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_bottom_east)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_14 = QHBoxLayout(self.frame)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 55))
        self.stackedWidget.setStyleSheet(u"")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.page_home.setStyleSheet(u"background:rgb(91,90,90);")
        self.horizontalLayout_19 = QHBoxLayout(self.page_home)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 5, 0, 5)
        self.frame_home_main = QFrame(self.page_home)
        self.frame_home_main.setObjectName(u"frame_home_main")
        self.frame_home_main.setFrameShape(QFrame.NoFrame)
        self.frame_home_main.setFrameShadow(QFrame.Plain)
        self.verticalLayout_5 = QVBoxLayout(self.frame_home_main)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.lab_home_main_hed = QLabel(self.frame_home_main)
        self.lab_home_main_hed.setObjectName(u"lab_home_main_hed")
        self.lab_home_main_hed.setMinimumSize(QSize(0, 55))
        self.lab_home_main_hed.setMaximumSize(QSize(16777215, 55))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semilight")
        font1.setPointSize(24)
        self.lab_home_main_hed.setFont(font1)
        self.lab_home_main_hed.setStyleSheet(u"QLabel {\n"
"	color:rgb(255,255,255);\n"
"}")
        self.lab_home_main_hed.setTextFormat(Qt.RichText)

        self.verticalLayout_5.addWidget(self.lab_home_main_hed)

        self.lab_home_main_disc = QLabel(self.frame_home_main)
        self.lab_home_main_disc.setObjectName(u"lab_home_main_disc")
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(10)
        self.lab_home_main_disc.setFont(font2)
        self.lab_home_main_disc.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_home_main_disc.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lab_home_main_disc.setWordWrap(True)
        self.lab_home_main_disc.setMargin(5)

        self.verticalLayout_5.addWidget(self.lab_home_main_disc)


        self.horizontalLayout_19.addWidget(self.frame_home_main)

        self.vert_divide = QFrame(self.page_home)
        self.vert_divide.setObjectName(u"vert_divide")
        self.vert_divide.setFrameShape(QFrame.VLine)
        self.vert_divide.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_19.addWidget(self.vert_divide)

        self.frame_home_stat = QFrame(self.page_home)
        self.frame_home_stat.setObjectName(u"frame_home_stat")
        self.frame_home_stat.setMinimumSize(QSize(220, 0))
        self.frame_home_stat.setMaximumSize(QSize(220, 16777215))
        self.frame_home_stat.setFrameShape(QFrame.NoFrame)
        self.frame_home_stat.setFrameShadow(QFrame.Plain)
        self.verticalLayout_6 = QVBoxLayout(self.frame_home_stat)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.lab_home_stat_hed = QLabel(self.frame_home_stat)
        self.lab_home_stat_hed.setObjectName(u"lab_home_stat_hed")
        self.lab_home_stat_hed.setMinimumSize(QSize(0, 55))
        self.lab_home_stat_hed.setMaximumSize(QSize(16777215, 55))
        self.lab_home_stat_hed.setFont(font1)
        self.lab_home_stat_hed.setStyleSheet(u"QLabel {\n"
"	color:rgb(255,255,255);\n"
"}")
        self.lab_home_stat_hed.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.lab_home_stat_hed)

        self.lab_home_stat_disc = QLabel(self.frame_home_stat)
        self.lab_home_stat_disc.setObjectName(u"lab_home_stat_disc")
        self.lab_home_stat_disc.setFont(font2)
        self.lab_home_stat_disc.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_6.addWidget(self.lab_home_stat_disc)


        self.horizontalLayout_19.addWidget(self.frame_home_stat)

        self.stackedWidget.addWidget(self.page_home)
        self.page_about_home = QWidget()
        self.page_about_home.setObjectName(u"page_about_home")
        self.page_about_home.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_13 = QVBoxLayout(self.page_about_home)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(5, 5, 5, 5)
        self.lab_about_home = QLabel(self.page_about_home)
        self.lab_about_home.setObjectName(u"lab_about_home")
        self.lab_about_home.setMinimumSize(QSize(0, 55))
        self.lab_about_home.setMaximumSize(QSize(16777215, 55))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(24)
        self.lab_about_home.setFont(font3)
        self.lab_about_home.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout_13.addWidget(self.lab_about_home)

        self.frame_about_home = QFrame(self.page_about_home)
        self.frame_about_home.setObjectName(u"frame_about_home")
        self.frame_about_home.setFrameShape(QFrame.StyledPanel)
        self.frame_about_home.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_about_home)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(5, 5, 0, 5)
        self.text_about_home = QTextEdit(self.frame_about_home)
        self.text_about_home.setObjectName(u"text_about_home")
        self.text_about_home.setEnabled(True)
        self.text_about_home.setFont(font2)
        self.text_about_home.setStyleSheet(u"color:rgb(255,255,255);")
        self.text_about_home.setFrameShape(QFrame.NoFrame)
        self.text_about_home.setFrameShadow(QFrame.Plain)
        self.text_about_home.setReadOnly(True)
        self.text_about_home.setTextInteractionFlags(Qt.TextBrowserInteraction)

        self.horizontalLayout_28.addWidget(self.text_about_home)

        self.vsb_about_home = QScrollBar(self.frame_about_home)
        self.vsb_about_home.setObjectName(u"vsb_about_home")
        self.vsb_about_home.setStyleSheet(u"QScrollBar:vertical {\n"
"	background:rgb(51,51,51);\n"
"    width:20px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background:rgb(0,143,170);\n"
"}\n"
"QScrollBar::add-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}\n"
"QScrollBar::sub-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}")
        self.vsb_about_home.setOrientation(Qt.Vertical)

        self.horizontalLayout_28.addWidget(self.vsb_about_home)


        self.verticalLayout_13.addWidget(self.frame_about_home)

        self.stackedWidget.addWidget(self.page_about_home)
        self.page_about_cloud = QWidget()
        self.page_about_cloud.setObjectName(u"page_about_cloud")
        self.page_about_cloud.setStyleSheet(u"background:rgb(91,90,90);")
        self.horizontalLayout_29 = QHBoxLayout(self.page_about_cloud)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_10 = QLabel(self.page_about_cloud)
        self.label_10.setObjectName(u"label_10")
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(30)
        self.label_10.setFont(font4)
        self.label_10.setStyleSheet(u"color:rgb(255,255,255);")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_10)

        self.stackedWidget.addWidget(self.page_about_cloud)
        self.page_about_android = QWidget()
        self.page_about_android.setObjectName(u"page_about_android")
        self.page_about_android.setStyleSheet(u"background:rgb(91,90,90);")
        self.stackedWidget.addWidget(self.page_about_android)
        self.page_about_bug = QWidget()
        self.page_about_bug.setObjectName(u"page_about_bug")
        self.page_about_bug.setStyleSheet(u"background:rgb(91,90,90);")
        self.stackedWidget.addWidget(self.page_about_bug)
        self.page_bug = QWidget()
        self.page_bug.setObjectName(u"page_bug")
        self.page_bug.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_7 = QVBoxLayout(self.page_bug)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.lab_Bug = QLabel(self.page_bug)
        self.lab_Bug.setObjectName(u"lab_Bug")
        self.lab_Bug.setMinimumSize(QSize(0, 55))
        self.lab_Bug.setMaximumSize(QSize(16777215, 55))
        self.lab_Bug.setFont(font1)
        self.lab_Bug.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout_7.addWidget(self.lab_Bug)

        self.frame_bug_main = QFrame(self.page_bug)
        self.frame_bug_main.setObjectName(u"frame_bug_main")
        self.frame_bug_main.setMinimumSize(QSize(0, 200))
        self.frame_bug_main.setMaximumSize(QSize(16777215, 200))
        self.frame_bug_main.setFrameShape(QFrame.NoFrame)
        self.frame_bug_main.setFrameShadow(QFrame.Plain)
        self.gridLayout = QGridLayout(self.frame_bug_main)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lab_bug1 = QLabel(self.frame_bug_main)
        self.lab_bug1.setObjectName(u"lab_bug1")
        self.lab_bug1.setMinimumSize(QSize(0, 0))
        self.lab_bug1.setMaximumSize(QSize(16777215, 16777215))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(14)
        self.lab_bug1.setFont(font5)
        self.lab_bug1.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_bug1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.lab_bug1, 0, 1, 1, 1)

        self.bn_bug_start = QPushButton(self.frame_bug_main)
        self.bn_bug_start.setObjectName(u"bn_bug_start")
        self.bn_bug_start.setMinimumSize(QSize(69, 25))
        self.bn_bug_start.setMaximumSize(QSize(69, 25))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(12)
        self.bn_bug_start.setFont(font6)
        self.bn_bug_start.setStyleSheet(u"QPushButton {\n"
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
        self.bn_bug_start.setCheckable(False)
        self.bn_bug_start.setFlat(True)

        self.gridLayout.addWidget(self.bn_bug_start, 3, 9, 1, 1)

        self.lab_bullet3 = QLabel(self.frame_bug_main)
        self.lab_bullet3.setObjectName(u"lab_bullet3")
        self.lab_bullet3.setMaximumSize(QSize(5, 16777215))
        self.lab_bullet3.setPixmap(QPixmap(u"icons/1x/bulletAsset 54.png"))

        self.gridLayout.addWidget(self.lab_bullet3, 2, 0, 1, 1)

        self.lab_bullet2 = QLabel(self.frame_bug_main)
        self.lab_bullet2.setObjectName(u"lab_bullet2")
        self.lab_bullet2.setMaximumSize(QSize(5, 16777215))
        self.lab_bullet2.setPixmap(QPixmap(u"icons/1x/bulletAsset 54.png"))

        self.gridLayout.addWidget(self.lab_bullet2, 1, 0, 1, 1)

        self.lab_bug3 = QLabel(self.frame_bug_main)
        self.lab_bug3.setObjectName(u"lab_bug3")
        self.lab_bug3.setFont(font5)

        self.gridLayout.addWidget(self.lab_bug3, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(421, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 5, 7, 1, 1)

        self.lab_bullet = QLabel(self.frame_bug_main)
        self.lab_bullet.setObjectName(u"lab_bullet")
        self.lab_bullet.setMaximumSize(QSize(5, 16777215))
        self.lab_bullet.setPixmap(QPixmap(u"icons/1x/bulletAsset 54.png"))
        self.lab_bullet.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lab_bullet, 0, 0, 1, 1)

        self.lab_bug2 = QLabel(self.frame_bug_main)
        self.lab_bug2.setObjectName(u"lab_bug2")
        self.lab_bug2.setFont(font5)
        self.lab_bug2.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout.addWidget(self.lab_bug2, 1, 1, 1, 1)

        self.lab_bug_action = QLabel(self.frame_bug_main)
        self.lab_bug_action.setObjectName(u"lab_bug_action")
        self.lab_bug_action.setMinimumSize(QSize(0, 20))
        self.lab_bug_action.setMaximumSize(QSize(16777215, 30))
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(16)
        self.lab_bug_action.setFont(font7)
        self.lab_bug_action.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_bug_action.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lab_bug_action, 3, 7, 1, 1)

        self.progressBar_bug = QProgressBar(self.frame_bug_main)
        self.progressBar_bug.setObjectName(u"progressBar_bug")
        self.progressBar_bug.setEnabled(True)
        self.progressBar_bug.setStyleSheet(u"QProgressBar\n"
"{\n"
"	color:rgb(255,255,255);\n"
"	background-color :rgb(51,51,51);\n"
"	border : 2px;\n"
"	border-radius:4px;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	border : 2px;\n"
"	border-radius:4px;\n"
"	background-color:rgb(0,143,170);\n"
"}")
        self.progressBar_bug.setValue(0)
        self.progressBar_bug.setAlignment(Qt.AlignCenter)
        self.progressBar_bug.setTextVisible(True)
        self.progressBar_bug.setOrientation(Qt.Horizontal)
        self.progressBar_bug.setInvertedAppearance(False)
        self.progressBar_bug.setTextDirection(QProgressBar.TopToBottom)

        self.gridLayout.addWidget(self.progressBar_bug, 4, 7, 1, 3)

        self.comboBox_bug = QComboBox(self.frame_bug_main)
        self.comboBox_bug.addItem("")
        self.comboBox_bug.addItem("")
        self.comboBox_bug.addItem("")
        self.comboBox_bug.addItem("")
        self.comboBox_bug.setObjectName(u"comboBox_bug")
        self.comboBox_bug.setMaximumSize(QSize(16777215, 25))
        self.comboBox_bug.setFont(font2)
        self.comboBox_bug.setStyleSheet(u"QComboBox {\n"
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
        self.comboBox_bug.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.comboBox_bug.setFrame(False)
        self.comboBox_bug.setModelColumn(0)

        self.gridLayout.addWidget(self.comboBox_bug, 3, 8, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_bug_main)

        self.verticalSpacer = QSpacerItem(20, 197, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.page_bug)
        self.page_cloud = QWidget()
        self.page_cloud.setObjectName(u"page_cloud")
        self.page_cloud.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_8 = QVBoxLayout(self.page_cloud)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.lab_cloud_main = QLabel(self.page_cloud)
        self.lab_cloud_main.setObjectName(u"lab_cloud_main")
        self.lab_cloud_main.setMinimumSize(QSize(0, 55))
        self.lab_cloud_main.setMaximumSize(QSize(16777215, 55))
        self.lab_cloud_main.setFont(font3)
        self.lab_cloud_main.setStyleSheet(u"QLabel {\n"
"	color:rgb(255,255,255);\n"
"}")

        self.verticalLayout_8.addWidget(self.lab_cloud_main)

        self.frame_2 = QFrame(self.page_cloud)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setEnabled(True)
        self.frame_2.setMinimumSize(QSize(0, 235))
        self.frame_2.setMaximumSize(QSize(16777215, 235))
        self.frame_2.setFont(font6)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 0))
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 0))
        self.label_3.setFont(font5)
        self.label_3.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 0))
        self.label_4.setFont(font5)
        self.label_4.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        self.line_cloud_proxy = QLineEdit(self.frame_2)
        self.line_cloud_proxy.setObjectName(u"line_cloud_proxy")
        self.line_cloud_proxy.setMinimumSize(QSize(400, 25))
        self.line_cloud_proxy.setMaximumSize(QSize(500, 25))
        self.line_cloud_proxy.setFont(font6)
        self.line_cloud_proxy.setStyleSheet(u"QLineEdit {\n"
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

        self.gridLayout_2.addWidget(self.line_cloud_proxy, 2, 1, 1, 3)

        self.line_cloud_id = QLineEdit(self.frame_2)
        self.line_cloud_id.setObjectName(u"line_cloud_id")
        self.line_cloud_id.setEnabled(True)
        self.line_cloud_id.setMinimumSize(QSize(400, 25))
        self.line_cloud_id.setMaximumSize(QSize(500, 25))
        self.line_cloud_id.setFont(font6)
        self.line_cloud_id.setStyleSheet(u"QLineEdit {\n"
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

        self.gridLayout_2.addWidget(self.line_cloud_id, 0, 1, 1, 3)

        self.line_cloud_adress = QLineEdit(self.frame_2)
        self.line_cloud_adress.setObjectName(u"line_cloud_adress")
        self.line_cloud_adress.setMinimumSize(QSize(400, 25))
        self.line_cloud_adress.setMaximumSize(QSize(500, 25))
        self.line_cloud_adress.setFont(font6)
        self.line_cloud_adress.setStyleSheet(u"QLineEdit {\n"
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

        self.gridLayout_2.addWidget(self.line_cloud_adress, 1, 1, 1, 3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 3, 0, 1, 2)

        self.bn_cloud_clear = QPushButton(self.frame_2)
        self.bn_cloud_clear.setObjectName(u"bn_cloud_clear")
        self.bn_cloud_clear.setEnabled(True)
        self.bn_cloud_clear.setMinimumSize(QSize(69, 25))
        self.bn_cloud_clear.setMaximumSize(QSize(69, 25))
        self.bn_cloud_clear.setFont(font6)
        self.bn_cloud_clear.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_2.addWidget(self.bn_cloud_clear, 3, 2, 1, 1)

        self.bn_cloud_connect = QPushButton(self.frame_2)
        self.bn_cloud_connect.setObjectName(u"bn_cloud_connect")
        self.bn_cloud_connect.setMinimumSize(QSize(69, 25))
        self.bn_cloud_connect.setMaximumSize(QSize(69, 25))
        self.bn_cloud_connect.setFont(font6)
        self.bn_cloud_connect.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_2.addWidget(self.bn_cloud_connect, 3, 3, 1, 1)


        self.verticalLayout_8.addWidget(self.frame_2)

        self.verticalSpacer_2 = QSpacerItem(20, 162, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.stackedWidget.addWidget(self.page_cloud)
        self.page_android = QWidget()
        self.page_android.setObjectName(u"page_android")
        self.page_android.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_9 = QVBoxLayout(self.page_android)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_android_menu = QFrame(self.page_android)
        self.frame_android_menu.setObjectName(u"frame_android_menu")
        self.frame_android_menu.setEnabled(False)
        self.frame_android_menu.setMinimumSize(QSize(0, 30))
        self.frame_android_menu.setMaximumSize(QSize(16777215, 30))
        self.frame_android_menu.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_android_menu.setFrameShape(QFrame.NoFrame)
        self.frame_android_menu.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_android_menu)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_android_contact = QFrame(self.frame_android_menu)
        self.frame_android_contact.setObjectName(u"frame_android_contact")
        self.frame_android_contact.setMinimumSize(QSize(80, 30))
        self.frame_android_contact.setMaximumSize(QSize(80, 30))
        self.frame_android_contact.setFrameShape(QFrame.NoFrame)
        self.frame_android_contact.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_android_contact)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.bn_android_contact = QPushButton(self.frame_android_contact)
        self.bn_android_contact.setObjectName(u"bn_android_contact")
        self.bn_android_contact.setMinimumSize(QSize(80, 30))
        self.bn_android_contact.setMaximumSize(QSize(80, 30))
        self.bn_android_contact.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"icons/1x/bookAsset 57.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_android_contact.setIcon(icon7)
        self.bn_android_contact.setIconSize(QSize(13, 16))
        self.bn_android_contact.setFlat(True)

        self.horizontalLayout_21.addWidget(self.bn_android_contact)


        self.horizontalLayout_20.addWidget(self.frame_android_contact)

        self.frame_android_game = QFrame(self.frame_android_menu)
        self.frame_android_game.setObjectName(u"frame_android_game")
        self.frame_android_game.setMinimumSize(QSize(80, 30))
        self.frame_android_game.setMaximumSize(QSize(80, 30))
        self.frame_android_game.setFrameShape(QFrame.NoFrame)
        self.frame_android_game.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_android_game)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.bn_android_game = QPushButton(self.frame_android_game)
        self.bn_android_game.setObjectName(u"bn_android_game")
        self.bn_android_game.setEnabled(False)
        self.bn_android_game.setMinimumSize(QSize(80, 30))
        self.bn_android_game.setMaximumSize(QSize(80, 30))
        self.bn_android_game.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"icons/1x/gameAsset 61.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_android_game.setIcon(icon8)
        self.bn_android_game.setIconSize(QSize(20, 13))
        self.bn_android_game.setFlat(True)

        self.horizontalLayout_22.addWidget(self.bn_android_game)


        self.horizontalLayout_20.addWidget(self.frame_android_game)

        self.frame_android_clean = QFrame(self.frame_android_menu)
        self.frame_android_clean.setObjectName(u"frame_android_clean")
        self.frame_android_clean.setMinimumSize(QSize(80, 30))
        self.frame_android_clean.setMaximumSize(QSize(80, 30))
        self.frame_android_clean.setFrameShape(QFrame.NoFrame)
        self.frame_android_clean.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_android_clean)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.bn_android_clean = QPushButton(self.frame_android_clean)
        self.bn_android_clean.setObjectName(u"bn_android_clean")
        self.bn_android_clean.setMinimumSize(QSize(80, 30))
        self.bn_android_clean.setMaximumSize(QSize(80, 30))
        self.bn_android_clean.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"icons/1x/cleanAsset 59.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_android_clean.setIcon(icon9)
        self.bn_android_clean.setFlat(True)

        self.horizontalLayout_23.addWidget(self.bn_android_clean)


        self.horizontalLayout_20.addWidget(self.frame_android_clean)

        self.frame_android_world = QFrame(self.frame_android_menu)
        self.frame_android_world.setObjectName(u"frame_android_world")
        self.frame_android_world.setMinimumSize(QSize(80, 30))
        self.frame_android_world.setMaximumSize(QSize(80, 30))
        self.frame_android_world.setFrameShape(QFrame.NoFrame)
        self.frame_android_world.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_android_world)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.bn_android_world = QPushButton(self.frame_android_world)
        self.bn_android_world.setObjectName(u"bn_android_world")
        self.bn_android_world.setEnabled(False)
        self.bn_android_world.setMinimumSize(QSize(80, 30))
        self.bn_android_world.setMaximumSize(QSize(80, 30))
        self.bn_android_world.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u"icons/1x/worldAsset 60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_android_world.setIcon(icon10)
        self.bn_android_world.setFlat(True)

        self.horizontalLayout_24.addWidget(self.bn_android_world)


        self.horizontalLayout_20.addWidget(self.frame_android_world)

        self.horizontalSpacer_4 = QSpacerItem(397, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_4)


        self.verticalLayout_9.addWidget(self.frame_android_menu)

        self.stackedWidget_android = QStackedWidget(self.page_android)
        self.stackedWidget_android.setObjectName(u"stackedWidget_android")
        self.stackedWidget_android.setStyleSheet(u"background:rgb(91,90,90);")
        self.page_android_contact = QWidget()
        self.page_android_contact.setObjectName(u"page_android_contact")
        self.page_android_contact.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_10 = QVBoxLayout(self.page_android_contact)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.lab_android_contact = QLabel(self.page_android_contact)
        self.lab_android_contact.setObjectName(u"lab_android_contact")
        self.lab_android_contact.setMinimumSize(QSize(0, 55))
        self.lab_android_contact.setMaximumSize(QSize(16777215, 55))
        self.lab_android_contact.setFont(font3)
        self.lab_android_contact.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout_10.addWidget(self.lab_android_contact)

        self.frame_android_bottom = QFrame(self.page_android_contact)
        self.frame_android_bottom.setObjectName(u"frame_android_bottom")
        self.frame_android_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_android_bottom.setFrameShadow(QFrame.Plain)
        self.gridLayout_3 = QGridLayout(self.frame_android_bottom)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.lab_person_icon = QLabel(self.frame_android_bottom)
        self.lab_person_icon.setObjectName(u"lab_person_icon")
        self.lab_person_icon.setMinimumSize(QSize(200, 160))
        self.lab_person_icon.setMaximumSize(QSize(200, 160))
        self.lab_person_icon.setPixmap(QPixmap(u"icons/1x/peopleAsset 62.png"))

        self.gridLayout_3.addWidget(self.lab_person_icon, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.frame_android_field = QFrame(self.frame_android_bottom)
        self.frame_android_field.setObjectName(u"frame_android_field")
        self.frame_android_field.setFrameShape(QFrame.NoFrame)
        self.frame_android_field.setFrameShadow(QFrame.Plain)
        self.gridLayout_4 = QGridLayout(self.frame_android_field)
        self.gridLayout_4.setSpacing(5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.label_8 = QLabel(self.frame_android_field)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font5)
        self.label_8.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label_8, 7, 0, 1, 1)

        self.label_6 = QLabel(self.frame_android_field)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font5)
        self.label_6.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label_6, 4, 0, 1, 1)

        self.label_7 = QLabel(self.frame_android_field)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font5)
        self.label_7.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label_7, 5, 0, 1, 1)

        self.label = QLabel(self.frame_android_field)
        self.label.setObjectName(u"label")
        self.label.setFont(font5)
        self.label.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 3)

        self.line_android_name = QLineEdit(self.frame_android_field)
        self.line_android_name.setObjectName(u"line_android_name")
        self.line_android_name.setEnabled(False)
        self.line_android_name.setMinimumSize(QSize(300, 25))
        self.line_android_name.setMaximumSize(QSize(400, 25))
        self.line_android_name.setFont(font6)
        self.line_android_name.setStyleSheet(u"QLineEdit {\n"
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

        self.gridLayout_4.addWidget(self.line_android_name, 1, 3, 1, 1)

        self.label_5 = QLabel(self.frame_android_field)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font5)
        self.label_5.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label_5, 3, 0, 1, 3)

        self.line_android_org = QLineEdit(self.frame_android_field)
        self.line_android_org.setObjectName(u"line_android_org")
        self.line_android_org.setEnabled(False)
        self.line_android_org.setMinimumSize(QSize(300, 25))
        self.line_android_org.setMaximumSize(QSize(400, 25))
        self.line_android_org.setFont(font6)
        self.line_android_org.setStyleSheet(u"QLineEdit {\n"
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

        self.gridLayout_4.addWidget(self.line_android_org, 4, 3, 1, 1)

        self.line_android_adress = QLineEdit(self.frame_android_field)
        self.line_android_adress.setObjectName(u"line_android_adress")
        self.line_android_adress.setEnabled(False)
        self.line_android_adress.setMinimumSize(QSize(300, 25))
        self.line_android_adress.setMaximumSize(QSize(400, 25))
        self.line_android_adress.setFont(font6)
        self.line_android_adress.setStyleSheet(u"QLineEdit {\n"
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

        self.gridLayout_4.addWidget(self.line_android_adress, 3, 3, 1, 1)

        self.line_android_ph = QLineEdit(self.frame_android_field)
        self.line_android_ph.setObjectName(u"line_android_ph")
        self.line_android_ph.setEnabled(False)
        self.line_android_ph.setMinimumSize(QSize(300, 25))
        self.line_android_ph.setMaximumSize(QSize(400, 25))
        self.line_android_ph.setFont(font6)
        self.line_android_ph.setStyleSheet(u"QLineEdit {\n"
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

        self.gridLayout_4.addWidget(self.line_android_ph, 7, 3, 1, 1)

        self.line_android_email = QLineEdit(self.frame_android_field)
        self.line_android_email.setObjectName(u"line_android_email")
        self.line_android_email.setEnabled(False)
        self.line_android_email.setMinimumSize(QSize(300, 25))
        self.line_android_email.setMaximumSize(QSize(400, 25))
        self.line_android_email.setFont(font6)
        self.line_android_email.setStyleSheet(u"QLineEdit {\n"
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

        self.gridLayout_4.addWidget(self.line_android_email, 5, 3, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 8, 8, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_5, 4, 8, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_4, 9, 3, 1, 1)

        self.frame_3 = QFrame(self.frame_android_field)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(100, 0, 0, 0)
        self.bn_android_contact_edit = QPushButton(self.frame_3)
        self.bn_android_contact_edit.setObjectName(u"bn_android_contact_edit")
        self.bn_android_contact_edit.setMinimumSize(QSize(69, 25))
        self.bn_android_contact_edit.setMaximumSize(QSize(69, 25))
        self.bn_android_contact_edit.setFont(font6)
        self.bn_android_contact_edit.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_25.addWidget(self.bn_android_contact_edit)

        self.bn_android_contact_share = QPushButton(self.frame_3)
        self.bn_android_contact_share.setObjectName(u"bn_android_contact_share")
        self.bn_android_contact_share.setMinimumSize(QSize(69, 25))
        self.bn_android_contact_share.setMaximumSize(QSize(69, 25))
        self.bn_android_contact_share.setFont(font6)
        self.bn_android_contact_share.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_25.addWidget(self.bn_android_contact_share)

        self.bn_android_contact_delete = QPushButton(self.frame_3)
        self.bn_android_contact_delete.setObjectName(u"bn_android_contact_delete")
        self.bn_android_contact_delete.setMinimumSize(QSize(69, 25))
        self.bn_android_contact_delete.setMaximumSize(QSize(69, 25))
        self.bn_android_contact_delete.setFont(font6)
        self.bn_android_contact_delete.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(112,0,0);\n"
"	background-color: rgb(112,0,0);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(112,0,0);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.horizontalLayout_25.addWidget(self.bn_android_contact_delete)

        self.bn_android_contact_save = QPushButton(self.frame_3)
        self.bn_android_contact_save.setObjectName(u"bn_android_contact_save")
        self.bn_android_contact_save.setEnabled(False)
        self.bn_android_contact_save.setMinimumSize(QSize(69, 25))
        self.bn_android_contact_save.setMaximumSize(QSize(69, 25))
        self.bn_android_contact_save.setFont(font6)
        self.bn_android_contact_save.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_25.addWidget(self.bn_android_contact_save)


        self.gridLayout_4.addWidget(self.frame_3, 8, 0, 1, 7)


        self.gridLayout_3.addWidget(self.frame_android_field, 0, 1, 2, 1)


        self.verticalLayout_10.addWidget(self.frame_android_bottom)

        self.stackedWidget_android.addWidget(self.page_android_contact)
        self.page_android_game = QWidget()
        self.page_android_game.setObjectName(u"page_android_game")
        self.page_android_game.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_11 = QVBoxLayout(self.page_android_game)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.lab_gamepad = QLabel(self.page_android_game)
        self.lab_gamepad.setObjectName(u"lab_gamepad")
        self.lab_gamepad.setMinimumSize(QSize(0, 55))
        self.lab_gamepad.setMaximumSize(QSize(16777215, 55))
        self.lab_gamepad.setFont(font3)
        self.lab_gamepad.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout_11.addWidget(self.lab_gamepad)

        self.frame_textbar = QFrame(self.page_android_game)
        self.frame_textbar.setObjectName(u"frame_textbar")
        self.frame_textbar.setStyleSheet(u"background:rgb(91,90,90);")
        self.frame_textbar.setFrameShape(QFrame.StyledPanel)
        self.frame_textbar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_textbar)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(5, 0, 0, 0)
        self.textEdit_gamepad = QTextEdit(self.frame_textbar)
        self.textEdit_gamepad.setObjectName(u"textEdit_gamepad")
        self.textEdit_gamepad.setFont(font6)
        self.textEdit_gamepad.setStyleSheet(u"color:rgb(255,255,255);")
        self.textEdit_gamepad.setFrameShape(QFrame.NoFrame)
        self.textEdit_gamepad.setFrameShadow(QFrame.Plain)
        self.textEdit_gamepad.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.textEdit_gamepad.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_26.addWidget(self.textEdit_gamepad)

        self.vsb_gamepad = QScrollBar(self.frame_textbar)
        self.vsb_gamepad.setObjectName(u"vsb_gamepad")
        self.vsb_gamepad.setStyleSheet(u"QScrollBar:vertical {\n"
"	background:rgb(51,51,51);\n"
"    width:20px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background:rgb(0,143,170);\n"
"}\n"
"QScrollBar::add-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}\n"
"QScrollBar::sub-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}")
        self.vsb_gamepad.setOrientation(Qt.Vertical)
        self.vsb_gamepad.setInvertedControls(True)

        self.horizontalLayout_26.addWidget(self.vsb_gamepad)


        self.verticalLayout_11.addWidget(self.frame_textbar)

        self.stackedWidget_android.addWidget(self.page_android_game)
        self.page_android_clean = QWidget()
        self.page_android_clean.setObjectName(u"page_android_clean")
        self.page_android_clean.setStyleSheet(u"background:rgb(91,90,90);")
        self.gridLayout_5 = QGridLayout(self.page_android_clean)
        self.gridLayout_5.setSpacing(5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(5, 5, 5, 5)
        self.groupBox_clean = QGroupBox(self.page_android_clean)
        self.groupBox_clean.setObjectName(u"groupBox_clean")
        self.groupBox_clean.setMinimumSize(QSize(250, 300))
        self.groupBox_clean.setMaximumSize(QSize(250, 300))
        self.groupBox_clean.setSizeIncrement(QSize(0, 0))
        self.groupBox_clean.setFont(font2)
        self.groupBox_clean.setStyleSheet(u"QGroupBox{\n"
"	border:1px solid rgb(51,51,51);	\n"
"	border-radius:4px;\n"
"	color:white;\n"
"	background:rgb(91,90,90);\n"
"}\n"
"")
        self.groupBox_clean.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupBox_clean.setFlat(False)
        self.groupBox_clean.setCheckable(False)
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_clean)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.radioButton_2 = QRadioButton(self.groupBox_clean)
        self.radioButton_2.setObjectName(u"radioButton_2")
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(9)
        self.radioButton_2.setFont(font8)
        self.radioButton_2.setStyleSheet(u"QRadioButton {\n"
"	background:rgb(91,90,90);\n"
"    color:white;\n"
"}\n"
"QRadioButton::indicator {\n"
"    width:10px;\n"
"    height:10px;\n"
"    border-radius: 7px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:rgb(91,90,90);\n"
"    border:2px solid rgb(51,51,51);\n"
"}")
        self.radioButton_2.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.radioButton_2)

        self.radioButton = QRadioButton(self.groupBox_clean)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setFont(font8)
        self.radioButton.setStyleSheet(u"QRadioButton {\n"
"	background:rgb(91,90,90);\n"
"    color:white;\n"
"}\n"
"QRadioButton::indicator {\n"
"    width:10px;\n"
"    height:10px;\n"
"    border-radius: 7px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:rgb(91,90,90);\n"
"    border:2px solid rgb(51,51,51);\n"
"}")
        self.radioButton.setAutoRepeat(False)
        self.radioButton.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.radioButton)

        self.radioButton_3 = QRadioButton(self.groupBox_clean)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setFont(font8)
        self.radioButton_3.setStyleSheet(u"QRadioButton {\n"
"	background:rgb(91,90,90);\n"
"    color:white;\n"
"}\n"
"QRadioButton::indicator {\n"
"    width:10px;\n"
"    height:10px;\n"
"    border-radius: 7px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:rgb(91,90,90);\n"
"    border:2px solid rgb(51,51,51);\n"
"}")
        self.radioButton_3.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.groupBox_clean)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setFont(font8)
        self.radioButton_4.setStyleSheet(u"QRadioButton {\n"
"	background:rgb(91,90,90);\n"
"    color:white;\n"
"}\n"
"QRadioButton::indicator {\n"
"    width:10px;\n"
"    height:10px;\n"
"    border-radius: 7px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:rgb(91,90,90);\n"
"    border:2px solid rgb(51,51,51);\n"
"}")
        self.radioButton_4.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.radioButton_4)

        self.checkBox = QCheckBox(self.groupBox_clean)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setFont(font8)
        self.checkBox.setStyleSheet(u"QCheckBox {\n"
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
        self.checkBox.setTristate(False)

        self.verticalLayout_12.addWidget(self.checkBox)

        self.checkBox_4 = QCheckBox(self.groupBox_clean)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setFont(font8)
        self.checkBox_4.setStyleSheet(u"QCheckBox {\n"
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
        self.checkBox_4.setTristate(False)

        self.verticalLayout_12.addWidget(self.checkBox_4)

        self.checkBox_2 = QCheckBox(self.groupBox_clean)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setFont(font8)
        self.checkBox_2.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_12.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.groupBox_clean)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setFont(font8)
        self.checkBox_3.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_12.addWidget(self.checkBox_3)


        self.gridLayout_5.addWidget(self.groupBox_clean, 2, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_7, 2, 7, 1, 1)

        self.lab_clean = QLabel(self.page_android_clean)
        self.lab_clean.setObjectName(u"lab_clean")
        self.lab_clean.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.lab_clean, 3, 2, 2, 2)

        self.groupBox = QGroupBox(self.page_android_clean)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(250, 300))
        self.groupBox.setMaximumSize(QSize(250, 300))
        self.groupBox.setFont(font8)
        self.groupBox.setStyleSheet(u"QGroupBox{\n"
"	border:1px solid rgb(51,51,51);	\n"
"	border-radius:4px;\n"
"	color:white;\n"
"	background:rgb(91,90,90);\n"
"}\n"
"")
        self.gridLayout_6 = QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalSlider = QSlider(self.groupBox)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"QSlider::groove:vertical {\n"
"    background: red;\n"
"    width:5px\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 10px;\n"
"    background:rgb(0,143,170);\n"
"	margin:0 -8px\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background:rgb(51,51,51);\n"
"}")
        self.verticalSlider.setTracking(True)
        self.verticalSlider.setOrientation(Qt.Vertical)
        self.verticalSlider.setInvertedAppearance(False)
        self.verticalSlider.setInvertedControls(False)
        self.verticalSlider.setTickPosition(QSlider.NoTicks)

        self.gridLayout_6.addWidget(self.verticalSlider, 2, 1, 1, 1)

        self.horizontalSlider_2 = QSlider(self.groupBox)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    height:5px;\n"
"    background: rgb(51,51,51);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background:rgb(0,143,170);\n"
"    width: 10px;\n"
"margin:-8px 0\n"
"}\n"
"\n"
"QSlider::add-page:horizondal {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"QSlider::sub-page:horizondal {\n"
"    background:rgb(51,51,51);\n"
"}")
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.gridLayout_6.addWidget(self.horizontalSlider_2, 2, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox, 2, 6, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_5, 3, 0, 1, 1)

        self.stackedWidget_android.addWidget(self.page_android_clean)
        self.page_android_world = QWidget()
        self.page_android_world.setObjectName(u"page_android_world")
        self.page_android_world.setStyleSheet(u"background:rgb(91,90,90);")
        self.horizontalLayout_27 = QHBoxLayout(self.page_android_world)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_9 = QLabel(self.page_android_world)
        self.label_9.setObjectName(u"label_9")
        font9 = QFont()
        font9.setFamily(u"Segoe UI Light")
        font9.setPointSize(30)
        self.label_9.setFont(font9)
        self.label_9.setStyleSheet(u"color:rgb(255,255,255);")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setWordWrap(True)

        self.horizontalLayout_27.addWidget(self.label_9)

        self.stackedWidget_android.addWidget(self.page_android_world)

        self.verticalLayout_9.addWidget(self.stackedWidget_android)

        self.stackedWidget.addWidget(self.page_android)
        self.page_measurements = QWidget()
        self.page_measurements.setObjectName(u"page_measurements")
        self.verticalLayout_91 = QVBoxLayout(self.page_measurements)
        self.verticalLayout_91.setSpacing(0)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.verticalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.frame_measurement_menu = QFrame(self.page_measurements)
        self.frame_measurement_menu.setObjectName(u"frame_measurement_menu")
        self.frame_measurement_menu.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_measurement_menu.sizePolicy().hasHeightForWidth())
        self.frame_measurement_menu.setSizePolicy(sizePolicy1)
        self.frame_measurement_menu.setMinimumSize(QSize(0, 30))
        self.frame_measurement_menu.setMaximumSize(QSize(16777215, 30))
        self.frame_measurement_menu.setFocusPolicy(Qt.StrongFocus)
        self.frame_measurement_menu.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_measurement_menu.setFrameShape(QFrame.NoFrame)
        self.frame_measurement_menu.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_measurement_menu)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.frame_group_1 = QFrame(self.frame_measurement_menu)
        self.frame_group_1.setObjectName(u"frame_group_1")
        self.frame_group_1.setEnabled(True)
        self.frame_group_1.setMinimumSize(QSize(120, 30))
        self.frame_group_1.setFrameShape(QFrame.NoFrame)
        self.frame_group_1.setFrameShadow(QFrame.Plain)
        self.frame_group_1.setLineWidth(0)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_group_1)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.bn_group_1 = QPushButton(self.frame_group_1)
        self.bn_group_1.setObjectName(u"bn_group_1")
        self.bn_group_1.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.bn_group_1.sizePolicy().hasHeightForWidth())
        self.bn_group_1.setSizePolicy(sizePolicy2)
        self.bn_group_1.setMinimumSize(QSize(120, 30))
        self.bn_group_1.setMaximumSize(QSize(16777215, 30))
        self.bn_group_1.setStyleSheet(u"QPushButton {\n"
"    color: rgba(255,255,255,255);\n"
"    font-weight: 900;\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_group_1.setFlat(True)

        self.horizontalLayout_32.addWidget(self.bn_group_1)


        self.horizontalLayout_31.addWidget(self.frame_group_1)

        self.frame_group_2 = QFrame(self.frame_measurement_menu)
        self.frame_group_2.setObjectName(u"frame_group_2")
        self.frame_group_2.setMinimumSize(QSize(120, 30))
        self.frame_group_2.setFrameShape(QFrame.NoFrame)
        self.frame_group_2.setFrameShadow(QFrame.Plain)
        self.frame_group_2.setLineWidth(0)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_group_2)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.bn_group_2 = QPushButton(self.frame_group_2)
        self.bn_group_2.setObjectName(u"bn_group_2")
        self.bn_group_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.bn_group_2.sizePolicy().hasHeightForWidth())
        self.bn_group_2.setSizePolicy(sizePolicy)
        self.bn_group_2.setMinimumSize(QSize(120, 30))
        self.bn_group_2.setMaximumSize(QSize(16777215, 30))
        self.bn_group_2.setStyleSheet(u"QPushButton {\n"
"    color: rgba(255,255,255,255);\n"
"    font-weight: 900;\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u"icons/1x/addAsset.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_group_2.setIcon(icon11)
        self.bn_group_2.setFlat(True)

        self.horizontalLayout_33.addWidget(self.bn_group_2)


        self.horizontalLayout_31.addWidget(self.frame_group_2)

        self.frame_group_3 = QFrame(self.frame_measurement_menu)
        self.frame_group_3.setObjectName(u"frame_group_3")
        self.frame_group_3.setMinimumSize(QSize(120, 30))
        self.frame_group_3.setFrameShape(QFrame.NoFrame)
        self.frame_group_3.setFrameShadow(QFrame.Plain)
        self.frame_group_3.setLineWidth(0)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_group_3)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.bn_group_3 = QPushButton(self.frame_group_3)
        self.bn_group_3.setObjectName(u"bn_group_3")
        self.bn_group_3.setEnabled(False)
        sizePolicy.setHeightForWidth(self.bn_group_3.sizePolicy().hasHeightForWidth())
        self.bn_group_3.setSizePolicy(sizePolicy)
        self.bn_group_3.setMinimumSize(QSize(120, 30))
        self.bn_group_3.setMaximumSize(QSize(16777215, 30))
        self.bn_group_3.setStyleSheet(u"QPushButton {\n"
"    color: rgba(255,255,255,255);\n"
"    font-weight: 900;\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_group_3.setFlat(True)

        self.horizontalLayout_34.addWidget(self.bn_group_3)


        self.horizontalLayout_31.addWidget(self.frame_group_3)

        self.frame_group_4 = QFrame(self.frame_measurement_menu)
        self.frame_group_4.setObjectName(u"frame_group_4")
        self.frame_group_4.setMinimumSize(QSize(120, 30))
        self.frame_group_4.setFrameShape(QFrame.NoFrame)
        self.frame_group_4.setFrameShadow(QFrame.Plain)
        self.frame_group_4.setLineWidth(0)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_group_4)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.bn_group_4 = QPushButton(self.frame_group_4)
        self.bn_group_4.setObjectName(u"bn_group_4")
        self.bn_group_4.setEnabled(False)
        sizePolicy.setHeightForWidth(self.bn_group_4.sizePolicy().hasHeightForWidth())
        self.bn_group_4.setSizePolicy(sizePolicy)
        self.bn_group_4.setMinimumSize(QSize(120, 30))
        self.bn_group_4.setMaximumSize(QSize(16777215, 30))
        self.bn_group_4.setStyleSheet(u"QPushButton {\n"
"    color: rgba(255,255,255,255);\n"
"    font-weight: 900;\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_group_4.setFlat(True)

        self.horizontalLayout_35.addWidget(self.bn_group_4)


        self.horizontalLayout_31.addWidget(self.frame_group_4)

        self.frame_group_5 = QFrame(self.frame_measurement_menu)
        self.frame_group_5.setObjectName(u"frame_group_5")
        self.frame_group_5.setMinimumSize(QSize(120, 30))
        self.frame_group_5.setFrameShape(QFrame.NoFrame)
        self.frame_group_5.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_group_5)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.bn_group_5 = QPushButton(self.frame_group_5)
        self.bn_group_5.setObjectName(u"bn_group_5")
        self.bn_group_5.setEnabled(False)
        sizePolicy.setHeightForWidth(self.bn_group_5.sizePolicy().hasHeightForWidth())
        self.bn_group_5.setSizePolicy(sizePolicy)
        self.bn_group_5.setMinimumSize(QSize(120, 30))
        self.bn_group_5.setMaximumSize(QSize(16777215, 30))
        self.bn_group_5.setStyleSheet(u"QPushButton {\n"
"    color: rgba(255,255,255,255);\n"
"    font-weight: 900;\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_group_5.setFlat(True)

        self.horizontalLayout_36.addWidget(self.bn_group_5)


        self.horizontalLayout_31.addWidget(self.frame_group_5)

        self.frame_group_6 = QFrame(self.frame_measurement_menu)
        self.frame_group_6.setObjectName(u"frame_group_6")
        self.frame_group_6.setMinimumSize(QSize(120, 30))
        self.frame_group_6.setMaximumSize(QSize(240, 30))
        self.frame_group_6.setFrameShape(QFrame.NoFrame)
        self.frame_group_6.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_group_6)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.bn_group_6 = QPushButton(self.frame_group_6)
        self.bn_group_6.setObjectName(u"bn_group_6")
        self.bn_group_6.setEnabled(False)
        sizePolicy.setHeightForWidth(self.bn_group_6.sizePolicy().hasHeightForWidth())
        self.bn_group_6.setSizePolicy(sizePolicy)
        self.bn_group_6.setMinimumSize(QSize(120, 30))
        self.bn_group_6.setMaximumSize(QSize(16777215, 30))
        self.bn_group_6.setStyleSheet(u"QPushButton {\n"
"    color: rgba(255,255,255,255);\n"
"    font-weight: 900;\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_group_6.setFlat(True)

        self.horizontalLayout_37.addWidget(self.bn_group_6)


        self.horizontalLayout_31.addWidget(self.frame_group_6)


        self.verticalLayout_91.addWidget(self.frame_measurement_menu)

        self.frame_measurement_details = QFrame(self.page_measurements)
        self.frame_measurement_details.setObjectName(u"frame_measurement_details")
        sizePolicy1.setHeightForWidth(self.frame_measurement_details.sizePolicy().hasHeightForWidth())
        self.frame_measurement_details.setSizePolicy(sizePolicy1)
        self.frame_measurement_details.setMinimumSize(QSize(720, 445))
        self.frame_measurement_details.setFrameShape(QFrame.NoFrame)
        self.frame_measurement_details.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_measurement_details)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.frame_measurement_view = QFrame(self.frame_measurement_details)
        self.frame_measurement_view.setObjectName(u"frame_measurement_view")
        self.frame_measurement_view.setMinimumSize(QSize(40, 445))
        self.frame_measurement_view.setMaximumSize(QSize(40, 16777215))
        self.frame_measurement_view.setStyleSheet(u"background:rgb(55,55,55);")
        self.frame_measurement_view.setFrameShape(QFrame.NoFrame)
        self.frame_measurement_view.setFrameShadow(QFrame.Plain)
        self.frame_measurement_view.setLineWidth(0)
        self.verticalLayout_19 = QVBoxLayout(self.frame_measurement_view)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_read_measurement = QFrame(self.frame_measurement_view)
        self.frame_read_measurement.setObjectName(u"frame_read_measurement")
        self.frame_read_measurement.setMinimumSize(QSize(40, 120))
        self.frame_read_measurement.setMaximumSize(QSize(40, 300))
        self.frame_read_measurement.setFrameShape(QFrame.NoFrame)
        self.frame_read_measurement.setFrameShadow(QFrame.Plain)
        self.frame_read_measurement.setLineWidth(1)
        self.verticalLayout_20 = QVBoxLayout(self.frame_read_measurement)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.bn_view_read_meas = QPushButton(self.frame_read_measurement)
        self.bn_view_read_meas.setObjectName(u"bn_view_read_meas")
        self.bn_view_read_meas.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.bn_view_read_meas.sizePolicy().hasHeightForWidth())
        self.bn_view_read_meas.setSizePolicy(sizePolicy2)
        self.bn_view_read_meas.setMinimumSize(QSize(40, 30))
        self.bn_view_read_meas.setMaximumSize(QSize(40, 300))
        self.bn_view_read_meas.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u"icons/1x/settAsset 50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_view_read_meas.setIcon(icon12)
        self.bn_view_read_meas.setFlat(True)

        self.verticalLayout_20.addWidget(self.bn_view_read_meas)


        self.verticalLayout_19.addWidget(self.frame_read_measurement)

        self.frame_view_measurement = QFrame(self.frame_measurement_view)
        self.frame_view_measurement.setObjectName(u"frame_view_measurement")
        self.frame_view_measurement.setMaximumSize(QSize(40, 300))
        self.frame_view_measurement.setFrameShape(QFrame.NoFrame)
        self.frame_view_measurement.setFrameShadow(QFrame.Plain)
        self.verticalLayout_21 = QVBoxLayout(self.frame_view_measurement)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.bn_view_measurement = QPushButton(self.frame_view_measurement)
        self.bn_view_measurement.setObjectName(u"bn_view_measurement")
        self.bn_view_measurement.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.bn_view_measurement.sizePolicy().hasHeightForWidth())
        self.bn_view_measurement.setSizePolicy(sizePolicy2)
        self.bn_view_measurement.setMinimumSize(QSize(40, 30))
        self.bn_view_measurement.setMaximumSize(QSize(40, 300))
        self.bn_view_measurement.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u"icons/1x/listAsset.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_view_measurement.setIcon(icon13)
        self.bn_view_measurement.setIconSize(QSize(22, 22))
        self.bn_view_measurement.setFlat(True)

        self.verticalLayout_21.addWidget(self.bn_view_measurement)


        self.verticalLayout_19.addWidget(self.frame_view_measurement)

        self.frame_view_parameters = QFrame(self.frame_measurement_view)
        self.frame_view_parameters.setObjectName(u"frame_view_parameters")
        self.frame_view_parameters.setMinimumSize(QSize(30, 120))
        self.frame_view_parameters.setMaximumSize(QSize(40, 300))
        self.frame_view_parameters.setFrameShape(QFrame.NoFrame)
        self.frame_view_parameters.setFrameShadow(QFrame.Plain)
        self.verticalLayout_22 = QVBoxLayout(self.frame_view_parameters)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.bn_view_parameters = QPushButton(self.frame_view_parameters)
        self.bn_view_parameters.setObjectName(u"bn_view_parameters")
        self.bn_view_parameters.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.bn_view_parameters.sizePolicy().hasHeightForWidth())
        self.bn_view_parameters.setSizePolicy(sizePolicy2)
        self.bn_view_parameters.setMinimumSize(QSize(40, 30))
        self.bn_view_parameters.setMaximumSize(QSize(40, 300))
        self.bn_view_parameters.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_view_parameters.setIcon(icon4)
        self.bn_view_parameters.setIconSize(QSize(22, 22))
        self.bn_view_parameters.setFlat(True)

        self.verticalLayout_22.addWidget(self.bn_view_parameters)


        self.verticalLayout_19.addWidget(self.frame_view_parameters)

        self.frame_view_graph = QFrame(self.frame_measurement_view)
        self.frame_view_graph.setObjectName(u"frame_view_graph")
        self.frame_view_graph.setMaximumSize(QSize(40, 300))
        self.frame_view_graph.setFrameShape(QFrame.NoFrame)
        self.frame_view_graph.setFrameShadow(QFrame.Plain)
        self.frame_view_graph.setLineWidth(0)
        self.verticalLayout_23 = QVBoxLayout(self.frame_view_graph)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.bn_view_graph = QPushButton(self.frame_view_graph)
        self.bn_view_graph.setObjectName(u"bn_view_graph")
        self.bn_view_graph.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.bn_view_graph.sizePolicy().hasHeightForWidth())
        self.bn_view_graph.setSizePolicy(sizePolicy2)
        self.bn_view_graph.setMinimumSize(QSize(40, 30))
        self.bn_view_graph.setMaximumSize(QSize(40, 300))
        self.bn_view_graph.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u"icons/1x/graphAsset.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_view_graph.setIcon(icon14)
        self.bn_view_graph.setFlat(True)

        self.verticalLayout_23.addWidget(self.bn_view_graph)


        self.verticalLayout_19.addWidget(self.frame_view_graph)


        self.horizontalLayout_38.addWidget(self.frame_measurement_view)

        self.stackedWidget_measurements = QStackedWidget(self.frame_measurement_details)
        self.stackedWidget_measurements.setObjectName(u"stackedWidget_measurements")
        sizePolicy1.setHeightForWidth(self.stackedWidget_measurements.sizePolicy().hasHeightForWidth())
        self.stackedWidget_measurements.setSizePolicy(sizePolicy1)
        self.stackedWidget_measurements.setStyleSheet(u"")
        self.page_read_measurements = QWidget()
        self.page_read_measurements.setObjectName(u"page_read_measurements")
        self.verticalLayout_92 = QVBoxLayout(self.page_read_measurements)
        self.verticalLayout_92.setSpacing(0)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.frame_read_measurements = QFrame(self.page_read_measurements)
        self.frame_read_measurements.setObjectName(u"frame_read_measurements")
        self.frame_read_measurements.setMinimumSize(QSize(680, 445))
        self.frame_read_measurements.setMaximumSize(QSize(16777215, 16777215))
        self.frame_read_measurements.setFrameShape(QFrame.StyledPanel)
        self.frame_read_measurements.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_read_measurements)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_select_meas_folder = QFrame(self.frame_read_measurements)
        self.frame_select_meas_folder.setObjectName(u"frame_select_meas_folder")
        self.frame_select_meas_folder.setMinimumSize(QSize(680, 180))
        self.frame_select_meas_folder.setMaximumSize(QSize(16777215, 16777215))
        self.frame_select_meas_folder.setFrameShape(QFrame.StyledPanel)
        self.frame_select_meas_folder.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_select_meas_folder)
        self.verticalLayout_15.setSpacing(2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(2, 2, 2, 2)
        self.group_select_meas_fold = QGroupBox(self.frame_select_meas_folder)
        self.group_select_meas_fold.setObjectName(u"group_select_meas_fold")
        self.group_select_meas_fold.setMinimumSize(QSize(650, 180))
        self.group_select_meas_fold.setMaximumSize(QSize(16777215, 16777215))
        self.group_select_meas_fold.setFont(font8)
        self.group_select_meas_fold.setStyleSheet(u"QGroupBox{\n"
"	border:1px solid rgb(51,51,51);	\n"
"	border-radius:4px;\n"
"	color:white;\n"
"	background:rgb(91,90,90);\n"
"}\n"
"")
        self.group_select_meas_fold.setCheckable(False)
        self.verticalLayout_18 = QVBoxLayout(self.group_select_meas_fold)
        self.verticalLayout_18.setSpacing(5)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(5, 15, 5, 5)
        self.frame_7 = QFrame(self.group_select_meas_fold)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(680, 25))
        self.frame_7.setMaximumSize(QSize(16777215, 30))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.lab_meas_folder = QLabel(self.frame_7)
        self.lab_meas_folder.setObjectName(u"lab_meas_folder")
        self.lab_meas_folder.setMinimumSize(QSize(200, 20))
        self.lab_meas_folder.setMaximumSize(QSize(16777215, 30))
        self.lab_meas_folder.setFont(font7)
        self.lab_meas_folder.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_meas_folder.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_41.addWidget(self.lab_meas_folder)

        self.line_meas_folder = QLineEdit(self.frame_7)
        self.line_meas_folder.setObjectName(u"line_meas_folder")
        self.line_meas_folder.setEnabled(True)
        self.line_meas_folder.setMinimumSize(QSize(300, 25))
        self.line_meas_folder.setMaximumSize(QSize(500, 25))
        self.line_meas_folder.setFont(font6)
        self.line_meas_folder.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_41.addWidget(self.line_meas_folder)

        self.bn_meas_open_folder = QPushButton(self.frame_7)
        self.bn_meas_open_folder.setObjectName(u"bn_meas_open_folder")
        self.bn_meas_open_folder.setMinimumSize(QSize(140, 25))
        self.bn_meas_open_folder.setMaximumSize(QSize(140, 25))
        self.bn_meas_open_folder.setFont(font6)
        self.bn_meas_open_folder.setStyleSheet(u"QPushButton {\n"
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
        self.bn_meas_open_folder.setCheckable(False)
        self.bn_meas_open_folder.setFlat(True)

        self.horizontalLayout_41.addWidget(self.bn_meas_open_folder)

        self.horizontalSpacer_8 = QSpacerItem(22, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_8)


        self.verticalLayout_18.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.group_select_meas_fold)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(680, 25))
        self.frame_8.setMaximumSize(QSize(16777215, 30))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.lab_meas_grp_name = QLabel(self.frame_8)
        self.lab_meas_grp_name.setObjectName(u"lab_meas_grp_name")
        self.lab_meas_grp_name.setMinimumSize(QSize(200, 20))
        self.lab_meas_grp_name.setMaximumSize(QSize(16777215, 30))
        self.lab_meas_grp_name.setFont(font7)
        self.lab_meas_grp_name.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_meas_grp_name.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_42.addWidget(self.lab_meas_grp_name)

        self.line_meas_grp_name = QLineEdit(self.frame_8)
        self.line_meas_grp_name.setObjectName(u"line_meas_grp_name")
        self.line_meas_grp_name.setEnabled(True)
        self.line_meas_grp_name.setMinimumSize(QSize(300, 25))
        self.line_meas_grp_name.setMaximumSize(QSize(500, 25))
        self.line_meas_grp_name.setFont(font6)
        self.line_meas_grp_name.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_42.addWidget(self.line_meas_grp_name)

        self.bn_meas_grp_rename = QPushButton(self.frame_8)
        self.bn_meas_grp_rename.setObjectName(u"bn_meas_grp_rename")
        self.bn_meas_grp_rename.setMinimumSize(QSize(140, 25))
        self.bn_meas_grp_rename.setMaximumSize(QSize(140, 25))
        self.bn_meas_grp_rename.setFont(font6)
        self.bn_meas_grp_rename.setStyleSheet(u"QPushButton {\n"
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
        self.bn_meas_grp_rename.setCheckable(False)
        self.bn_meas_grp_rename.setFlat(True)

        self.horizontalLayout_42.addWidget(self.bn_meas_grp_rename)

        self.horizontalSpacer_9 = QSpacerItem(22, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_9)


        self.verticalLayout_18.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.group_select_meas_fold)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(680, 25))
        self.frame_9.setMaximumSize(QSize(16777215, 30))
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Plain)
        self.frame_9.setLineWidth(0)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.lab_hdr_file = QLabel(self.frame_9)
        self.lab_hdr_file.setObjectName(u"lab_hdr_file")
        self.lab_hdr_file.setMinimumSize(QSize(200, 20))
        self.lab_hdr_file.setMaximumSize(QSize(16777215, 30))
        self.lab_hdr_file.setFont(font7)
        self.lab_hdr_file.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_hdr_file.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_43.addWidget(self.lab_hdr_file)

        self.combo_header = QComboBox(self.frame_9)
        self.combo_header.setObjectName(u"combo_header")
        self.combo_header.setMinimumSize(QSize(300, 25))
        self.combo_header.setMaximumSize(QSize(500, 25))
        self.combo_header.setFont(font2)
        self.combo_header.setStyleSheet(u"QComboBox {\n"
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
        self.combo_header.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.combo_header.setFrame(False)
        self.combo_header.setModelColumn(0)

        self.horizontalLayout_43.addWidget(self.combo_header)

        self.bn_update_hdr_files = QPushButton(self.frame_9)
        self.bn_update_hdr_files.setObjectName(u"bn_update_hdr_files")
        self.bn_update_hdr_files.setMinimumSize(QSize(140, 25))
        self.bn_update_hdr_files.setMaximumSize(QSize(140, 25))
        self.bn_update_hdr_files.setFont(font6)
        self.bn_update_hdr_files.setStyleSheet(u"QPushButton {\n"
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
        self.bn_update_hdr_files.setCheckable(False)
        self.bn_update_hdr_files.setFlat(True)

        self.horizontalLayout_43.addWidget(self.bn_update_hdr_files)

        self.horizontalSpacer_12 = QSpacerItem(24, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_12)


        self.verticalLayout_18.addWidget(self.frame_9)

        self.frame_16 = QFrame(self.group_select_meas_fold)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(680, 25))
        self.frame_16.setMaximumSize(QSize(16777215, 30))
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Plain)
        self.frame_16.setLineWidth(0)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.lab_sfun_file = QLabel(self.frame_16)
        self.lab_sfun_file.setObjectName(u"lab_sfun_file")
        self.lab_sfun_file.setMinimumSize(QSize(200, 20))
        self.lab_sfun_file.setMaximumSize(QSize(16777215, 30))
        self.lab_sfun_file.setFont(font7)
        self.lab_sfun_file.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_sfun_file.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_50.addWidget(self.lab_sfun_file)

        self.combo_sfunction = QComboBox(self.frame_16)
        self.combo_sfunction.setObjectName(u"combo_sfunction")
        self.combo_sfunction.setMinimumSize(QSize(300, 25))
        self.combo_sfunction.setMaximumSize(QSize(500, 25))
        self.combo_sfunction.setFont(font2)
        self.combo_sfunction.setStyleSheet(u"QComboBox {\n"
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
        self.combo_sfunction.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.combo_sfunction.setFrame(False)
        self.combo_sfunction.setModelColumn(0)

        self.horizontalLayout_50.addWidget(self.combo_sfunction)

        self.bn_update_sfun_files = QPushButton(self.frame_16)
        self.bn_update_sfun_files.setObjectName(u"bn_update_sfun_files")
        self.bn_update_sfun_files.setMinimumSize(QSize(140, 25))
        self.bn_update_sfun_files.setMaximumSize(QSize(140, 25))
        self.bn_update_sfun_files.setFont(font6)
        self.bn_update_sfun_files.setStyleSheet(u"QPushButton {\n"
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
        self.bn_update_sfun_files.setCheckable(False)
        self.bn_update_sfun_files.setFlat(True)

        self.horizontalLayout_50.addWidget(self.bn_update_sfun_files)

        self.horizontalSpacer_17 = QSpacerItem(24, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_50.addItem(self.horizontalSpacer_17)


        self.verticalLayout_18.addWidget(self.frame_16)

        self.frame_10 = QFrame(self.group_select_meas_fold)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(680, 20))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_44.setSpacing(6)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.bn_read_meas = QPushButton(self.frame_10)
        self.bn_read_meas.setObjectName(u"bn_read_meas")
        self.bn_read_meas.setMinimumSize(QSize(100, 25))
        self.bn_read_meas.setMaximumSize(QSize(69, 25))
        self.bn_read_meas.setFont(font6)
        self.bn_read_meas.setStyleSheet(u"QPushButton {\n"
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
        self.bn_read_meas.setCheckable(False)
        self.bn_read_meas.setFlat(True)

        self.horizontalLayout_44.addWidget(self.bn_read_meas)

        self.progressBar_read_meas = QProgressBar(self.frame_10)
        self.progressBar_read_meas.setObjectName(u"progressBar_read_meas")
        self.progressBar_read_meas.setEnabled(True)
        self.progressBar_read_meas.setStyleSheet(u"QProgressBar\n"
"{\n"
"	color:rgb(255,255,255);\n"
"	background-color :rgb(51,51,51);\n"
"	border : 2px;\n"
"	border-radius:4px;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	border : 2px;\n"
"	border-radius:4px;\n"
"	background-color:rgb(0,143,170);\n"
"}")
        self.progressBar_read_meas.setValue(0)
        self.progressBar_read_meas.setAlignment(Qt.AlignCenter)
        self.progressBar_read_meas.setTextVisible(True)
        self.progressBar_read_meas.setOrientation(Qt.Horizontal)
        self.progressBar_read_meas.setInvertedAppearance(False)
        self.progressBar_read_meas.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout_44.addWidget(self.progressBar_read_meas)


        self.verticalLayout_18.addWidget(self.frame_10)


        self.verticalLayout_15.addWidget(self.group_select_meas_fold)


        self.verticalLayout_24.addWidget(self.frame_select_meas_folder)

        self.frame_select_param_file = QFrame(self.frame_read_measurements)
        self.frame_select_param_file.setObjectName(u"frame_select_param_file")
        self.frame_select_param_file.setMinimumSize(QSize(680, 90))
        self.frame_select_param_file.setMaximumSize(QSize(16777215, 16777215))
        self.frame_select_param_file.setFrameShape(QFrame.StyledPanel)
        self.frame_select_param_file.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_select_param_file)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.group_select_param_file = QGroupBox(self.frame_select_param_file)
        self.group_select_param_file.setObjectName(u"group_select_param_file")
        self.group_select_param_file.setMinimumSize(QSize(650, 90))
        self.group_select_param_file.setMaximumSize(QSize(16777215, 16777215))
        self.group_select_param_file.setFont(font8)
        self.group_select_param_file.setStyleSheet(u"QGroupBox{\n"
"	border:1px solid rgb(51,51,51);	\n"
"	border-radius:4px;\n"
"	color:white;\n"
"	background:rgb(91,90,90);\n"
"}\n"
"")
        self.group_select_param_file.setCheckable(False)
        self.verticalLayout_25 = QVBoxLayout(self.group_select_param_file)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(5, 15, 5, 5)
        self.frame_11 = QFrame(self.group_select_param_file)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 30))
        self.frame_11.setMaximumSize(QSize(16777215, 30))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.lab_par_file = QLabel(self.frame_11)
        self.lab_par_file.setObjectName(u"lab_par_file")
        self.lab_par_file.setMinimumSize(QSize(290, 20))
        self.lab_par_file.setMaximumSize(QSize(290, 30))
        self.lab_par_file.setFont(font7)
        self.lab_par_file.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_par_file.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_45.addWidget(self.lab_par_file)

        self.combo_parameter = QComboBox(self.frame_11)
        self.combo_parameter.setObjectName(u"combo_parameter")
        self.combo_parameter.setMinimumSize(QSize(220, 25))
        self.combo_parameter.setMaximumSize(QSize(500, 25))
        self.combo_parameter.setFont(font2)
        self.combo_parameter.setStyleSheet(u"QComboBox {\n"
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
        self.combo_parameter.setMaxVisibleItems(9)
        self.combo_parameter.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.combo_parameter.setFrame(False)
        self.combo_parameter.setModelColumn(0)

        self.horizontalLayout_45.addWidget(self.combo_parameter)

        self.bn_update_par_files = QPushButton(self.frame_11)
        self.bn_update_par_files.setObjectName(u"bn_update_par_files")
        self.bn_update_par_files.setMinimumSize(QSize(140, 25))
        self.bn_update_par_files.setMaximumSize(QSize(140, 25))
        self.bn_update_par_files.setFont(font6)
        self.bn_update_par_files.setStyleSheet(u"QPushButton {\n"
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
        self.bn_update_par_files.setCheckable(False)
        self.bn_update_par_files.setFlat(True)

        self.horizontalLayout_45.addWidget(self.bn_update_par_files)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_14)


        self.verticalLayout_25.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.group_select_param_file)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.bn_param_read = QPushButton(self.frame_12)
        self.bn_param_read.setObjectName(u"bn_param_read")
        self.bn_param_read.setGeometry(QRect(590, 0, 80, 25))
        self.bn_param_read.setMinimumSize(QSize(80, 25))
        self.bn_param_read.setMaximumSize(QSize(80, 25))
        self.bn_param_read.setFont(font6)
        self.bn_param_read.setStyleSheet(u"QPushButton {\n"
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
        self.bn_param_read.setCheckable(False)
        self.bn_param_read.setFlat(True)

        self.verticalLayout_25.addWidget(self.frame_12)


        self.verticalLayout_16.addWidget(self.group_select_param_file)


        self.verticalLayout_24.addWidget(self.frame_select_param_file)

        self.frame_select_graph_template = QFrame(self.frame_read_measurements)
        self.frame_select_graph_template.setObjectName(u"frame_select_graph_template")
        self.frame_select_graph_template.setMinimumSize(QSize(680, 90))
        self.frame_select_graph_template.setMaximumSize(QSize(16777215, 16777215))
        self.frame_select_graph_template.setFrameShape(QFrame.StyledPanel)
        self.frame_select_graph_template.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_select_graph_template)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.group_select_graph_template = QGroupBox(self.frame_select_graph_template)
        self.group_select_graph_template.setObjectName(u"group_select_graph_template")
        self.group_select_graph_template.setMinimumSize(QSize(650, 90))
        self.group_select_graph_template.setMaximumSize(QSize(16777215, 16777215))
        self.group_select_graph_template.setFont(font8)
        self.group_select_graph_template.setStyleSheet(u"QGroupBox{\n"
"	border:1px solid rgb(51,51,51);	\n"
"	border-radius:4px;\n"
"	color:white;\n"
"	background:rgb(91,90,90);\n"
"}\n"
"")
        self.group_select_graph_template.setCheckable(False)
        self.verticalLayout_26 = QVBoxLayout(self.group_select_graph_template)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(5, 15, 5, 5)
        self.frame_13 = QFrame(self.group_select_graph_template)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 30))
        self.frame_13.setMaximumSize(QSize(16777215, 50))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.lab_graph_format = QLabel(self.frame_13)
        self.lab_graph_format.setObjectName(u"lab_graph_format")
        self.lab_graph_format.setMinimumSize(QSize(230, 20))
        self.lab_graph_format.setMaximumSize(QSize(230, 30))
        self.lab_graph_format.setFont(font7)
        self.lab_graph_format.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_graph_format.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_46.addWidget(self.lab_graph_format)

        self.combo_graph = QComboBox(self.frame_13)
        self.combo_graph.setObjectName(u"combo_graph")
        self.combo_graph.setMinimumSize(QSize(280, 25))
        self.combo_graph.setMaximumSize(QSize(500, 25))
        self.combo_graph.setFont(font2)
        self.combo_graph.setStyleSheet(u"QComboBox {\n"
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
        self.combo_graph.setMaxVisibleItems(9)
        self.combo_graph.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.combo_graph.setFrame(False)
        self.combo_graph.setModelColumn(0)

        self.horizontalLayout_46.addWidget(self.combo_graph)

        self.bn_update_graph_files = QPushButton(self.frame_13)
        self.bn_update_graph_files.setObjectName(u"bn_update_graph_files")
        self.bn_update_graph_files.setMinimumSize(QSize(140, 25))
        self.bn_update_graph_files.setMaximumSize(QSize(140, 25))
        self.bn_update_graph_files.setFont(font6)
        self.bn_update_graph_files.setStyleSheet(u"QPushButton {\n"
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
        self.bn_update_graph_files.setCheckable(False)
        self.bn_update_graph_files.setFlat(True)

        self.horizontalLayout_46.addWidget(self.bn_update_graph_files)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_13)


        self.verticalLayout_26.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.group_select_graph_template)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 30))
        self.frame_14.setMaximumSize(QSize(16777215, 16777215))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.bn_graph_format = QPushButton(self.frame_14)
        self.bn_graph_format.setObjectName(u"bn_graph_format")
        self.bn_graph_format.setGeometry(QRect(590, 0, 80, 25))
        self.bn_graph_format.setMinimumSize(QSize(80, 25))
        self.bn_graph_format.setMaximumSize(QSize(80, 25))
        self.bn_graph_format.setFont(font6)
        self.bn_graph_format.setStyleSheet(u"QPushButton {\n"
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
        self.bn_graph_format.setCheckable(False)
        self.bn_graph_format.setFlat(True)

        self.verticalLayout_26.addWidget(self.frame_14)


        self.verticalLayout_17.addWidget(self.group_select_graph_template)


        self.verticalLayout_24.addWidget(self.frame_select_graph_template)

        self.frame_select_param_file.raise_()
        self.frame_select_graph_template.raise_()
        self.frame_select_meas_folder.raise_()

        self.verticalLayout_92.addWidget(self.frame_read_measurements)

        self.stackedWidget_measurements.addWidget(self.page_read_measurements)
        self.page_view_measurements = QWidget()
        self.page_view_measurements.setObjectName(u"page_view_measurements")
        self.page_view_measurements.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_93 = QVBoxLayout(self.page_view_measurements)
        self.verticalLayout_93.setSpacing(0)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.verticalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.frame_view_measurements = QFrame(self.page_view_measurements)
        self.frame_view_measurements.setObjectName(u"frame_view_measurements")
        self.frame_view_measurements.setMinimumSize(QSize(500, 1000))
        self.frame_view_measurements.setFrameShape(QFrame.NoFrame)
        self.frame_view_measurements.setFrameShadow(QFrame.Plain)
        self.frame_view_measurements.setLineWidth(0)
        self.verticalLayout_27 = QVBoxLayout(self.frame_view_measurements)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_view_meas_fun = QFrame(self.frame_view_measurements)
        self.frame_view_meas_fun.setObjectName(u"frame_view_meas_fun")
        self.frame_view_meas_fun.setMinimumSize(QSize(0, 40))
        self.frame_view_meas_fun.setMaximumSize(QSize(16777215, 40))
        self.frame_view_meas_fun.setFrameShape(QFrame.NoFrame)
        self.frame_view_meas_fun.setFrameShadow(QFrame.Plain)
        self.frame_view_meas_fun.setLineWidth(0)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_view_meas_fun)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.bn_meas_prev = QPushButton(self.frame_view_meas_fun)
        self.bn_meas_prev.setObjectName(u"bn_meas_prev")
        self.bn_meas_prev.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.bn_meas_prev.sizePolicy().hasHeightForWidth())
        self.bn_meas_prev.setSizePolicy(sizePolicy2)
        self.bn_meas_prev.setMinimumSize(QSize(120, 40))
        self.bn_meas_prev.setMaximumSize(QSize(240, 40))
        self.bn_meas_prev.setStyleSheet(u"QPushButton {\n"
"    color: rgba(255,255,255,255);\n"
"    font-weight: 900;\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(51,50,50);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u"icons/1x/prevAsset.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_meas_prev.setIcon(icon15)
        self.bn_meas_prev.setIconSize(QSize(28, 28))
        self.bn_meas_prev.setFlat(True)

        self.horizontalLayout_39.addWidget(self.bn_meas_prev)

        self.frame_4 = QFrame(self.frame_view_meas_fun)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(440, 40))
        self.frame_4.setMaximumSize(QSize(16777215, 40))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_10 = QSpacerItem(105, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_10)

        self.line_view_meas = QLineEdit(self.frame_4)
        self.line_view_meas.setObjectName(u"line_view_meas")
        self.line_view_meas.setEnabled(True)
        self.line_view_meas.setMinimumSize(QSize(100, 25))
        self.line_view_meas.setMaximumSize(QSize(150, 25))
        self.line_view_meas.setFont(font6)
        self.line_view_meas.setAutoFillBackground(False)
        self.line_view_meas.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_40.addWidget(self.line_view_meas)

        self.bn_show_meas = QPushButton(self.frame_4)
        self.bn_show_meas.setObjectName(u"bn_show_meas")
        self.bn_show_meas.setMinimumSize(QSize(80, 25))
        self.bn_show_meas.setMaximumSize(QSize(80, 25))
        self.bn_show_meas.setFont(font6)
        self.bn_show_meas.setStyleSheet(u"QPushButton {\n"
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
        self.bn_show_meas.setCheckable(False)
        self.bn_show_meas.setFlat(True)

        self.horizontalLayout_40.addWidget(self.bn_show_meas)

        self.horizontalSpacer_11 = QSpacerItem(104, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_11)


        self.horizontalLayout_39.addWidget(self.frame_4)

        self.bn_meas_next = QPushButton(self.frame_view_meas_fun)
        self.bn_meas_next.setObjectName(u"bn_meas_next")
        self.bn_meas_next.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.bn_meas_next.sizePolicy().hasHeightForWidth())
        self.bn_meas_next.setSizePolicy(sizePolicy2)
        self.bn_meas_next.setMinimumSize(QSize(120, 40))
        self.bn_meas_next.setMaximumSize(QSize(240, 40))
        self.bn_meas_next.setStyleSheet(u"QPushButton {\n"
"    color: rgba(255,255,255,255);\n"
"    font-weight: 900;\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(51,50,50);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u"icons/1x/nextAsset.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_meas_next.setIcon(icon16)
        self.bn_meas_next.setIconSize(QSize(28, 28))
        self.bn_meas_next.setFlat(True)

        self.horizontalLayout_39.addWidget(self.bn_meas_next)

        self.frame_4.raise_()
        self.bn_meas_next.raise_()
        self.bn_meas_prev.raise_()

        self.verticalLayout_27.addWidget(self.frame_view_meas_fun)

        self.frame_table_meas = QFrame(self.frame_view_measurements)
        self.frame_table_meas.setObjectName(u"frame_table_meas")
        self.frame_table_meas.setMinimumSize(QSize(680, 0))
        self.frame_table_meas.setFrameShape(QFrame.NoFrame)
        self.frame_table_meas.setFrameShadow(QFrame.Plain)
        self.frame_table_meas.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.frame_table_meas)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.table_meas = QTableWidget(self.frame_table_meas)
        self.table_meas.setObjectName(u"table_meas")
        self.table_meas.setMinimumSize(QSize(680, 400))
        self.table_meas.setStyleSheet(u"QLineEdit {border: none;\n"
" background-color: white; selection-color: white;color: black; font-weight:900;}\n"
"\n"
"QTableView::item:selected { color:white; background:rgb(80,180,180); font-weight:900; }\n"
"QTableView::item { color:white; font-weight:900; }\n"
"QTableCornerButton::section { background-color:rgb(80,80,80); }\n"
"QHeaderView::section { border:none; color:white; background-color:rgb(80,80,80);selection-color: white }\n"
"\n"
"QScrollBar:vertical {\n"
"	background:rgb(51,51,51);\n"
"    width:20px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background:rgb(0,143,170);\n"
"	height: 10px;\n"
"	width: 20px;\n"
"}\n"
"QScrollBar::add-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}\n"
"QScrollBar::sub-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}")
        self.table_meas.setFrameShape(QFrame.NoFrame)
        self.table_meas.setFrameShadow(QFrame.Plain)
        self.table_meas.setLineWidth(0)

        self.verticalLayout_4.addWidget(self.table_meas)


        self.verticalLayout_27.addWidget(self.frame_table_meas)


        self.verticalLayout_93.addWidget(self.frame_view_measurements)

        self.stackedWidget_measurements.addWidget(self.page_view_measurements)
        self.page_view_parameters = QWidget()
        self.page_view_parameters.setObjectName(u"page_view_parameters")
        self.verticalLayout_94 = QVBoxLayout(self.page_view_parameters)
        self.verticalLayout_94.setSpacing(0)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.verticalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.page_view_parameters)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setMinimumSize(QSize(680, 445))
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Plain)
        self.frame_6.setLineWidth(0)
        self.verticalLayout_14 = QVBoxLayout(self.frame_6)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.table_parameters = QTableWidget(self.frame_6)
        self.table_parameters.setObjectName(u"table_parameters")
        self.table_parameters.setStyleSheet(u"QLineEdit {border: none;\n"
" background-color: white; selection-color: white;color: black; font-weight:900;}\n"
"\n"
"QTableView::item:selected { color:white; background:rgb(80,180,180); font-weight:900; }\n"
"QTableView::item { color:white; font-weight:900; }\n"
"QTableCornerButton::section { background-color:rgb(80,80,80); }\n"
"QHeaderView::section { border:none; color:white; background-color:rgb(80,80,80);selection-color: white }\n"
"\n"
"")
        self.table_parameters.setFrameShape(QFrame.NoFrame)
        self.table_parameters.setFrameShadow(QFrame.Plain)
        self.table_parameters.setLineWidth(0)
        self.table_parameters.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_parameters.setTextElideMode(Qt.ElideMiddle)
        self.table_parameters.setSortingEnabled(True)

        self.verticalLayout_14.addWidget(self.table_parameters)


        self.verticalLayout_94.addWidget(self.frame_6)

        self.stackedWidget_measurements.addWidget(self.page_view_parameters)
        self.page_view_graphs = QWidget()
        self.page_view_graphs.setObjectName(u"page_view_graphs")
        self.verticalLayout_95 = QVBoxLayout(self.page_view_graphs)
        self.verticalLayout_95.setSpacing(0)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.verticalLayout_95.setContentsMargins(0, 0, 0, 0)
        self.frame_view_graph_fun = QFrame(self.page_view_graphs)
        self.frame_view_graph_fun.setObjectName(u"frame_view_graph_fun")
        self.frame_view_graph_fun.setMinimumSize(QSize(0, 40))
        self.frame_view_graph_fun.setMaximumSize(QSize(16777215, 40))
        self.frame_view_graph_fun.setFrameShape(QFrame.NoFrame)
        self.frame_view_graph_fun.setFrameShadow(QFrame.Plain)
        self.frame_view_graph_fun.setLineWidth(0)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_view_graph_fun)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.bn_graph_prev = QPushButton(self.frame_view_graph_fun)
        self.bn_graph_prev.setObjectName(u"bn_graph_prev")
        self.bn_graph_prev.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.bn_graph_prev.sizePolicy().hasHeightForWidth())
        self.bn_graph_prev.setSizePolicy(sizePolicy2)
        self.bn_graph_prev.setMinimumSize(QSize(120, 40))
        self.bn_graph_prev.setMaximumSize(QSize(240, 40))
        self.bn_graph_prev.setStyleSheet(u"QPushButton {\n"
"      color: rgba(255,255,255,255);\n"
"      font-weight: 900;\n"
"      border: none;\n"
"      background-color: rgba(0,0,0,0);\n"
"  }\n"
"  QPushButton:hover {\n"
"      background-color: rgb(51,50,50);\n"
"  }\n"
"  QPushButton:pressed {\n"
"      background-color: rgba(0,0,0,0);\n"
"  }")
        self.bn_graph_prev.setIcon(icon15)
        self.bn_graph_prev.setIconSize(QSize(28, 28))
        self.bn_graph_prev.setFlat(True)

        self.horizontalLayout_47.addWidget(self.bn_graph_prev)

        self.frame_15 = QFrame(self.frame_view_graph_fun)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(440, 40))
        self.frame_15.setMaximumSize(QSize(16777215, 40))
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_15 = QSpacerItem(105, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_48.addItem(self.horizontalSpacer_15)

        self.line_view_graph = QLineEdit(self.frame_15)
        self.line_view_graph.setObjectName(u"line_view_graph")
        self.line_view_graph.setEnabled(True)
        self.line_view_graph.setMinimumSize(QSize(100, 25))
        self.line_view_graph.setMaximumSize(QSize(150, 25))
        self.line_view_graph.setFont(font6)
        self.line_view_graph.setAutoFillBackground(False)
        self.line_view_graph.setStyleSheet(u"QLineEdit {\n"
"      color:rgb(255,255,255);\n"
"      border:2px solid rgb(51,51,51);\n"
"      border-radius:4px;\n"
"      background:rgb(51,51,51);\n"
"  }\n"
"\n"
"  QLineEdit:disabled {\n"
"      color:rgb(255,255,255);\n"
"      border:2px solid rgb(112,112,112);\n"
"      border-radius:4px;\n"
"      background:rgb(112,112,112);\n"
"  }")

        self.horizontalLayout_48.addWidget(self.line_view_graph)

        self.bn_show_graph = QPushButton(self.frame_15)
        self.bn_show_graph.setObjectName(u"bn_show_graph")
        self.bn_show_graph.setMinimumSize(QSize(80, 25))
        self.bn_show_graph.setMaximumSize(QSize(80, 25))
        self.bn_show_graph.setFont(font6)
        self.bn_show_graph.setStyleSheet(u"QPushButton {\n"
"      border: 2px solid rgb(51,51,51);\n"
"      border-radius: 5px;\n"
"      color:rgb(255,255,255);\n"
"      background-color: rgb(51,51,51);\n"
"  }\n"
"  QPushButton:hover {\n"
"      border: 2px solid rgb(0,143,150);\n"
"      background-color: rgb(0,143,150);\n"
"  }\n"
"  QPushButton:pressed {\n"
"      border: 2px solid rgb(0,143,150);\n"
"      background-color: rgb(51,51,51);\n"
"  }\n"
"\n"
"  QPushButton:disabled {\n"
"      border-radius: 5px;\n"
"      border: 2px solid rgb(112,112,112);\n"
"      background-color: rgb(112,112,112);\n"
"  }")
        self.bn_show_graph.setCheckable(False)
        self.bn_show_graph.setFlat(True)

        self.horizontalLayout_48.addWidget(self.bn_show_graph)

        self.horizontalSpacer_16 = QSpacerItem(104, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_48.addItem(self.horizontalSpacer_16)


        self.horizontalLayout_47.addWidget(self.frame_15)

        self.bn_graph_next = QPushButton(self.frame_view_graph_fun)
        self.bn_graph_next.setObjectName(u"bn_graph_next")
        self.bn_graph_next.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.bn_graph_next.sizePolicy().hasHeightForWidth())
        self.bn_graph_next.setSizePolicy(sizePolicy2)
        self.bn_graph_next.setMinimumSize(QSize(120, 40))
        self.bn_graph_next.setMaximumSize(QSize(240, 40))
        self.bn_graph_next.setStyleSheet(u"QPushButton {\n"
"      color: rgba(255,255,255,255);\n"
"      font-weight: 900;\n"
"      border: none;\n"
"      background-color: rgba(0,0,0,0);\n"
"  }\n"
"  QPushButton:hover {\n"
"      background-color: rgb(51,50,50);\n"
"  }\n"
"  QPushButton:pressed {\n"
"      background-color: rgba(0,0,0,0);\n"
"  }")
        self.bn_graph_next.setIcon(icon16)
        self.bn_graph_next.setIconSize(QSize(28, 28))
        self.bn_graph_next.setFlat(True)

        self.horizontalLayout_47.addWidget(self.bn_graph_next)


        self.verticalLayout_95.addWidget(self.frame_view_graph_fun)

        self.frame_view_graphs = QFrame(self.page_view_graphs)
        self.frame_view_graphs.setObjectName(u"frame_view_graphs")
        self.frame_view_graphs.setFrameShape(QFrame.StyledPanel)
        self.frame_view_graphs.setFrameShadow(QFrame.Raised)

        self.verticalLayout_95.addWidget(self.frame_view_graphs)

        self.stackedWidget_measurements.addWidget(self.page_view_graphs)

        self.horizontalLayout_38.addWidget(self.stackedWidget_measurements)


        self.verticalLayout_91.addWidget(self.frame_measurement_details)

        self.stackedWidget.addWidget(self.page_measurements)
        self.page_about_measurements = QWidget()
        self.page_about_measurements.setObjectName(u"page_about_measurements")
        self.stackedWidget.addWidget(self.page_about_measurements)
        self.page_graphs = QWidget()
        self.page_graphs.setObjectName(u"page_graphs")
        self.stackedWidget.addWidget(self.page_graphs)
        self.page_about_graphs = QWidget()
        self.page_about_graphs.setObjectName(u"page_about_graphs")
        self.stackedWidget.addWidget(self.page_about_graphs)
        self.page_functions = QWidget()
        self.page_functions.setObjectName(u"page_functions")
        self.verticalLayout_34 = QVBoxLayout(self.page_functions)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.frame_function = QFrame(self.page_functions)
        self.frame_function.setObjectName(u"frame_function")
        self.frame_function.setFrameShape(QFrame.NoFrame)
        self.frame_function.setFrameShadow(QFrame.Plain)
        self.frame_function.setLineWidth(0)
        self.verticalLayout_28 = QVBoxLayout(self.frame_function)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_function_type = QFrame(self.frame_function)
        self.frame_function_type.setObjectName(u"frame_function_type")
        self.frame_function_type.setMinimumSize(QSize(0, 40))
        self.frame_function_type.setMaximumSize(QSize(16777215, 40))
        self.frame_function_type.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_function_type.setFrameShape(QFrame.NoFrame)
        self.frame_function_type.setFrameShadow(QFrame.Plain)
        self.frame_function_type.setLineWidth(0)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_function_type)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_series_function = QFrame(self.frame_function_type)
        self.frame_series_function.setObjectName(u"frame_series_function")
        self.frame_series_function.setEnabled(True)
        self.frame_series_function.setMinimumSize(QSize(120, 30))
        self.frame_series_function.setFrameShape(QFrame.NoFrame)
        self.frame_series_function.setFrameShadow(QFrame.Plain)
        self.frame_series_function.setLineWidth(0)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_series_function)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.bn_series_function = QPushButton(self.frame_series_function)
        self.bn_series_function.setObjectName(u"bn_series_function")
        self.bn_series_function.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.bn_series_function.sizePolicy().hasHeightForWidth())
        self.bn_series_function.setSizePolicy(sizePolicy2)
        self.bn_series_function.setMinimumSize(QSize(120, 30))
        self.bn_series_function.setMaximumSize(QSize(16777215, 40))
        self.bn_series_function.setStyleSheet(u"QPushButton {\n"
"    color: rgba(255,255,255,255);\n"
"    font-weight: 900;\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_series_function.setIcon(icon14)
        self.bn_series_function.setIconSize(QSize(18, 18))
        self.bn_series_function.setFlat(True)

        self.horizontalLayout_52.addWidget(self.bn_series_function)


        self.horizontalLayout_16.addWidget(self.frame_series_function)

        self.frame_parameter_function = QFrame(self.frame_function_type)
        self.frame_parameter_function.setObjectName(u"frame_parameter_function")
        self.frame_parameter_function.setEnabled(True)
        self.frame_parameter_function.setMinimumSize(QSize(120, 30))
        self.frame_parameter_function.setFrameShape(QFrame.NoFrame)
        self.frame_parameter_function.setFrameShadow(QFrame.Plain)
        self.frame_parameter_function.setLineWidth(0)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_parameter_function)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.bn_parameter_function = QPushButton(self.frame_parameter_function)
        self.bn_parameter_function.setObjectName(u"bn_parameter_function")
        self.bn_parameter_function.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.bn_parameter_function.sizePolicy().hasHeightForWidth())
        self.bn_parameter_function.setSizePolicy(sizePolicy2)
        self.bn_parameter_function.setMinimumSize(QSize(120, 30))
        self.bn_parameter_function.setMaximumSize(QSize(16777215, 40))
        self.bn_parameter_function.setStyleSheet(u"QPushButton {\n"
"    color: rgba(255,255,255,255);\n"
"    font-weight: 900;\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_parameter_function.setIcon(icon13)
        self.bn_parameter_function.setIconSize(QSize(22, 22))
        self.bn_parameter_function.setFlat(True)

        self.horizontalLayout_53.addWidget(self.bn_parameter_function)


        self.horizontalLayout_16.addWidget(self.frame_parameter_function)


        self.verticalLayout_28.addWidget(self.frame_function_type)

        self.frame_function_details = QFrame(self.frame_function)
        self.frame_function_details.setObjectName(u"frame_function_details")
        self.frame_function_details.setFrameShape(QFrame.NoFrame)
        self.frame_function_details.setFrameShadow(QFrame.Plain)
        self.frame_function_details.setLineWidth(0)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_function_details)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_function_view = QFrame(self.frame_function_details)
        self.frame_function_view.setObjectName(u"frame_function_view")
        self.frame_function_view.setMinimumSize(QSize(40, 420))
        self.frame_function_view.setMaximumSize(QSize(40, 16777215))
        self.frame_function_view.setStyleSheet(u"background:rgb(55,55,55);")
        self.frame_function_view.setFrameShape(QFrame.NoFrame)
        self.frame_function_view.setFrameShadow(QFrame.Plain)
        self.frame_function_view.setLineWidth(0)
        self.verticalLayout_29 = QVBoxLayout(self.frame_function_view)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_function_sett_bn = QFrame(self.frame_function_view)
        self.frame_function_sett_bn.setObjectName(u"frame_function_sett_bn")
        self.frame_function_sett_bn.setMinimumSize(QSize(40, 120))
        self.frame_function_sett_bn.setMaximumSize(QSize(40, 300))
        self.frame_function_sett_bn.setFrameShape(QFrame.NoFrame)
        self.frame_function_sett_bn.setFrameShadow(QFrame.Plain)
        self.frame_function_sett_bn.setLineWidth(1)
        self.verticalLayout_30 = QVBoxLayout(self.frame_function_sett_bn)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.bn_function_sett = QPushButton(self.frame_function_sett_bn)
        self.bn_function_sett.setObjectName(u"bn_function_sett")
        self.bn_function_sett.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.bn_function_sett.sizePolicy().hasHeightForWidth())
        self.bn_function_sett.setSizePolicy(sizePolicy2)
        self.bn_function_sett.setMinimumSize(QSize(40, 30))
        self.bn_function_sett.setMaximumSize(QSize(40, 300))
        self.bn_function_sett.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_function_sett.setIcon(icon12)
        self.bn_function_sett.setFlat(True)

        self.verticalLayout_30.addWidget(self.bn_function_sett)


        self.verticalLayout_29.addWidget(self.frame_function_sett_bn)

        self.frame_function_define_bn = QFrame(self.frame_function_view)
        self.frame_function_define_bn.setObjectName(u"frame_function_define_bn")
        self.frame_function_define_bn.setMaximumSize(QSize(40, 300))
        self.frame_function_define_bn.setFrameShape(QFrame.NoFrame)
        self.frame_function_define_bn.setFrameShadow(QFrame.Plain)
        self.verticalLayout_31 = QVBoxLayout(self.frame_function_define_bn)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.bn_function_define = QPushButton(self.frame_function_define_bn)
        self.bn_function_define.setObjectName(u"bn_function_define")
        self.bn_function_define.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.bn_function_define.sizePolicy().hasHeightForWidth())
        self.bn_function_define.setSizePolicy(sizePolicy2)
        self.bn_function_define.setMinimumSize(QSize(40, 30))
        self.bn_function_define.setMaximumSize(QSize(40, 300))
        self.bn_function_define.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_function_define.setIcon(icon13)
        self.bn_function_define.setIconSize(QSize(22, 22))
        self.bn_function_define.setFlat(True)

        self.verticalLayout_31.addWidget(self.bn_function_define)


        self.verticalLayout_29.addWidget(self.frame_function_define_bn)


        self.horizontalLayout_15.addWidget(self.frame_function_view)

        self.stackedFunction_define = QStackedWidget(self.frame_function_details)
        self.stackedFunction_define.setObjectName(u"stackedFunction_define")
        self.page_function_sett = QWidget()
        self.page_function_sett.setObjectName(u"page_function_sett")
        self.verticalLayout_35 = QVBoxLayout(self.page_function_sett)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.frame_function_sett = QFrame(self.page_function_sett)
        self.frame_function_sett.setObjectName(u"frame_function_sett")
        self.frame_function_sett.setFrameShape(QFrame.StyledPanel)
        self.frame_function_sett.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_function_sett)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.sw_function_sett = QStackedWidget(self.frame_function_sett)
        self.sw_function_sett.setObjectName(u"sw_function_sett")
        self.page_series_function_sett = QWidget()
        self.page_series_function_sett.setObjectName(u"page_series_function_sett")
        self.verticalLayout_351 = QVBoxLayout(self.page_series_function_sett)
        self.verticalLayout_351.setSpacing(0)
        self.verticalLayout_351.setObjectName(u"verticalLayout_351")
        self.verticalLayout_351.setContentsMargins(0, 0, 0, 0)
        self.frame_series_function_sett = QFrame(self.page_series_function_sett)
        self.frame_series_function_sett.setObjectName(u"frame_series_function_sett")
        self.frame_series_function_sett.setFrameShape(QFrame.NoFrame)
        self.frame_series_function_sett.setFrameShadow(QFrame.Plain)
        self.frame_series_function_sett.setLineWidth(0)
        self.verticalLayout_45 = QVBoxLayout(self.frame_series_function_sett)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.frame_series_function_heading = QFrame(self.frame_series_function_sett)
        self.frame_series_function_heading.setObjectName(u"frame_series_function_heading")
        self.frame_series_function_heading.setMaximumSize(QSize(16777215, 70))
        self.frame_series_function_heading.setFrameShape(QFrame.NoFrame)
        self.frame_series_function_heading.setFrameShadow(QFrame.Plain)
        self.frame_series_function_heading.setLineWidth(0)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_series_function_heading)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.lab_series_function_heading = QLabel(self.frame_series_function_heading)
        self.lab_series_function_heading.setObjectName(u"lab_series_function_heading")
        self.lab_series_function_heading.setMaximumSize(QSize(500, 16777215))
        self.lab_series_function_heading.setFont(font)
        self.lab_series_function_heading.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_series_function_heading.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.lab_series_function_heading)

        self.horizontalSpacer_series_function_heading = QSpacerItem(395, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_series_function_heading)


        self.verticalLayout_45.addWidget(self.frame_series_function_heading)

        self.frame_series_function_name = QFrame(self.frame_series_function_sett)
        self.frame_series_function_name.setObjectName(u"frame_series_function_name")
        self.frame_series_function_name.setMaximumSize(QSize(16777215, 50))
        self.frame_series_function_name.setFrameShape(QFrame.NoFrame)
        self.frame_series_function_name.setFrameShadow(QFrame.Plain)
        self.frame_series_function_name.setLineWidth(0)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_series_function_name)
        self.horizontalLayout_18.setSpacing(5)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.lab_series_function_name = QLabel(self.frame_series_function_name)
        self.lab_series_function_name.setObjectName(u"lab_series_function_name")
        self.lab_series_function_name.setMinimumSize(QSize(200, 20))
        self.lab_series_function_name.setMaximumSize(QSize(16777215, 30))
        self.lab_series_function_name.setFont(font7)
        self.lab_series_function_name.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_series_function_name.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_18.addWidget(self.lab_series_function_name)

        self.line_series_function_name = QLineEdit(self.frame_series_function_name)
        self.line_series_function_name.setObjectName(u"line_series_function_name")
        self.line_series_function_name.setEnabled(True)
        self.line_series_function_name.setMinimumSize(QSize(300, 25))
        self.line_series_function_name.setMaximumSize(QSize(500, 25))
        self.line_series_function_name.setFont(font6)
        self.line_series_function_name.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_18.addWidget(self.line_series_function_name)

        self.bn_series_function_save = QPushButton(self.frame_series_function_name)
        self.bn_series_function_save.setObjectName(u"bn_series_function_save")
        self.bn_series_function_save.setMinimumSize(QSize(140, 25))
        self.bn_series_function_save.setMaximumSize(QSize(140, 25))
        self.bn_series_function_save.setFont(font6)
        self.bn_series_function_save.setStyleSheet(u"QPushButton {\n"
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
        self.bn_series_function_save.setCheckable(False)
        self.bn_series_function_save.setFlat(True)

        self.horizontalLayout_18.addWidget(self.bn_series_function_save)

        self.horizontalSpacer_18 = QSpacerItem(123, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_18)


        self.verticalLayout_45.addWidget(self.frame_series_function_name)

        self.frame_series_function_load = QFrame(self.frame_series_function_sett)
        self.frame_series_function_load.setObjectName(u"frame_series_function_load")
        self.frame_series_function_load.setMaximumSize(QSize(16777215, 50))
        self.frame_series_function_load.setFrameShape(QFrame.NoFrame)
        self.frame_series_function_load.setFrameShadow(QFrame.Plain)
        self.frame_series_function_load.setLineWidth(0)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_series_function_load)
        self.horizontalLayout_51.setSpacing(5)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.lab_series_function_load = QLabel(self.frame_series_function_load)
        self.lab_series_function_load.setObjectName(u"lab_series_function_load")
        self.lab_series_function_load.setMinimumSize(QSize(200, 20))
        self.lab_series_function_load.setMaximumSize(QSize(16777215, 30))
        self.lab_series_function_load.setFont(font7)
        self.lab_series_function_load.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_series_function_load.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_51.addWidget(self.lab_series_function_load)

        self.combo_series_function_load = QComboBox(self.frame_series_function_load)
        self.combo_series_function_load.setObjectName(u"combo_series_function_load")
        self.combo_series_function_load.setMinimumSize(QSize(300, 25))
        self.combo_series_function_load.setMaximumSize(QSize(500, 25))
        self.combo_series_function_load.setFont(font2)
        self.combo_series_function_load.setStyleSheet(u"QComboBox {\n"
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
        self.combo_series_function_load.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.combo_series_function_load.setFrame(False)
        self.combo_series_function_load.setModelColumn(0)

        self.horizontalLayout_51.addWidget(self.combo_series_function_load)

        self.bn_series_function_load = QPushButton(self.frame_series_function_load)
        self.bn_series_function_load.setObjectName(u"bn_series_function_load")
        self.bn_series_function_load.setMinimumSize(QSize(140, 25))
        self.bn_series_function_load.setMaximumSize(QSize(140, 25))
        self.bn_series_function_load.setFont(font6)
        self.bn_series_function_load.setStyleSheet(u"QPushButton {\n"
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
        self.bn_series_function_load.setCheckable(False)
        self.bn_series_function_load.setFlat(True)

        self.horizontalLayout_51.addWidget(self.bn_series_function_load)

        self.horizontalSpacer_19 = QSpacerItem(123, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_51.addItem(self.horizontalSpacer_19)


        self.verticalLayout_45.addWidget(self.frame_series_function_load)

        self.frame_series_function_blank = QFrame(self.frame_series_function_sett)
        self.frame_series_function_blank.setObjectName(u"frame_series_function_blank")
        self.frame_series_function_blank.setFrameShape(QFrame.StyledPanel)
        self.frame_series_function_blank.setFrameShadow(QFrame.Raised)

        self.verticalLayout_45.addWidget(self.frame_series_function_blank)


        self.verticalLayout_351.addWidget(self.frame_series_function_sett)

        self.sw_function_sett.addWidget(self.page_series_function_sett)
        self.page_parameter_function_sett = QWidget()
        self.page_parameter_function_sett.setObjectName(u"page_parameter_function_sett")
        self.verticalLayout_352 = QVBoxLayout(self.page_parameter_function_sett)
        self.verticalLayout_352.setSpacing(0)
        self.verticalLayout_352.setObjectName(u"verticalLayout_352")
        self.verticalLayout_352.setContentsMargins(0, 0, 0, 0)
        self.frame_parameter_function_sett = QFrame(self.page_parameter_function_sett)
        self.frame_parameter_function_sett.setObjectName(u"frame_parameter_function_sett")
        self.frame_parameter_function_sett.setFrameShape(QFrame.NoFrame)
        self.frame_parameter_function_sett.setFrameShadow(QFrame.Plain)
        self.frame_parameter_function_sett.setLineWidth(0)
        self.verticalLayout_53 = QVBoxLayout(self.frame_parameter_function_sett)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.frame_parameter_function_heading = QFrame(self.frame_parameter_function_sett)
        self.frame_parameter_function_heading.setObjectName(u"frame_parameter_function_heading")
        self.frame_parameter_function_heading.setMaximumSize(QSize(16777215, 70))
        self.frame_parameter_function_heading.setFrameShape(QFrame.NoFrame)
        self.frame_parameter_function_heading.setFrameShadow(QFrame.Plain)
        self.frame_parameter_function_heading.setLineWidth(0)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_parameter_function_heading)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.lab_parameter_function_heading = QLabel(self.frame_parameter_function_heading)
        self.lab_parameter_function_heading.setObjectName(u"lab_parameter_function_heading")
        self.lab_parameter_function_heading.setMaximumSize(QSize(500, 16777215))
        self.lab_parameter_function_heading.setFont(font)
        self.lab_parameter_function_heading.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_parameter_function_heading.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_57.addWidget(self.lab_parameter_function_heading)

        self.horizontalSpacer_parameter_function_heading = QSpacerItem(395, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_57.addItem(self.horizontalSpacer_parameter_function_heading)


        self.verticalLayout_53.addWidget(self.frame_parameter_function_heading)

        self.frame_parameter_function_name = QFrame(self.frame_parameter_function_sett)
        self.frame_parameter_function_name.setObjectName(u"frame_parameter_function_name")
        self.frame_parameter_function_name.setMaximumSize(QSize(16777215, 50))
        self.frame_parameter_function_name.setFrameShape(QFrame.NoFrame)
        self.frame_parameter_function_name.setFrameShadow(QFrame.Plain)
        self.frame_parameter_function_name.setLineWidth(0)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_parameter_function_name)
        self.horizontalLayout_58.setSpacing(5)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.lab_parameter_function_name = QLabel(self.frame_parameter_function_name)
        self.lab_parameter_function_name.setObjectName(u"lab_parameter_function_name")
        self.lab_parameter_function_name.setMinimumSize(QSize(200, 20))
        self.lab_parameter_function_name.setMaximumSize(QSize(16777215, 30))
        self.lab_parameter_function_name.setFont(font7)
        self.lab_parameter_function_name.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_parameter_function_name.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_58.addWidget(self.lab_parameter_function_name)

        self.line_parameter_function_name = QLineEdit(self.frame_parameter_function_name)
        self.line_parameter_function_name.setObjectName(u"line_parameter_function_name")
        self.line_parameter_function_name.setEnabled(True)
        self.line_parameter_function_name.setMinimumSize(QSize(300, 25))
        self.line_parameter_function_name.setMaximumSize(QSize(500, 25))
        self.line_parameter_function_name.setFont(font6)
        self.line_parameter_function_name.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_58.addWidget(self.line_parameter_function_name)

        self.bn_parameter_function_save = QPushButton(self.frame_parameter_function_name)
        self.bn_parameter_function_save.setObjectName(u"bn_parameter_function_save")
        self.bn_parameter_function_save.setMinimumSize(QSize(140, 25))
        self.bn_parameter_function_save.setMaximumSize(QSize(140, 25))
        self.bn_parameter_function_save.setFont(font6)
        self.bn_parameter_function_save.setStyleSheet(u"QPushButton {\n"
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
        self.bn_parameter_function_save.setCheckable(False)
        self.bn_parameter_function_save.setFlat(True)

        self.horizontalLayout_58.addWidget(self.bn_parameter_function_save)

        self.horizontalSpacer_22 = QSpacerItem(123, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_58.addItem(self.horizontalSpacer_22)


        self.verticalLayout_53.addWidget(self.frame_parameter_function_name)

        self.frame_parameter_function_load = QFrame(self.frame_parameter_function_sett)
        self.frame_parameter_function_load.setObjectName(u"frame_parameter_function_load")
        self.frame_parameter_function_load.setMaximumSize(QSize(16777215, 50))
        self.frame_parameter_function_load.setFrameShape(QFrame.NoFrame)
        self.frame_parameter_function_load.setFrameShadow(QFrame.Plain)
        self.frame_parameter_function_load.setLineWidth(0)
        self.horizontalLayout_59 = QHBoxLayout(self.frame_parameter_function_load)
        self.horizontalLayout_59.setSpacing(5)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.lab_parameter_function_load = QLabel(self.frame_parameter_function_load)
        self.lab_parameter_function_load.setObjectName(u"lab_parameter_function_load")
        self.lab_parameter_function_load.setMinimumSize(QSize(200, 20))
        self.lab_parameter_function_load.setMaximumSize(QSize(16777215, 30))
        self.lab_parameter_function_load.setFont(font7)
        self.lab_parameter_function_load.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_parameter_function_load.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_59.addWidget(self.lab_parameter_function_load)

        self.combo_parameter_function_load = QComboBox(self.frame_parameter_function_load)
        self.combo_parameter_function_load.setObjectName(u"combo_parameter_function_load")
        self.combo_parameter_function_load.setMinimumSize(QSize(300, 25))
        self.combo_parameter_function_load.setMaximumSize(QSize(500, 25))
        self.combo_parameter_function_load.setFont(font2)
        self.combo_parameter_function_load.setStyleSheet(u"QComboBox {\n"
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
        self.combo_parameter_function_load.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.combo_parameter_function_load.setFrame(False)
        self.combo_parameter_function_load.setModelColumn(0)

        self.horizontalLayout_59.addWidget(self.combo_parameter_function_load)

        self.bn_parameter_function_load = QPushButton(self.frame_parameter_function_load)
        self.bn_parameter_function_load.setObjectName(u"bn_parameter_function_load")
        self.bn_parameter_function_load.setMinimumSize(QSize(140, 25))
        self.bn_parameter_function_load.setMaximumSize(QSize(140, 25))
        self.bn_parameter_function_load.setFont(font6)
        self.bn_parameter_function_load.setStyleSheet(u"QPushButton {\n"
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
        self.bn_parameter_function_load.setCheckable(False)
        self.bn_parameter_function_load.setFlat(True)

        self.horizontalLayout_59.addWidget(self.bn_parameter_function_load)

        self.horizontalSpacer_23 = QSpacerItem(123, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_59.addItem(self.horizontalSpacer_23)


        self.verticalLayout_53.addWidget(self.frame_parameter_function_load)

        self.frame_parameter_function_blank = QFrame(self.frame_parameter_function_sett)
        self.frame_parameter_function_blank.setObjectName(u"frame_parameter_function_blank")
        self.frame_parameter_function_blank.setFrameShape(QFrame.StyledPanel)
        self.frame_parameter_function_blank.setFrameShadow(QFrame.Raised)

        self.verticalLayout_53.addWidget(self.frame_parameter_function_blank)


        self.verticalLayout_352.addWidget(self.frame_parameter_function_sett)

        self.sw_function_sett.addWidget(self.page_parameter_function_sett)

        self.verticalLayout_32.addWidget(self.sw_function_sett)


        self.verticalLayout_35.addWidget(self.frame_function_sett)

        self.stackedFunction_define.addWidget(self.page_function_sett)
        self.page_function_define3 = QWidget()
        self.page_function_define3.setObjectName(u"page_function_define3")
        self.verticalLayout_341 = QVBoxLayout(self.page_function_define3)
        self.verticalLayout_341.setSpacing(0)
        self.verticalLayout_341.setObjectName(u"verticalLayout_341")
        self.verticalLayout_341.setContentsMargins(0, 0, 0, 0)
        self.scrollA_function_define = QScrollArea(self.page_function_define3)
        self.scrollA_function_define.setObjectName(u"scrollA_function_define")
        self.scrollA_function_define.setStyleSheet(u"QScrollBar:vertical {\n"
"	background:rgb(51,51,51);\n"
"    width:20px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background:rgb(0,143,170);\n"
"	height: 10px;\n"
"	width: 20px;\n"
"}\n"
"QScrollBar::add-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}\n"
"QScrollBar::sub-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}")
        self.scrollA_function_define.setFrameShape(QFrame.NoFrame)
        self.scrollA_function_define.setFrameShadow(QFrame.Plain)
        self.scrollA_function_define.setLineWidth(0)
        self.scrollA_function_define.setWidgetResizable(True)
        self.scrollW_function_define = QWidget()
        self.scrollW_function_define.setObjectName(u"scrollW_function_define")
        self.scrollW_function_define.setGeometry(QRect(0, 0, 100, 30))
        self.verticalLayout_342 = QVBoxLayout(self.scrollW_function_define)
        self.verticalLayout_342.setSpacing(0)
        self.verticalLayout_342.setObjectName(u"verticalLayout_342")
        self.verticalLayout_342.setContentsMargins(0, 0, 0, 0)
        self.frame_function_define_add = QFrame(self.scrollW_function_define)
        self.frame_function_define_add.setObjectName(u"frame_function_define_add")
        self.frame_function_define_add.setFrameShape(QFrame.NoFrame)
        self.frame_function_define_add.setFrameShadow(QFrame.Plain)
        self.frame_function_define_add.setLineWidth(0)
        self.frame_function_item_blank = QFrame(self.frame_function_define_add)
        self.frame_function_item_blank.setObjectName(u"frame_function_item_blank")
        self.frame_function_item_blank.setGeometry(QRect(270, 230, 20, 20))
        self.frame_function_item_blank.setStyleSheet(u"QFrame {\n"
"	background:rgb(91,90,90);\n"
"}")
        self.frame_function_item_blank.setFrameShape(QFrame.StyledPanel)
        self.frame_function_item_blank.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_function_item_blank)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")

        self.verticalLayout_342.addWidget(self.frame_function_define_add)

        self.scrollA_function_define.setWidget(self.scrollW_function_define)

        self.verticalLayout_341.addWidget(self.scrollA_function_define)

        self.stackedFunction_define.addWidget(self.page_function_define3)
        self.page_function_define = QWidget()
        self.page_function_define.setObjectName(u"page_function_define")
        self.verticalLayout_343 = QVBoxLayout(self.page_function_define)
        self.verticalLayout_343.setSpacing(0)
        self.verticalLayout_343.setObjectName(u"verticalLayout_343")
        self.verticalLayout_343.setContentsMargins(0, 0, 0, 0)
        self.frame_function_define = QFrame(self.page_function_define)
        self.frame_function_define.setObjectName(u"frame_function_define")
        self.frame_function_define.setFrameShape(QFrame.NoFrame)
        self.frame_function_define.setFrameShadow(QFrame.Plain)
        self.frame_function_define.setLineWidth(0)
        self.verticalLayout_36 = QVBoxLayout(self.frame_function_define)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.sw_function_define = QStackedWidget(self.frame_function_define)
        self.sw_function_define.setObjectName(u"sw_function_define")
        self.page_series_function_define = QWidget()
        self.page_series_function_define.setObjectName(u"page_series_function_define")
        self.verticalLayout_344 = QVBoxLayout(self.page_series_function_define)
        self.verticalLayout_344.setSpacing(0)
        self.verticalLayout_344.setObjectName(u"verticalLayout_344")
        self.verticalLayout_344.setContentsMargins(0, 0, 0, 0)
        self.sa_series_function_define = QScrollArea(self.page_series_function_define)
        self.sa_series_function_define.setObjectName(u"sa_series_function_define")
        self.sa_series_function_define.setStyleSheet(u"QScrollBar:vertical {\n"
"	background:rgb(51,51,51);\n"
"    width:20px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background:rgb(0,143,170);\n"
"	height: 10px;\n"
"	width: 20px;\n"
"}\n"
"QScrollBar::add-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}\n"
"QScrollBar::sub-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}")
        self.sa_series_function_define.setFrameShape(QFrame.NoFrame)
        self.sa_series_function_define.setFrameShadow(QFrame.Plain)
        self.sa_series_function_define.setLineWidth(0)
        self.sa_series_function_define.setWidgetResizable(True)
        self.scrollW_series_function_define = QWidget()
        self.scrollW_series_function_define.setObjectName(u"scrollW_series_function_define")
        self.scrollW_series_function_define.setGeometry(QRect(0, 0, 100, 30))
        self.verticalLayout_37 = QVBoxLayout(self.scrollW_series_function_define)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.frame_series_function_define_add = QFrame(self.scrollW_series_function_define)
        self.frame_series_function_define_add.setObjectName(u"frame_series_function_define_add")
        self.frame_series_function_define_add.setFrameShape(QFrame.NoFrame)
        self.frame_series_function_define_add.setFrameShadow(QFrame.Plain)
        self.frame_series_function_define_add.setLineWidth(0)
        self.frame_series_function_item_blank = QFrame(self.frame_series_function_define_add)
        self.frame_series_function_item_blank.setObjectName(u"frame_series_function_item_blank")
        self.frame_series_function_item_blank.setGeometry(QRect(270, 230, 20, 20))
        self.frame_series_function_item_blank.setStyleSheet(u"QFrame {\n"
"	background:rgb(91,90,90);\n"
"}")
        self.frame_series_function_item_blank.setFrameShape(QFrame.StyledPanel)
        self.frame_series_function_item_blank.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_series_function_item_blank)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")

        self.verticalLayout_37.addWidget(self.frame_series_function_define_add)

        self.sa_series_function_define.setWidget(self.scrollW_series_function_define)

        self.verticalLayout_344.addWidget(self.sa_series_function_define)

        self.sw_function_define.addWidget(self.page_series_function_define)
        self.page_parameter_function_define = QWidget()
        self.page_parameter_function_define.setObjectName(u"page_parameter_function_define")
        self.verticalLayout_345 = QVBoxLayout(self.page_parameter_function_define)
        self.verticalLayout_345.setSpacing(0)
        self.verticalLayout_345.setObjectName(u"verticalLayout_345")
        self.verticalLayout_345.setContentsMargins(0, 0, 0, 0)
        self.sa_parameter_function_define = QScrollArea(self.page_parameter_function_define)
        self.sa_parameter_function_define.setObjectName(u"sa_parameter_function_define")
        self.sa_parameter_function_define.setStyleSheet(u"QScrollBar:vertical {\n"
"	background:rgb(51,51,51);\n"
"    width:20px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background:rgb(0,143,170);\n"
"	height: 10px;\n"
"	width: 20px;\n"
"}\n"
"QScrollBar::add-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}\n"
"QScrollBar::sub-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}")
        self.sa_parameter_function_define.setFrameShape(QFrame.NoFrame)
        self.sa_parameter_function_define.setFrameShadow(QFrame.Plain)
        self.sa_parameter_function_define.setLineWidth(0)
        self.sa_parameter_function_define.setWidgetResizable(True)
        self.scrollW_parameter_function_define = QWidget()
        self.scrollW_parameter_function_define.setObjectName(u"scrollW_parameter_function_define")
        self.scrollW_parameter_function_define.setGeometry(QRect(0, 0, 100, 30))
        self.verticalLayout_43 = QVBoxLayout(self.scrollW_parameter_function_define)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.frame_parameter_function_define_add = QFrame(self.scrollW_parameter_function_define)
        self.frame_parameter_function_define_add.setObjectName(u"frame_parameter_function_define_add")
        self.frame_parameter_function_define_add.setFrameShape(QFrame.NoFrame)
        self.frame_parameter_function_define_add.setFrameShadow(QFrame.Plain)
        self.frame_parameter_function_define_add.setLineWidth(0)
        self.frame_parameter_function_item_blank = QFrame(self.frame_parameter_function_define_add)
        self.frame_parameter_function_item_blank.setObjectName(u"frame_parameter_function_item_blank")
        self.frame_parameter_function_item_blank.setGeometry(QRect(270, 230, 20, 20))
        self.frame_parameter_function_item_blank.setStyleSheet(u"QFrame {\n"
"	background:rgb(91,90,90);\n"
"}")
        self.frame_parameter_function_item_blank.setFrameShape(QFrame.StyledPanel)
        self.frame_parameter_function_item_blank.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_parameter_function_item_blank)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")

        self.verticalLayout_43.addWidget(self.frame_parameter_function_define_add)

        self.sa_parameter_function_define.setWidget(self.scrollW_parameter_function_define)

        self.verticalLayout_345.addWidget(self.sa_parameter_function_define)

        self.sw_function_define.addWidget(self.page_parameter_function_define)

        self.verticalLayout_36.addWidget(self.sw_function_define)


        self.verticalLayout_343.addWidget(self.frame_function_define)

        self.stackedFunction_define.addWidget(self.page_function_define)

        self.horizontalLayout_15.addWidget(self.stackedFunction_define)


        self.verticalLayout_28.addWidget(self.frame_function_details)


        self.verticalLayout_34.addWidget(self.frame_function)

        self.stackedWidget.addWidget(self.page_functions)
        self.page_about_functions = QWidget()
        self.page_about_functions.setObjectName(u"page_about_functions")
        self.stackedWidget.addWidget(self.page_about_functions)
        self.page_report = QWidget()
        self.page_report.setObjectName(u"page_report")
        self.verticalLayout1 = QVBoxLayout(self.page_report)
        self.verticalLayout1.setSpacing(0)
        self.verticalLayout1.setObjectName(u"verticalLayout1")
        self.verticalLayout1.setContentsMargins(0, 0, 0, 0)
        self.frame_report = QFrame(self.page_report)
        self.frame_report.setObjectName(u"frame_report")
        self.frame_report.setFrameShape(QFrame.NoFrame)
        self.frame_report.setFrameShadow(QFrame.Plain)
        self.frame_report.setLineWidth(0)
        self.verticalLayout_39 = QVBoxLayout(self.frame_report)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.frame_report_type = QFrame(self.frame_report)
        self.frame_report_type.setObjectName(u"frame_report_type")
        self.frame_report_type.setMinimumSize(QSize(0, 40))
        self.frame_report_type.setMaximumSize(QSize(16777215, 40))
        self.frame_report_type.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_report_type.setFrameShape(QFrame.NoFrame)
        self.frame_report_type.setFrameShadow(QFrame.Plain)
        self.frame_report_type.setLineWidth(0)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_report_type)
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.frame_excel_report = QFrame(self.frame_report_type)
        self.frame_excel_report.setObjectName(u"frame_excel_report")
        self.frame_excel_report.setEnabled(True)
        self.frame_excel_report.setMinimumSize(QSize(120, 30))
        self.frame_excel_report.setFrameShape(QFrame.NoFrame)
        self.frame_excel_report.setFrameShadow(QFrame.Plain)
        self.frame_excel_report.setLineWidth(0)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_excel_report)
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.bn_excel_report = QPushButton(self.frame_excel_report)
        self.bn_excel_report.setObjectName(u"bn_excel_report")
        self.bn_excel_report.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.bn_excel_report.sizePolicy().hasHeightForWidth())
        self.bn_excel_report.setSizePolicy(sizePolicy2)
        self.bn_excel_report.setMinimumSize(QSize(120, 30))
        self.bn_excel_report.setMaximumSize(QSize(16777215, 40))
        self.bn_excel_report.setStyleSheet(u"QPushButton {\n"
"    color: rgba(255,255,255,255);\n"
"    font-weight: 900;\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_excel_report.setIcon(icon6)
        self.bn_excel_report.setIconSize(QSize(35, 35))
        self.bn_excel_report.setFlat(True)

        self.horizontalLayout_55.addWidget(self.bn_excel_report)


        self.horizontalLayout_54.addWidget(self.frame_excel_report)

        self.frame_word_report = QFrame(self.frame_report_type)
        self.frame_word_report.setObjectName(u"frame_word_report")
        self.frame_word_report.setEnabled(True)
        self.frame_word_report.setMinimumSize(QSize(120, 30))
        self.frame_word_report.setFrameShape(QFrame.NoFrame)
        self.frame_word_report.setFrameShadow(QFrame.Plain)
        self.frame_word_report.setLineWidth(0)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_word_report)
        self.horizontalLayout_56.setSpacing(0)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.bn_word_report = QPushButton(self.frame_word_report)
        self.bn_word_report.setObjectName(u"bn_word_report")
        self.bn_word_report.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.bn_word_report.sizePolicy().hasHeightForWidth())
        self.bn_word_report.setSizePolicy(sizePolicy2)
        self.bn_word_report.setMinimumSize(QSize(120, 30))
        self.bn_word_report.setMaximumSize(QSize(16777215, 40))
        self.bn_word_report.setStyleSheet(u"QPushButton {\n"
"    color: rgba(255,255,255,255);\n"
"    font-weight: 900;\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u"icons/1x/wordAsset.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_word_report.setIcon(icon17)
        self.bn_word_report.setIconSize(QSize(35, 35))
        self.bn_word_report.setFlat(True)

        self.horizontalLayout_56.addWidget(self.bn_word_report)


        self.horizontalLayout_54.addWidget(self.frame_word_report)


        self.verticalLayout_39.addWidget(self.frame_report_type)

        self.frame_report_details = QFrame(self.frame_report)
        self.frame_report_details.setObjectName(u"frame_report_details")
        self.frame_report_details.setFrameShape(QFrame.NoFrame)
        self.frame_report_details.setFrameShadow(QFrame.Plain)
        self.frame_report_details.setLineWidth(0)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_report_details)
        self.horizontalLayout_61.setSpacing(0)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.frame_report_view = QFrame(self.frame_report_details)
        self.frame_report_view.setObjectName(u"frame_report_view")
        self.frame_report_view.setMinimumSize(QSize(40, 420))
        self.frame_report_view.setMaximumSize(QSize(40, 16777215))
        self.frame_report_view.setStyleSheet(u"background:rgb(55,55,55);")
        self.frame_report_view.setFrameShape(QFrame.NoFrame)
        self.frame_report_view.setFrameShadow(QFrame.Plain)
        self.frame_report_view.setLineWidth(0)
        self.verticalLayout_54 = QVBoxLayout(self.frame_report_view)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.frame_report_pick_bn = QFrame(self.frame_report_view)
        self.frame_report_pick_bn.setObjectName(u"frame_report_pick_bn")
        self.frame_report_pick_bn.setMinimumSize(QSize(40, 120))
        self.frame_report_pick_bn.setMaximumSize(QSize(40, 300))
        self.frame_report_pick_bn.setFrameShape(QFrame.NoFrame)
        self.frame_report_pick_bn.setFrameShadow(QFrame.Plain)
        self.frame_report_pick_bn.setLineWidth(1)
        self.verticalLayout_55 = QVBoxLayout(self.frame_report_pick_bn)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.bn_report_pick = QPushButton(self.frame_report_pick_bn)
        self.bn_report_pick.setObjectName(u"bn_report_pick")
        self.bn_report_pick.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.bn_report_pick.sizePolicy().hasHeightForWidth())
        self.bn_report_pick.setSizePolicy(sizePolicy2)
        self.bn_report_pick.setMinimumSize(QSize(40, 30))
        self.bn_report_pick.setMaximumSize(QSize(40, 500))
        self.bn_report_pick.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon18 = QIcon()
        icon18.addFile(u"icons/1x/pickAsset.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_report_pick.setIcon(icon18)
        self.bn_report_pick.setFlat(True)

        self.verticalLayout_55.addWidget(self.bn_report_pick)


        self.verticalLayout_54.addWidget(self.frame_report_pick_bn)

        self.frame_report_sett_bn = QFrame(self.frame_report_view)
        self.frame_report_sett_bn.setObjectName(u"frame_report_sett_bn")
        self.frame_report_sett_bn.setMinimumSize(QSize(40, 120))
        self.frame_report_sett_bn.setMaximumSize(QSize(40, 300))
        self.frame_report_sett_bn.setFrameShape(QFrame.NoFrame)
        self.frame_report_sett_bn.setFrameShadow(QFrame.Plain)
        self.frame_report_sett_bn.setLineWidth(1)
        self.verticalLayout_74 = QVBoxLayout(self.frame_report_sett_bn)
        self.verticalLayout_74.setSpacing(0)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.bn_report_sett = QPushButton(self.frame_report_sett_bn)
        self.bn_report_sett.setObjectName(u"bn_report_sett")
        self.bn_report_sett.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.bn_report_sett.sizePolicy().hasHeightForWidth())
        self.bn_report_sett.setSizePolicy(sizePolicy2)
        self.bn_report_sett.setMinimumSize(QSize(40, 30))
        self.bn_report_sett.setMaximumSize(QSize(40, 500))
        self.bn_report_sett.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_report_sett.setIcon(icon12)
        self.bn_report_sett.setFlat(True)

        self.verticalLayout_74.addWidget(self.bn_report_sett)


        self.verticalLayout_54.addWidget(self.frame_report_sett_bn)

        self.frame_report_create_bn = QFrame(self.frame_report_view)
        self.frame_report_create_bn.setObjectName(u"frame_report_create_bn")
        self.frame_report_create_bn.setMaximumSize(QSize(40, 500))
        self.frame_report_create_bn.setFrameShape(QFrame.NoFrame)
        self.frame_report_create_bn.setFrameShadow(QFrame.Plain)
        self.frame_report_create_bn.setLineWidth(0)
        self.verticalLayout_56 = QVBoxLayout(self.frame_report_create_bn)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.bn_report_create = QPushButton(self.frame_report_create_bn)
        self.bn_report_create.setObjectName(u"bn_report_create")
        self.bn_report_create.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.bn_report_create.sizePolicy().hasHeightForWidth())
        self.bn_report_create.setSizePolicy(sizePolicy2)
        self.bn_report_create.setMinimumSize(QSize(40, 30))
        self.bn_report_create.setMaximumSize(QSize(40, 300))
        self.bn_report_create.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon19 = QIcon()
        icon19.addFile(u"icons/1x/penAsset.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_report_create.setIcon(icon19)
        self.bn_report_create.setIconSize(QSize(22, 22))
        self.bn_report_create.setFlat(True)

        self.verticalLayout_56.addWidget(self.bn_report_create)


        self.verticalLayout_54.addWidget(self.frame_report_create_bn)


        self.horizontalLayout_61.addWidget(self.frame_report_view)

        self.stackedReport_define = QStackedWidget(self.frame_report_details)
        self.stackedReport_define.setObjectName(u"stackedReport_define")
        self.page_report_pick = QWidget()
        self.page_report_pick.setObjectName(u"page_report_pick")
        self.verticalLayout_57 = QVBoxLayout(self.page_report_pick)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.frame_report_pick = QFrame(self.page_report_pick)
        self.frame_report_pick.setObjectName(u"frame_report_pick")
        self.frame_report_pick.setFrameShape(QFrame.StyledPanel)
        self.frame_report_pick.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.frame_report_pick)
        self.verticalLayout_58.setSpacing(0)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.sw_report_pick = QStackedWidget(self.frame_report_pick)
        self.sw_report_pick.setObjectName(u"sw_report_pick")
        self.page_excel_report_pick = QWidget()
        self.page_excel_report_pick.setObjectName(u"page_excel_report_pick")
        self.verticalLayout_59 = QVBoxLayout(self.page_excel_report_pick)
        self.verticalLayout_59.setSpacing(0)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.frame_excel_report_pick = QFrame(self.page_excel_report_pick)
        self.frame_excel_report_pick.setObjectName(u"frame_excel_report_pick")
        self.frame_excel_report_pick.setFrameShape(QFrame.NoFrame)
        self.frame_excel_report_pick.setFrameShadow(QFrame.Plain)
        self.frame_excel_report_pick.setLineWidth(0)
        self.verticalLayout_60 = QVBoxLayout(self.frame_excel_report_pick)
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.frame_excel_report_heading = QFrame(self.frame_excel_report_pick)
        self.frame_excel_report_heading.setObjectName(u"frame_excel_report_heading")
        self.frame_excel_report_heading.setMaximumSize(QSize(16777215, 70))
        self.frame_excel_report_heading.setFrameShape(QFrame.NoFrame)
        self.frame_excel_report_heading.setFrameShadow(QFrame.Plain)
        self.frame_excel_report_heading.setLineWidth(0)
        self.horizontalLayout_62 = QHBoxLayout(self.frame_excel_report_heading)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.lab_excel_report_heading = QLabel(self.frame_excel_report_heading)
        self.lab_excel_report_heading.setObjectName(u"lab_excel_report_heading")
        self.lab_excel_report_heading.setMaximumSize(QSize(500, 16777215))
        self.lab_excel_report_heading.setFont(font)
        self.lab_excel_report_heading.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_excel_report_heading.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_62.addWidget(self.lab_excel_report_heading)

        self.horizontalSpacer_excel_report_heading = QSpacerItem(395, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_62.addItem(self.horizontalSpacer_excel_report_heading)


        self.verticalLayout_60.addWidget(self.frame_excel_report_heading)

        self.frame_excel_report_name = QFrame(self.frame_excel_report_pick)
        self.frame_excel_report_name.setObjectName(u"frame_excel_report_name")
        self.frame_excel_report_name.setMaximumSize(QSize(16777215, 50))
        self.frame_excel_report_name.setFrameShape(QFrame.NoFrame)
        self.frame_excel_report_name.setFrameShadow(QFrame.Plain)
        self.frame_excel_report_name.setLineWidth(0)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_excel_report_name)
        self.horizontalLayout_63.setSpacing(5)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.lab_excel_report_name = QLabel(self.frame_excel_report_name)
        self.lab_excel_report_name.setObjectName(u"lab_excel_report_name")
        self.lab_excel_report_name.setMinimumSize(QSize(200, 20))
        self.lab_excel_report_name.setMaximumSize(QSize(16777215, 30))
        self.lab_excel_report_name.setFont(font7)
        self.lab_excel_report_name.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_excel_report_name.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_63.addWidget(self.lab_excel_report_name)

        self.line_excel_report_name = QLineEdit(self.frame_excel_report_name)
        self.line_excel_report_name.setObjectName(u"line_excel_report_name")
        self.line_excel_report_name.setEnabled(True)
        self.line_excel_report_name.setMinimumSize(QSize(300, 25))
        self.line_excel_report_name.setMaximumSize(QSize(500, 25))
        self.line_excel_report_name.setFont(font6)
        self.line_excel_report_name.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_63.addWidget(self.line_excel_report_name)

        self.bn_excel_report_save = QPushButton(self.frame_excel_report_name)
        self.bn_excel_report_save.setObjectName(u"bn_excel_report_save")
        self.bn_excel_report_save.setEnabled(False)
        self.bn_excel_report_save.setMinimumSize(QSize(140, 25))
        self.bn_excel_report_save.setMaximumSize(QSize(140, 25))
        self.bn_excel_report_save.setFont(font6)
        self.bn_excel_report_save.setStyleSheet(u"QPushButton {\n"
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
        self.bn_excel_report_save.setCheckable(False)
        self.bn_excel_report_save.setFlat(True)

        self.horizontalLayout_63.addWidget(self.bn_excel_report_save)

        self.horizontalSpacer_20 = QSpacerItem(123, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_63.addItem(self.horizontalSpacer_20)


        self.verticalLayout_60.addWidget(self.frame_excel_report_name)

        self.frame_excel_report_load = QFrame(self.frame_excel_report_pick)
        self.frame_excel_report_load.setObjectName(u"frame_excel_report_load")
        self.frame_excel_report_load.setMaximumSize(QSize(16777215, 50))
        self.frame_excel_report_load.setFrameShape(QFrame.NoFrame)
        self.frame_excel_report_load.setFrameShadow(QFrame.Plain)
        self.frame_excel_report_load.setLineWidth(0)
        self.horizontalLayout_64 = QHBoxLayout(self.frame_excel_report_load)
        self.horizontalLayout_64.setSpacing(5)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.lab_excel_report_load = QLabel(self.frame_excel_report_load)
        self.lab_excel_report_load.setObjectName(u"lab_excel_report_load")
        self.lab_excel_report_load.setMinimumSize(QSize(200, 20))
        self.lab_excel_report_load.setMaximumSize(QSize(16777215, 30))
        self.lab_excel_report_load.setFont(font7)
        self.lab_excel_report_load.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_excel_report_load.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_64.addWidget(self.lab_excel_report_load)

        self.combo_excel_report_load = QComboBox(self.frame_excel_report_load)
        self.combo_excel_report_load.setObjectName(u"combo_excel_report_load")
        self.combo_excel_report_load.setMinimumSize(QSize(300, 25))
        self.combo_excel_report_load.setMaximumSize(QSize(500, 25))
        self.combo_excel_report_load.setFont(font2)
        self.combo_excel_report_load.setStyleSheet(u"QComboBox {\n"
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
        self.combo_excel_report_load.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.combo_excel_report_load.setFrame(False)
        self.combo_excel_report_load.setModelColumn(0)

        self.horizontalLayout_64.addWidget(self.combo_excel_report_load)

        self.bn_excel_report_load = QPushButton(self.frame_excel_report_load)
        self.bn_excel_report_load.setObjectName(u"bn_excel_report_load")
        self.bn_excel_report_load.setMinimumSize(QSize(140, 25))
        self.bn_excel_report_load.setMaximumSize(QSize(140, 25))
        self.bn_excel_report_load.setFont(font6)
        self.bn_excel_report_load.setStyleSheet(u"QPushButton {\n"
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
        self.bn_excel_report_load.setCheckable(False)
        self.bn_excel_report_load.setFlat(True)

        self.horizontalLayout_64.addWidget(self.bn_excel_report_load)

        self.horizontalSpacer_21 = QSpacerItem(123, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_64.addItem(self.horizontalSpacer_21)


        self.verticalLayout_60.addWidget(self.frame_excel_report_load)

        self.frame_excel_report_blank = QFrame(self.frame_excel_report_pick)
        self.frame_excel_report_blank.setObjectName(u"frame_excel_report_blank")
        self.frame_excel_report_blank.setFrameShape(QFrame.StyledPanel)
        self.frame_excel_report_blank.setFrameShadow(QFrame.Raised)

        self.verticalLayout_60.addWidget(self.frame_excel_report_blank)


        self.verticalLayout_59.addWidget(self.frame_excel_report_pick)

        self.sw_report_pick.addWidget(self.page_excel_report_pick)
        self.page_word_report_pick = QWidget()
        self.page_word_report_pick.setObjectName(u"page_word_report_pick")
        self.verticalLayout_61 = QVBoxLayout(self.page_word_report_pick)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.frame_word_report_pick = QFrame(self.page_word_report_pick)
        self.frame_word_report_pick.setObjectName(u"frame_word_report_pick")
        self.frame_word_report_pick.setFrameShape(QFrame.NoFrame)
        self.frame_word_report_pick.setFrameShadow(QFrame.Plain)
        self.frame_word_report_pick.setLineWidth(0)
        self.verticalLayout_62 = QVBoxLayout(self.frame_word_report_pick)
        self.verticalLayout_62.setSpacing(0)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.frame_word_report_heading = QFrame(self.frame_word_report_pick)
        self.frame_word_report_heading.setObjectName(u"frame_word_report_heading")
        self.frame_word_report_heading.setMaximumSize(QSize(16777215, 70))
        self.frame_word_report_heading.setFrameShape(QFrame.NoFrame)
        self.frame_word_report_heading.setFrameShadow(QFrame.Plain)
        self.frame_word_report_heading.setLineWidth(0)
        self.horizontalLayout_65 = QHBoxLayout(self.frame_word_report_heading)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.lab_word_report_heading = QLabel(self.frame_word_report_heading)
        self.lab_word_report_heading.setObjectName(u"lab_word_report_heading")
        self.lab_word_report_heading.setMaximumSize(QSize(500, 16777215))
        self.lab_word_report_heading.setFont(font)
        self.lab_word_report_heading.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_word_report_heading.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_65.addWidget(self.lab_word_report_heading)

        self.horizontalSpacer_word_report_heading = QSpacerItem(395, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_65.addItem(self.horizontalSpacer_word_report_heading)


        self.verticalLayout_62.addWidget(self.frame_word_report_heading)

        self.frame_word_report_name = QFrame(self.frame_word_report_pick)
        self.frame_word_report_name.setObjectName(u"frame_word_report_name")
        self.frame_word_report_name.setMaximumSize(QSize(16777215, 50))
        self.frame_word_report_name.setFrameShape(QFrame.NoFrame)
        self.frame_word_report_name.setFrameShadow(QFrame.Plain)
        self.frame_word_report_name.setLineWidth(0)
        self.horizontalLayout_66 = QHBoxLayout(self.frame_word_report_name)
        self.horizontalLayout_66.setSpacing(5)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.lab_word_report_name = QLabel(self.frame_word_report_name)
        self.lab_word_report_name.setObjectName(u"lab_word_report_name")
        self.lab_word_report_name.setMinimumSize(QSize(200, 20))
        self.lab_word_report_name.setMaximumSize(QSize(16777215, 30))
        self.lab_word_report_name.setFont(font7)
        self.lab_word_report_name.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_word_report_name.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_66.addWidget(self.lab_word_report_name)

        self.line_word_report_name = QLineEdit(self.frame_word_report_name)
        self.line_word_report_name.setObjectName(u"line_word_report_name")
        self.line_word_report_name.setEnabled(True)
        self.line_word_report_name.setMinimumSize(QSize(300, 25))
        self.line_word_report_name.setMaximumSize(QSize(500, 25))
        self.line_word_report_name.setFont(font6)
        self.line_word_report_name.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_66.addWidget(self.line_word_report_name)

        self.bn_word_report_save = QPushButton(self.frame_word_report_name)
        self.bn_word_report_save.setObjectName(u"bn_word_report_save")
        self.bn_word_report_save.setEnabled(False)
        self.bn_word_report_save.setMinimumSize(QSize(140, 25))
        self.bn_word_report_save.setMaximumSize(QSize(140, 25))
        self.bn_word_report_save.setFont(font6)
        self.bn_word_report_save.setStyleSheet(u"QPushButton {\n"
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
        self.bn_word_report_save.setCheckable(False)
        self.bn_word_report_save.setFlat(True)

        self.horizontalLayout_66.addWidget(self.bn_word_report_save)

        self.horizontalSpacer_24 = QSpacerItem(123, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_66.addItem(self.horizontalSpacer_24)


        self.verticalLayout_62.addWidget(self.frame_word_report_name)

        self.frame_word_report_load = QFrame(self.frame_word_report_pick)
        self.frame_word_report_load.setObjectName(u"frame_word_report_load")
        self.frame_word_report_load.setMaximumSize(QSize(16777215, 50))
        self.frame_word_report_load.setFrameShape(QFrame.NoFrame)
        self.frame_word_report_load.setFrameShadow(QFrame.Plain)
        self.frame_word_report_load.setLineWidth(0)
        self.horizontalLayout_67 = QHBoxLayout(self.frame_word_report_load)
        self.horizontalLayout_67.setSpacing(5)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.lab_word_report_load = QLabel(self.frame_word_report_load)
        self.lab_word_report_load.setObjectName(u"lab_word_report_load")
        self.lab_word_report_load.setMinimumSize(QSize(200, 20))
        self.lab_word_report_load.setMaximumSize(QSize(16777215, 30))
        self.lab_word_report_load.setFont(font7)
        self.lab_word_report_load.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_word_report_load.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_67.addWidget(self.lab_word_report_load)

        self.combo_word_report_load = QComboBox(self.frame_word_report_load)
        self.combo_word_report_load.setObjectName(u"combo_word_report_load")
        self.combo_word_report_load.setMinimumSize(QSize(300, 25))
        self.combo_word_report_load.setMaximumSize(QSize(500, 25))
        self.combo_word_report_load.setFont(font2)
        self.combo_word_report_load.setStyleSheet(u"QComboBox {\n"
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
        self.combo_word_report_load.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.combo_word_report_load.setFrame(False)
        self.combo_word_report_load.setModelColumn(0)

        self.horizontalLayout_67.addWidget(self.combo_word_report_load)

        self.bn_word_report_load = QPushButton(self.frame_word_report_load)
        self.bn_word_report_load.setObjectName(u"bn_word_report_load")
        self.bn_word_report_load.setMinimumSize(QSize(140, 25))
        self.bn_word_report_load.setMaximumSize(QSize(140, 25))
        self.bn_word_report_load.setFont(font6)
        self.bn_word_report_load.setStyleSheet(u"QPushButton {\n"
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
        self.bn_word_report_load.setCheckable(False)
        self.bn_word_report_load.setFlat(True)

        self.horizontalLayout_67.addWidget(self.bn_word_report_load)

        self.horizontalSpacer_25 = QSpacerItem(123, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_67.addItem(self.horizontalSpacer_25)


        self.verticalLayout_62.addWidget(self.frame_word_report_load)

        self.frame_word_report_blank = QFrame(self.frame_word_report_pick)
        self.frame_word_report_blank.setObjectName(u"frame_word_report_blank")
        self.frame_word_report_blank.setFrameShape(QFrame.StyledPanel)
        self.frame_word_report_blank.setFrameShadow(QFrame.Raised)

        self.verticalLayout_62.addWidget(self.frame_word_report_blank)


        self.verticalLayout_61.addWidget(self.frame_word_report_pick)

        self.sw_report_pick.addWidget(self.page_word_report_pick)

        self.verticalLayout_58.addWidget(self.sw_report_pick)


        self.verticalLayout_57.addWidget(self.frame_report_pick)

        self.stackedReport_define.addWidget(self.page_report_pick)
        self.page_report_create = QWidget()
        self.page_report_create.setObjectName(u"page_report_create")
        self.verticalLayout_63 = QVBoxLayout(self.page_report_create)
        self.verticalLayout_63.setSpacing(0)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.frame_report_create = QFrame(self.page_report_create)
        self.frame_report_create.setObjectName(u"frame_report_create")
        self.frame_report_create.setFrameShape(QFrame.NoFrame)
        self.frame_report_create.setFrameShadow(QFrame.Plain)
        self.frame_report_create.setLineWidth(0)
        self.horizontalLayout_68 = QHBoxLayout(self.frame_report_create)
        self.horizontalLayout_68.setSpacing(0)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.sw_report_create = QStackedWidget(self.frame_report_create)
        self.sw_report_create.setObjectName(u"sw_report_create")
        self.page_excel_report_create = QWidget()
        self.page_excel_report_create.setObjectName(u"page_excel_report_create")
        self.verticalLayout_631 = QVBoxLayout(self.page_excel_report_create)
        self.verticalLayout_631.setSpacing(0)
        self.verticalLayout_631.setObjectName(u"verticalLayout_631")
        self.verticalLayout_631.setContentsMargins(0, 0, 0, 0)
        self.frame_excel_report_create = QFrame(self.page_excel_report_create)
        self.frame_excel_report_create.setObjectName(u"frame_excel_report_create")
        self.frame_excel_report_create.setFrameShape(QFrame.NoFrame)
        self.frame_excel_report_create.setFrameShadow(QFrame.Plain)
        self.frame_excel_report_create.setLineWidth(0)
        self.horizontalLayout_69 = QHBoxLayout(self.frame_excel_report_create)
        self.horizontalLayout_69.setSpacing(0)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.sa_excel_report_create = QScrollArea(self.frame_excel_report_create)
        self.sa_excel_report_create.setObjectName(u"sa_excel_report_create")
        self.sa_excel_report_create.setStyleSheet(u"QScrollBar:vertical {\n"
"	background:rgb(51,51,51);\n"
"    width:20px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background:rgb(0,143,170);\n"
"	height: 10px;\n"
"	width: 20px;\n"
"}\n"
"QScrollBar::add-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}\n"
"QScrollBar::sub-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}")
        self.sa_excel_report_create.setFrameShape(QFrame.NoFrame)
        self.sa_excel_report_create.setFrameShadow(QFrame.Plain)
        self.sa_excel_report_create.setLineWidth(0)
        self.sa_excel_report_create.setWidgetResizable(True)
        self.scrollW_excel_report_create = QWidget()
        self.scrollW_excel_report_create.setObjectName(u"scrollW_excel_report_create")
        self.scrollW_excel_report_create.setGeometry(QRect(0, 0, 783, 458))
        self.verticalLayout_75 = QVBoxLayout(self.scrollW_excel_report_create)
        self.verticalLayout_75.setSpacing(0)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.frame_excel_report_create_sa = QFrame(self.scrollW_excel_report_create)
        self.frame_excel_report_create_sa.setObjectName(u"frame_excel_report_create_sa")
        self.frame_excel_report_create_sa.setFrameShape(QFrame.NoFrame)
        self.frame_excel_report_create_sa.setFrameShadow(QFrame.Plain)
        self.frame_excel_report_create_sa.setLineWidth(0)
        self.frame_excel_report_create_item_create = QFrame(self.frame_excel_report_create_sa)
        self.frame_excel_report_create_item_create.setObjectName(u"frame_excel_report_create_item_create")
        self.frame_excel_report_create_item_create.setGeometry(QRect(240, 0, 432, 455))
        self.frame_excel_report_create_item_create.setMinimumSize(QSize(0, 50))
        self.frame_excel_report_create_item_create.setMaximumSize(QSize(16777215, 16777215))
        self.frame_excel_report_create_item_create.setStyleSheet(u"QFrame {\n"
"	background:rgb(91,90,90);\n"
"}")
        self.frame_excel_report_create_item_create.setFrameShape(QFrame.NoFrame)
        self.frame_excel_report_create_item_create.setFrameShadow(QFrame.Plain)
        self.frame_excel_report_create_item_create.setLineWidth(0)
        self.verticalLayout_excel_create = QVBoxLayout(self.frame_excel_report_create_item_create)
        self.verticalLayout_excel_create.setSpacing(0)
        self.verticalLayout_excel_create.setObjectName(u"verticalLayout_excel_create")
        self.verticalLayout_excel_create.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.frame_excel_report_create_item_create)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 50))
        self.frame_17.setMaximumSize(QSize(16777215, 50))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_70 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_70.setSpacing(10)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.bn_excel_report_create = QPushButton(self.frame_17)
        self.bn_excel_report_create.setObjectName(u"bn_excel_report_create")
        self.bn_excel_report_create.setMinimumSize(QSize(200, 25))
        self.bn_excel_report_create.setMaximumSize(QSize(200, 25))
        self.bn_excel_report_create.setFont(font6)
        self.bn_excel_report_create.setStyleSheet(u"QPushButton {\n"
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
        self.bn_excel_report_create.setCheckable(False)
        self.bn_excel_report_create.setFlat(True)

        self.horizontalLayout_70.addWidget(self.bn_excel_report_create)

        self.bn_excel_report_open = QPushButton(self.frame_17)
        self.bn_excel_report_open.setObjectName(u"bn_excel_report_open")
        self.bn_excel_report_open.setMinimumSize(QSize(250, 25))
        self.bn_excel_report_open.setMaximumSize(QSize(250, 25))
        self.bn_excel_report_open.setFont(font6)
        self.bn_excel_report_open.setStyleSheet(u"QPushButton {\n"
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
        self.bn_excel_report_open.setCheckable(False)
        self.bn_excel_report_open.setFlat(True)

        self.horizontalLayout_70.addWidget(self.bn_excel_report_open)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_70.addItem(self.horizontalSpacer_26)


        self.verticalLayout_excel_create.addWidget(self.frame_17)

        self.verticalSpacer_7 = QSpacerItem(20, 405, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_excel_create.addItem(self.verticalSpacer_7)


        self.verticalLayout_75.addWidget(self.frame_excel_report_create_sa)

        self.sa_excel_report_create.setWidget(self.scrollW_excel_report_create)

        self.horizontalLayout_69.addWidget(self.sa_excel_report_create)


        self.verticalLayout_631.addWidget(self.frame_excel_report_create)

        self.sw_report_create.addWidget(self.page_excel_report_create)
        self.page_word_report_create = QWidget()
        self.page_word_report_create.setObjectName(u"page_word_report_create")
        self.verticalLayout_632 = QVBoxLayout(self.page_word_report_create)
        self.verticalLayout_632.setSpacing(0)
        self.verticalLayout_632.setObjectName(u"verticalLayout_632")
        self.verticalLayout_632.setContentsMargins(0, 0, 0, 0)
        self.frame_word_report_create = QFrame(self.page_word_report_create)
        self.frame_word_report_create.setObjectName(u"frame_word_report_create")
        self.frame_word_report_create.setFrameShape(QFrame.NoFrame)
        self.frame_word_report_create.setFrameShadow(QFrame.Plain)
        self.frame_word_report_create.setLineWidth(0)
        self.horizontalLayout_89 = QHBoxLayout(self.frame_word_report_create)
        self.horizontalLayout_89.setSpacing(0)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.horizontalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.sa_word_report_create = QScrollArea(self.frame_word_report_create)
        self.sa_word_report_create.setObjectName(u"sa_word_report_create")
        self.sa_word_report_create.setStyleSheet(u"QScrollBar:vertical {\n"
"	background:rgb(51,51,51);\n"
"    width:20px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background:rgb(0,143,170);\n"
"	height: 10px;\n"
"	width: 20px;\n"
"}\n"
"QScrollBar::add-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}\n"
"QScrollBar::sub-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}")
        self.sa_word_report_create.setFrameShape(QFrame.NoFrame)
        self.sa_word_report_create.setFrameShadow(QFrame.Plain)
        self.sa_word_report_create.setLineWidth(0)
        self.sa_word_report_create.setWidgetResizable(True)
        self.scrollW_word_report_create = QWidget()
        self.scrollW_word_report_create.setObjectName(u"scrollW_word_report_create")
        self.scrollW_word_report_create.setGeometry(QRect(0, 0, 783, 458))
        self.verticalLayout_76 = QVBoxLayout(self.scrollW_word_report_create)
        self.verticalLayout_76.setSpacing(0)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.frame_word_report_create_sa = QFrame(self.scrollW_word_report_create)
        self.frame_word_report_create_sa.setObjectName(u"frame_word_report_create_sa")
        self.frame_word_report_create_sa.setFrameShape(QFrame.NoFrame)
        self.frame_word_report_create_sa.setFrameShadow(QFrame.Plain)
        self.frame_word_report_create_sa.setLineWidth(0)
        self.frame_word_report_create_item_create = QFrame(self.frame_word_report_create_sa)
        self.frame_word_report_create_item_create.setObjectName(u"frame_word_report_create_item_create")
        self.frame_word_report_create_item_create.setGeometry(QRect(0, 0, 472, 455))
        self.frame_word_report_create_item_create.setStyleSheet(u"QFrame {\n"
"	background:rgb(91,90,90);\n"
"}")
        self.frame_word_report_create_item_create.setFrameShape(QFrame.NoFrame)
        self.frame_word_report_create_item_create.setFrameShadow(QFrame.Plain)
        self.frame_word_report_create_item_create.setLineWidth(0)
        self.verticalLayout_78 = QVBoxLayout(self.frame_word_report_create_item_create)
        self.verticalLayout_78.setSpacing(0)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_word_report_create_item_create)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 50))
        self.frame_18.setMaximumSize(QSize(16777215, 50))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.bn_word_report_create = QPushButton(self.frame_18)
        self.bn_word_report_create.setObjectName(u"bn_word_report_create")
        self.bn_word_report_create.setMinimumSize(QSize(200, 25))
        self.bn_word_report_create.setMaximumSize(QSize(200, 25))
        self.bn_word_report_create.setFont(font6)
        self.bn_word_report_create.setStyleSheet(u"QPushButton {\n"
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
        self.bn_word_report_create.setCheckable(False)
        self.bn_word_report_create.setFlat(True)

        self.horizontalLayout_71.addWidget(self.bn_word_report_create)

        self.bn_word_report_open = QPushButton(self.frame_18)
        self.bn_word_report_open.setObjectName(u"bn_word_report_open")
        self.bn_word_report_open.setMinimumSize(QSize(250, 25))
        self.bn_word_report_open.setMaximumSize(QSize(250, 25))
        self.bn_word_report_open.setFont(font6)
        self.bn_word_report_open.setStyleSheet(u"QPushButton {\n"
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
        self.bn_word_report_open.setCheckable(False)
        self.bn_word_report_open.setFlat(True)

        self.horizontalLayout_71.addWidget(self.bn_word_report_open)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_71.addItem(self.horizontalSpacer_27)


        self.verticalLayout_78.addWidget(self.frame_18)

        self.verticalSpacer_8 = QSpacerItem(20, 405, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_78.addItem(self.verticalSpacer_8)


        self.verticalLayout_76.addWidget(self.frame_word_report_create_sa)

        self.sa_word_report_create.setWidget(self.scrollW_word_report_create)

        self.horizontalLayout_89.addWidget(self.sa_word_report_create)


        self.verticalLayout_632.addWidget(self.frame_word_report_create)

        self.sw_report_create.addWidget(self.page_word_report_create)

        self.horizontalLayout_68.addWidget(self.sw_report_create)


        self.verticalLayout_63.addWidget(self.frame_report_create)

        self.stackedReport_define.addWidget(self.page_report_create)
        self.page_report_define = QWidget()
        self.page_report_define.setObjectName(u"page_report_define")
        self.verticalLayout_66 = QVBoxLayout(self.page_report_define)
        self.verticalLayout_66.setSpacing(0)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.frame_report_define = QFrame(self.page_report_define)
        self.frame_report_define.setObjectName(u"frame_report_define")
        self.frame_report_define.setFrameShape(QFrame.NoFrame)
        self.frame_report_define.setFrameShadow(QFrame.Plain)
        self.frame_report_define.setLineWidth(0)
        self.verticalLayout_67 = QVBoxLayout(self.frame_report_define)
        self.verticalLayout_67.setSpacing(0)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.sw_report_define = QStackedWidget(self.frame_report_define)
        self.sw_report_define.setObjectName(u"sw_report_define")
        self.page_excel_report_define = QWidget()
        self.page_excel_report_define.setObjectName(u"page_excel_report_define")
        self.verticalLayout_68 = QVBoxLayout(self.page_excel_report_define)
        self.verticalLayout_68.setSpacing(0)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.sa_excel_report_define = QScrollArea(self.page_excel_report_define)
        self.sa_excel_report_define.setObjectName(u"sa_excel_report_define")
        self.sa_excel_report_define.setStyleSheet(u"QScrollBar:vertical {\n"
"	background:rgb(51,51,51);\n"
"    width:20px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background:rgb(0,143,170);\n"
"	height: 10px;\n"
"	width: 20px;\n"
"}\n"
"QScrollBar::add-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}\n"
"QScrollBar::sub-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}")
        self.sa_excel_report_define.setFrameShape(QFrame.NoFrame)
        self.sa_excel_report_define.setFrameShadow(QFrame.Plain)
        self.sa_excel_report_define.setLineWidth(0)
        self.sa_excel_report_define.setWidgetResizable(True)
        self.scrollW_excel_report_define = QWidget()
        self.scrollW_excel_report_define.setObjectName(u"scrollW_excel_report_define")
        self.scrollW_excel_report_define.setGeometry(QRect(0, 0, 100, 30))
        self.verticalLayout_69 = QVBoxLayout(self.scrollW_excel_report_define)
        self.verticalLayout_69.setSpacing(0)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.frame_report_define_add = QFrame(self.scrollW_excel_report_define)
        self.frame_report_define_add.setObjectName(u"frame_report_define_add")
        self.frame_report_define_add.setFrameShape(QFrame.NoFrame)
        self.frame_report_define_add.setFrameShadow(QFrame.Plain)
        self.frame_report_define_add.setLineWidth(0)
        self.frame_excel_report_define_item_blank = QFrame(self.frame_report_define_add)
        self.frame_excel_report_define_item_blank.setObjectName(u"frame_excel_report_define_item_blank")
        self.frame_excel_report_define_item_blank.setGeometry(QRect(270, 230, 20, 20))
        self.frame_excel_report_define_item_blank.setStyleSheet(u"QFrame {\n"
"	background:rgb(91,90,90);\n"
"}")
        self.frame_excel_report_define_item_blank.setFrameShape(QFrame.StyledPanel)
        self.frame_excel_report_define_item_blank.setFrameShadow(QFrame.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.frame_excel_report_define_item_blank)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.label_11 = QLabel(self.frame_report_define_add)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(260, 200, 81, 16))

        self.verticalLayout_69.addWidget(self.frame_report_define_add)

        self.sa_excel_report_define.setWidget(self.scrollW_excel_report_define)

        self.verticalLayout_68.addWidget(self.sa_excel_report_define)

        self.sw_report_define.addWidget(self.page_excel_report_define)
        self.page_word_report_define = QWidget()
        self.page_word_report_define.setObjectName(u"page_word_report_define")
        self.verticalLayout_71 = QVBoxLayout(self.page_word_report_define)
        self.verticalLayout_71.setSpacing(0)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.sa_word_report_define = QScrollArea(self.page_word_report_define)
        self.sa_word_report_define.setObjectName(u"sa_word_report_define")
        self.sa_word_report_define.setStyleSheet(u"QScrollBar:vertical {\n"
"	background:rgb(51,51,51);\n"
"    width:20px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background:rgb(0,143,170);\n"
"	height: 10px;\n"
"	width: 20px;\n"
"}\n"
"QScrollBar::add-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}\n"
"QScrollBar::sub-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}")
        self.sa_word_report_define.setFrameShape(QFrame.NoFrame)
        self.sa_word_report_define.setFrameShadow(QFrame.Plain)
        self.sa_word_report_define.setLineWidth(0)
        self.sa_word_report_define.setWidgetResizable(True)
        self.scrollW_word_report_define = QWidget()
        self.scrollW_word_report_define.setObjectName(u"scrollW_word_report_define")
        self.scrollW_word_report_define.setGeometry(QRect(0, 0, 100, 30))
        self.verticalLayout_72 = QVBoxLayout(self.scrollW_word_report_define)
        self.verticalLayout_72.setSpacing(0)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.frame_word_report_define_add = QFrame(self.scrollW_word_report_define)
        self.frame_word_report_define_add.setObjectName(u"frame_word_report_define_add")
        self.frame_word_report_define_add.setFrameShape(QFrame.NoFrame)
        self.frame_word_report_define_add.setFrameShadow(QFrame.Plain)
        self.frame_word_report_define_add.setLineWidth(0)
        self.frame_word_report_item_blank = QFrame(self.frame_word_report_define_add)
        self.frame_word_report_item_blank.setObjectName(u"frame_word_report_item_blank")
        self.frame_word_report_item_blank.setGeometry(QRect(270, 230, 20, 20))
        self.frame_word_report_item_blank.setStyleSheet(u"QFrame {\n"
"	background:rgb(91,90,90);\n"
"}")
        self.frame_word_report_item_blank.setFrameShape(QFrame.StyledPanel)
        self.frame_word_report_item_blank.setFrameShadow(QFrame.Raised)
        self.verticalLayout_73 = QVBoxLayout(self.frame_word_report_item_blank)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.label_12 = QLabel(self.frame_word_report_define_add)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(420, 200, 91, 16))

        self.verticalLayout_72.addWidget(self.frame_word_report_define_add)

        self.sa_word_report_define.setWidget(self.scrollW_word_report_define)

        self.verticalLayout_71.addWidget(self.sa_word_report_define)

        self.sw_report_define.addWidget(self.page_word_report_define)

        self.verticalLayout_67.addWidget(self.sw_report_define)


        self.verticalLayout_66.addWidget(self.frame_report_define)

        self.stackedReport_define.addWidget(self.page_report_define)

        self.horizontalLayout_61.addWidget(self.stackedReport_define)


        self.verticalLayout_39.addWidget(self.frame_report_details)


        self.verticalLayout1.addWidget(self.frame_report)

        self.stackedWidget.addWidget(self.page_report)
        self.page_about_report = QWidget()
        self.page_about_report.setObjectName(u"page_about_report")
        self.verticalLayout_346 = QVBoxLayout(self.page_about_report)
        self.verticalLayout_346.setSpacing(0)
        self.verticalLayout_346.setObjectName(u"verticalLayout_346")
        self.verticalLayout_346.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.page_about_report)

        self.horizontalLayout_14.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_low = QFrame(self.frame_bottom_east)
        self.frame_low.setObjectName(u"frame_low")
        self.frame_low.setMinimumSize(QSize(0, 20))
        self.frame_low.setMaximumSize(QSize(16777215, 20))
        self.frame_low.setStyleSheet(u"")
        self.frame_low.setFrameShape(QFrame.NoFrame)
        self.frame_low.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_low)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_tab = QFrame(self.frame_low)
        self.frame_tab.setObjectName(u"frame_tab")
        font10 = QFont()
        font10.setFamily(u"Segoe UI")
        self.frame_tab.setFont(font10)
        self.frame_tab.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_tab.setFrameShape(QFrame.NoFrame)
        self.frame_tab.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_tab)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.lab_tab = QLabel(self.frame_tab)
        self.lab_tab.setObjectName(u"lab_tab")
        font11 = QFont()
        font11.setFamily(u"Segoe UI Light")
        font11.setPointSize(10)
        self.lab_tab.setFont(font11)
        self.lab_tab.setStyleSheet(u"color:rgb(255,255,255);")

        self.horizontalLayout_12.addWidget(self.lab_tab)


        self.horizontalLayout_11.addWidget(self.frame_tab)

        self.frame_drag = QFrame(self.frame_low)
        self.frame_drag.setObjectName(u"frame_drag")
        self.frame_drag.setMinimumSize(QSize(20, 20))
        self.frame_drag.setMaximumSize(QSize(20, 20))
        self.frame_drag.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_drag.setFrameShape(QFrame.NoFrame)
        self.frame_drag.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_drag)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_11.addWidget(self.frame_drag)


        self.verticalLayout_2.addWidget(self.frame_low)


        self.horizontalLayout_2.addWidget(self.frame_bottom_east)


        self.verticalLayout.addWidget(self.frame_bottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.bn_measurements.setDefault(False)
        self.stackedWidget.setCurrentIndex(14)
        self.stackedWidget_android.setCurrentIndex(2)
        self.stackedWidget_measurements.setCurrentIndex(0)
        self.stackedFunction_define.setCurrentIndex(0)
        self.stackedReport_define.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toodle.setText("")
        self.lab_appname.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Data processor</span><br/></p></body></html>", None))
        self.lab_user.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">User8455</span></p></body></html>", None))
        self.lab_person.setText("")
#if QT_CONFIG(tooltip)
        self.bn_min.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.bn_min.setText("")
#if QT_CONFIG(tooltip)
        self.bn_max.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.bn_max.setText("")
#if QT_CONFIG(tooltip)
        self.bn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.bn_close.setText("")
        self.bn_measurements.setText("")
        self.bn_functions.setText("")
        self.bn_reports.setText("")
        self.lab_home_main_hed.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Profile</span></p></body></html>", None))
        self.lab_home_main_disc.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Name:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Age:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /"
                        "></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Adress:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Description: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; "
                        "margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Managememt :Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum i"
                        "ure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?</span></p></body></html>", None))
        self.lab_home_stat_hed.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Stat </span></p></body></html>", None))
        self.lab_home_stat_disc.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Weather: Rainy<br/>Skys: Cloudy<br/>Wind: blowing Fast<br/>Temperature: 32 Degree Celcious</span></p></body></html>", None))
        self.lab_about_home.setText(QCoreApplication.translate("MainWindow", u"About: Home", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Empty", None))
        self.lab_Bug.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Bugs Found</span></p></body></html>", None))
        self.lab_bug1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Vore/Lore</span></p></body></html>", None))
        self.bn_bug_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.lab_bullet3.setText("")
        self.lab_bullet2.setText("")
        self.lab_bug3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Sertilage</span></p></body></html>", None))
        self.lab_bullet.setText("")
        self.lab_bug2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Simple TO</span></p></body></html>", None))
        self.lab_bug_action.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Action: </span></p></body></html>", None))
        self.comboBox_bug.setItemText(0, QCoreApplication.translate("MainWindow", u"100000", None))
        self.comboBox_bug.setItemText(1, QCoreApplication.translate("MainWindow", u"1000000", None))
        self.comboBox_bug.setItemText(2, QCoreApplication.translate("MainWindow", u"10000000", None))
        self.comboBox_bug.setItemText(3, QCoreApplication.translate("MainWindow", u"100000000", None))

        self.lab_cloud_main.setText(QCoreApplication.translate("MainWindow", u"Cloud Connect", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Client ID :", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Server Adress :", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Proxy :", None))
        self.bn_cloud_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.bn_cloud_connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
#if QT_CONFIG(tooltip)
        self.bn_android_contact.setToolTip(QCoreApplication.translate("MainWindow", u"Contact", None))
#endif // QT_CONFIG(tooltip)
        self.bn_android_contact.setText("")
#if QT_CONFIG(tooltip)
        self.bn_android_game.setToolTip(QCoreApplication.translate("MainWindow", u"GamePad", None))
#endif // QT_CONFIG(tooltip)
        self.bn_android_game.setText("")
#if QT_CONFIG(tooltip)
        self.bn_android_clean.setToolTip(QCoreApplication.translate("MainWindow", u"Clean", None))
#endif // QT_CONFIG(tooltip)
        self.bn_android_clean.setText("")
#if QT_CONFIG(tooltip)
        self.bn_android_world.setToolTip(QCoreApplication.translate("MainWindow", u"World", None))
#endif // QT_CONFIG(tooltip)
        self.bn_android_world.setText("")
        self.lab_android_contact.setText(QCoreApplication.translate("MainWindow", u"Contact", None))
        self.lab_person_icon.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Ph:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Organisation:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Name: ", None))
        self.line_android_name.setText(QCoreApplication.translate("MainWindow", u"ALBERT EINSTEIN", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Adress: ", None))
        self.line_android_org.setText(QCoreApplication.translate("MainWindow", u"Physist", None))
        self.line_android_adress.setText(QCoreApplication.translate("MainWindow", u"112 Mercer Street", None))
        self.line_android_email.setText(QCoreApplication.translate("MainWindow", u"einstein@gmail.com", None))
        self.bn_android_contact_edit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.bn_android_contact_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.bn_android_contact_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.bn_android_contact_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.lab_gamepad.setText(QCoreApplication.translate("MainWindow", u"GamePad", None))
        self.groupBox_clean.setTitle(QCoreApplication.translate("MainWindow", u"Review", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Clean Password", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Clean History", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Clean Chache", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"Clean Bookmarks", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Did you liked the UI", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Did you like the Color Scheme", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Did you like Custome Buttons", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Did you like the Stacked Window", None))
        self.lab_clean.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Sliders", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"VACANT? TRY YOUR IMAGINATION", None))
        self.bn_group_1.setText(QCoreApplication.translate("MainWindow", u"Group 1", None))
        self.bn_group_2.setText("")
        self.bn_group_3.setText("")
        self.bn_group_4.setText("")
        self.bn_group_5.setText("")
        self.bn_group_6.setText("")
        self.bn_view_read_meas.setText("")
        self.bn_view_measurement.setText("")
        self.bn_view_parameters.setText("")
        self.bn_view_graph.setText("")
        self.group_select_meas_fold.setTitle(QCoreApplication.translate("MainWindow", u"Meritve", None))
        self.lab_meas_folder.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Izberi mapo z meritvami:</span></p></body></html>", None))
        self.line_meas_folder.setText("")
        self.bn_meas_open_folder.setText(QCoreApplication.translate("MainWindow", u"Prebrskaj", None))
        self.lab_meas_grp_name.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Ime skupine:</span></p></body></html>", None))
        self.line_meas_grp_name.setText(QCoreApplication.translate("MainWindow", u"Group 1", None))
        self.bn_meas_grp_rename.setText(QCoreApplication.translate("MainWindow", u"Spremeni", None))
        self.lab_hdr_file.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Izberi datoteko z glavami:</span></p></body></html>", None))
        self.bn_update_hdr_files.setText(QCoreApplication.translate("MainWindow", u"Posodobi seznam", None))
        self.lab_sfun_file.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Izberi datoteko s funkcijami:</span></p></body></html>", None))
        self.bn_update_sfun_files.setText(QCoreApplication.translate("MainWindow", u"Posodobi seznam", None))
        self.bn_read_meas.setText(QCoreApplication.translate("MainWindow", u"Beri", None))
        self.group_select_param_file.setTitle(QCoreApplication.translate("MainWindow", u"Parametri", None))
        self.lab_par_file.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Izberi datoteko za ustvarjanje parametrov:</span></p></body></html>", None))
        self.bn_update_par_files.setText(QCoreApplication.translate("MainWindow", u"Posodobi seznam", None))
        self.bn_param_read.setText(QCoreApplication.translate("MainWindow", u"Preberi", None))
        self.group_select_graph_template.setTitle(QCoreApplication.translate("MainWindow", u"Nastavitve grafov", None))
        self.lab_graph_format.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Izberi datoteko za obliko grafov:</span></p></body></html>", None))
        self.bn_update_graph_files.setText(QCoreApplication.translate("MainWindow", u"Posodobi seznam", None))
        self.bn_graph_format.setText(QCoreApplication.translate("MainWindow", u"Oblikuj", None))
        self.bn_meas_prev.setText("")
        self.line_view_meas.setText("")
        self.bn_show_meas.setText(QCoreApplication.translate("MainWindow", u"Prika\u017ei", None))
        self.bn_meas_next.setText("")
        self.bn_graph_prev.setText("")
        self.line_view_graph.setText("")
        self.bn_show_graph.setText(QCoreApplication.translate("MainWindow", u"Prika\u017ei", None))
        self.bn_graph_next.setText("")
        self.bn_series_function.setText("")
        self.bn_parameter_function.setText("")
        self.bn_function_sett.setText("")
        self.bn_function_define.setText("")
        self.lab_series_function_heading.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Nastavitve \u010dasovnih funkcij</span></p></body></html>", None))
        self.lab_series_function_name.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Ime datoteke s funkcijami:</span></p></body></html>", None))
        self.line_series_function_name.setText("")
        self.bn_series_function_save.setText(QCoreApplication.translate("MainWindow", u"Shrani", None))
        self.lab_series_function_load.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Izberi obstoje\u010do datoteko:</span></p></body></html>", None))
        self.bn_series_function_load.setText(QCoreApplication.translate("MainWindow", u"Nalo\u017ei", None))
        self.lab_parameter_function_heading.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Nastavitve parametri\u010dnih funkcij</span></p></body></html>", None))
        self.lab_parameter_function_name.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Ime datoteke s funkcijami:</span></p></body></html>", None))
        self.line_parameter_function_name.setText("")
        self.bn_parameter_function_save.setText(QCoreApplication.translate("MainWindow", u"Shrani", None))
        self.lab_parameter_function_load.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Izberi obstoje\u010do datoteko:</span></p></body></html>", None))
        self.bn_parameter_function_load.setText(QCoreApplication.translate("MainWindow", u"Nalo\u017ei", None))
        self.bn_excel_report.setText("")
        self.bn_word_report.setText("")
        self.bn_report_pick.setText("")
        self.bn_report_sett.setText("")
        self.bn_report_create.setText("")
        self.lab_excel_report_heading.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Izbira Excel poro\u010dil</span></p></body></html>", None))
        self.lab_excel_report_name.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Ime nastavitev poro\u010dila:</span></p></body></html>", None))
        self.line_excel_report_name.setText("")
        self.bn_excel_report_save.setText(QCoreApplication.translate("MainWindow", u"Shrani", None))
        self.lab_excel_report_load.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Izberi obstoje\u010do datoteko:</span></p></body></html>", None))
        self.bn_excel_report_load.setText(QCoreApplication.translate("MainWindow", u"Nalo\u017ei", None))
        self.lab_word_report_heading.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Izbira Word poro\u010dil</span></p></body></html>", None))
        self.lab_word_report_name.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Ime nastavitev poro\u010dila:</span></p></body></html>", None))
        self.line_word_report_name.setText("")
        self.bn_word_report_save.setText(QCoreApplication.translate("MainWindow", u"Shrani", None))
        self.lab_word_report_load.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Izberi obstoje\u010do datoteko:</span></p></body></html>", None))
        self.bn_word_report_load.setText(QCoreApplication.translate("MainWindow", u"Nalo\u017ei", None))
        self.bn_excel_report_create.setText(QCoreApplication.translate("MainWindow", u"Ustvari Excel poro\u010dilo", None))
        self.bn_excel_report_open.setText(QCoreApplication.translate("MainWindow", u"Odpri zadnje Excel poro\u010dilo", None))
        self.bn_word_report_create.setText(QCoreApplication.translate("MainWindow", u"Ustvari Word poro\u010dilo", None))
        self.bn_word_report_open.setText(QCoreApplication.translate("MainWindow", u"Odpri zadnje Word poro\u010dilo", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Exel define", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Word define", None))
        self.lab_tab.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.frame_drag.setToolTip(QCoreApplication.translate("MainWindow", u"Drag", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

