###########################################################################################
###                        CODE:       WRITTEN BY: ANJAL.P AUGUST 11 2020               ###
###                        PROJECT:    PELLIS Z1                                        ###
###                        PURPOSE:    WINDOWS/LINUX/MAC OS FLAT MODERN UI              ###
###                                    BASED ON QT DESIGNER, PySide2                    ###
###                        USE CASE:   TEMPLATE FOR SOFTWARES                           ###
###                        LICENCE:    MIT OPENSOURCE LICENCE                           ###
###                                                                                     ###
###                            CODE IS FREE TO USE AND MODIFY                           ###
###########################################################################################

###########################################################################################
#                                     DOCUMENTATION                                       #
#                                                                                         #
#                                                                                         #
#  Each line of the code described below is commented well, such as: the purpose of the   #
#  code, its function, returns e.t.c as in certain caes: the alternatives to that solul-  #
#  ution, other sources like included PDF document has also the working of the code.      #
#  CSS stylesheet of the buttons are given seperatly in the CSS.txt in the parent folder  #
###########################################################################################

###########################################################################################
#                                       CAUTION                                           #
#  SINCE MOST OF THE WORK IS DONE IN THE QT DESIGNER, YOU WAY NOT SEE THE STYLESHEET HERE #
#  FOR THAT PLEASE REFER THE CSS.txt FILE PROVIDED IN THIS SAME FILE.                     #
#  ALSO AMNY OF THE SETTINGS IS PREDEFINED IN THE QT DESIGNER ITSELF, SO HERE IN THIS FUN-#
#  CTION WHAY HAPPENS AFTER THIS I.E. WHEN THE USER CHANGES THE INPUT STATE, ONLY IS DELT #
#  HERE, SO IF YOU WANT TO MODIFY THE FILE, PLEASE OPEN THE CORRESPONDING .ui FILE IN QT  #
#  DESIGNER AND MADE THE MODIFICATION AND THENY COME BACK HERE TO ADD FUNCTIONALITY TO THE#
#  CHANGES.                                                                               #
########################################################################################### 


from main import * #IMPORTING THE MAIN.PY FILE

from about import *

from PySide2.QtGui import QColor, qRgb, QIcon
from PyQt5 import sip

from matplotlib.backends.qt_compat import QtCore, QtWidgets as QtWidgMat, is_pyqt5
from matplotlib.backends.backend_qt5agg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import matplotlib as mpl
from matplotlib.backend_tools import ToolBase
mpl.rcParams['toolbar'] = 'toolmanager'

mpl.rcParams['text.color'] = 'white'
mpl.rcParams['font.size'] = 12

from function_item import Ui_StackedWidget
from report_group_item import Ui_StackedWidget as rgi_StacketWidget
#from function_item import Ui_Frame
from DataProcessor.Data import DataGroup
from DataProcessor.Texts import Text
from DataProcessor.Graph import GraphWrapper
from DataProcessor import Basic
from DataProcessor import Interface
import Paths


#plt.tight_layout()


GLOBAL_STATE = 0 #NECESSERY FOR CHECKING WEATHER THE WINDWO IS FULL SCREEN OR NOT
GLOBAL_TITLE_BAR = True #NECESSERY FOR CHECKING WEATHER THE WINDWO IS FULL SCREEN OR NOT
init = False # NECRESSERY FOR INITITTION OF THE WINDOW.

# tab_Buttons = ['bn_home', 'bn_bug', 'bn_android', 'bn_cloud'] #BUTTONS IN MAIN TAB  
# android_buttons = ['bn_android_contact', 'bn_android_game', 'bn_android_clean', 'bn_android_world'] #BUTTONS IN ANDROID STACKPAGE

# THIS CLASS HOUSES ALL FUNCTION NECESSERY FOR OUR PROGRAMME TO RUN.
class UIFunction():#MainWindow):

    #----> INITIAL FUNCTION TO LOAD THE FRONT STACK WIDGET AND TAB BUTTON I.E. HOME PAGE 
    #INITIALISING THE WELCOME PAGE TO: HOME PAGE IN THE STACKEDWIDGET, SETTING THE BOTTOM LABEL AS THE PAGE NAME, SETTING THE BUTTON STYLE.
    def initStackTab(self):
        global init
        if init==False:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_measurements)
            self.ui.lab_tab.setText("Measurements")

            self.ui.frame_measurements.setStyleSheet("background:rgb(91,90,90)")
            init = True
    ################################################################################################


    #------> SETING THE APPLICATION NAME IN OUR CUSTOME MADE TAB, WHERE LABEL NAMED: lab_appname()
    def labelTitle(self, appName):
        self.ui.lab_appname.setText(appName)
    ################################################################################################


    #----> MAXIMISE/RESTORE FUNCTION
    #THIS FUNCTION MAXIMISES OUR MAINWINDOW WHEN THE MAXIMISE BUTTON IS PRESSED OR IF DOUBLE MOUSE LEFT PRESS IS DOEN OVER THE TOPFRMAE.
    #THIS MAKE THE APPLICATION TO OCCUPY THE WHOLE MONITOR.
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            self.ui.bn_max.setToolTip("Restore") 
            self.ui.bn_max.setIcon(QtGui.QIcon("icons/1x/restore.png")) #CHANGE THE MAXIMISE ICON TO RESTOR ICON
            self.ui.frame_drag.hide() #HIDE DRAG AS NOT NECESSERY
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.bn_max.setToolTip("Maximize")
            self.ui.bn_max.setIcon(QtGui.QIcon("icons/1x/max.png")) #CHANGE BACK TO MAXIMISE ICON
            self.ui.frame_drag.show()
    ################################################################################################


    #----> RETURN STATUS MAX OR RESTROE
    #NECESSERY OFR THE MAXIMISE FUNCTION TRO WORK.
    def returStatus():
        return GLOBAL_STATE


    def setStatus(status):
        global GLOBAL_STATE
        GLOBAL_STATE = status


    #------> TOODLE MENU FUNCTION
    #THIS FUNCTION TOODLES THE MENU BAR TO DOUBLE THE LENGTH OPENING A NEW ARE OF ABOUT TAB IN FRONT.
    #ASLO IT SETS THE ABOUT>HOME AS THE FIRST PAGE.
    #IF THE PAGE IS IN THE ABOUT PAGE THEN PRESSING AGAIN WILL RESULT IN UNDOING THE PROCESS AND COMMING BACK TO THE 
    #HOME PAGE.
    def toodleMenu(self, maxWidth, clicked):

        #------> THIS LINE CLEARS THE BG OF PREVIOUS TABS : I.E. MAKING THEN NORMAL COLOR THAN LIGHTER COLOR.
        for each in self.ui.frame_bottom_west.findChildren(QFrame): 
            each.setStyleSheet("background:rgb(51,51,51)")

        if clicked:
            currentWidth = self.ui.frame_bottom_west.width() #Reads the current width of the frame
            minWidth = 80 #MINIMUN WITDTH OF THE BOTTOM_WEST FRAME
            if currentWidth == 80:
                extend = maxWidth
                #----> MAKE THE STACKED WIDGET PAGE TO ABOUT HOME PAGE
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_measurements)
                self.ui.lab_tab.setText("About > Measurements")
                self.ui.frame_measurements.setStyleSheet("background:rgb(91,90,90)")
            else:
                extend = minWidth
                #-----> REVERT THE ABOUT HOME PAGE TO NORMAL HOME PAGE
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_measurements)
                self.ui.lab_tab.setText("Measurements")
                self.ui.frame_measurements.setStyleSheet("background:rgb(91,90,90)")
            #THIS ANIMATION IS RESPONSIBLE FOR THE TOODLE TO MOVE IN A SOME FIXED STATE.
            self.animation = QPropertyAnimation(self.ui.frame_bottom_west, b"minimumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(minWidth)
            self.animation.setEndValue(extend)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
    ################################################################################################


    #-----> DEFAULT ACTION FUNCTION
    def constantFunction(self):
        #-----> DOUBLE CLICK RESULT IN MAXIMISE OF WINDOW
        def maxDoubleClick(stateMouse):
            if stateMouse.type() == QtCore.QEvent.MouseButtonDblClick:
                QtCore.QTimer.singleShot(250, lambda: UIFunction.maximize_restore(self))

        #----> REMOVE NORMAL TITLE BAR 
        if True:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            self.ui.frame_appname.mouseDoubleClickEvent = maxDoubleClick
        else:
            self.ui.frame_close.hide()
            self.ui.frame_max.hide()
            self.ui.frame_min.hide()
            self.ui.frame_drag.hide()

        #-----> RESIZE USING DRAG                                       THIS CODE TO DRAG AND RESIZE IS IN PROTOPYPE.
        #self.sizegrip = QSizeGrip(self.ui.frame_drag)
        #self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        #SINCE THERE IS NO WINDOWS TOPBAR, THE CLOSE MIN, MAX BUTTON ARE ABSENT AND SO THERE IS A NEED FOR THE ALTERNATIVE BUTTONS IN OUR
        #DIALOG BOX, WHICH IS CARRIED OUT BY THE BELOW CODE
        #-----> MINIMIZE BUTTON FUNCTION 
        self.ui.bn_min.clicked.connect(lambda: self.showMinimized())

        #-----> MAXIMIZE/RESTORE BUTTON FUNCTION
        self.ui.bn_max.clicked.connect(lambda: UIFunction.maximize_restore(self))

        #-----> CLOSE APPLICATION FUNCTION BUTTON
        self.ui.bn_close.clicked.connect(lambda: self.close())
    ################################################################################################################


    #----> BUTTON IN TAB PRESSED EXECUTES THE CORRESPONDING PAGE IN STACKEDWIDGET PAGES
    def buttonPressed(self, buttonName):

        index = self.ui.stackedWidget.currentIndex()

        #------> THIS LINE CLEARS THE BG OF PREVIOUS TABS I.E. FROM THE LITER COLOR TO THE SAME BG COLOR I.E. TO CHANGE THE HIGHLIGHT.
        for each in self.ui.frame_bottom_west.findChildren(QFrame):
            each.setStyleSheet("background:rgb(51,51,51)")
        """
        if buttonName=='bn_home':
            if self.ui.frame_bottom_west.width()==80  and index!=0:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
                self.ui.lab_tab.setText("Home")
                self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST 

            elif self.ui.frame_bottom_west.width()==160  and index!=1:  # ABOUT PAGE STACKED WIDGET
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_home)
                self.ui.lab_tab.setText("About > Home")
                self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

        elif buttonName=='bn_bug':
            if self.ui.frame_bottom_west.width()==80 and index!=5:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_bug)
                self.ui.lab_tab.setText("Bug")
                self.ui.frame_bug.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

            elif self.ui.frame_bottom_west.width()==160 and index!=4:   # ABOUT PAGE STACKED WIDGET
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_bug)
                self.ui.lab_tab.setText("About > Bug")
                self.ui.frame_bug.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

        elif buttonName=='bn_android':
            if self.ui.frame_bottom_west.width()==80  and index!=7:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_android)
                self.ui.lab_tab.setText("Android")
                self.ui.frame_android.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST
                UIFunction.androidStackPages(self, "page_contact")

            elif self.ui.frame_bottom_west.width()==160  and index!=3:   # ABOUT PAGE STACKED WIDGET
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_android)
                self.ui.lab_tab.setText("About > Android")
                self.ui.frame_android.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

        elif buttonName=='bn_cloud':
            if self.ui.frame_bottom_west.width()==80 and index!=6:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_cloud)
                self.ui.lab_tab.setText("Cloud")
                self.ui.frame_cloud.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

            elif self.ui.frame_bottom_west.width()==160 and index!=2:   # ABOUT PAGE STACKED WIDGET
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_cloud)
                self.ui.lab_tab.setText("About > Cloud")
                self.ui.frame_cloud.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST
        """
        if buttonName == 'bn_measurements':
            if self.ui.frame_bottom_west.width() == 80 and index != 6:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_measurements)
                self.ui.lab_tab.setText("Measurements")
                self.ui.frame_measurements.setStyleSheet("background:rgb(80,180,180)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

            elif self.ui.frame_bottom_west.width() == 160 and index != 2:   # ABOUT PAGE STACKED WIDGET
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_measurements)
                self.ui.lab_tab.setText("About > Measurements")
                self.ui.frame_measurements.setStyleSheet("background:rgb(80,180,180)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

        elif buttonName == 'bn_functions':
            if self.ui.frame_bottom_west.width() == 80 and index != 6:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_functions)
                self.ui.lab_tab.setText("Functions")
                self.ui.frame_functions.setStyleSheet(
                    "background:rgb(80,180,180)")  # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

            elif self.ui.frame_bottom_west.width() == 160 and index != 2:  # ABOUT PAGE STACKED WIDGET
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_functions)
                self.ui.lab_tab.setText("About > Functions")
                self.ui.frame_functions.setStyleSheet(
                    "background:rgb(80,180,180)")  # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

        elif buttonName == 'bn_reports':
            if self.ui.frame_bottom_west.width() == 80 and index != 6:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_report)
                self.ui.lab_tab.setText("Reports")
                self.ui.frame_reports.setStyleSheet(
                    "background:rgb(80,180,180)")  # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

            elif self.ui.frame_bottom_west.width() == 160 and index != 2:  # ABOUT PAGE STACKED WIDGET
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_report)
                self.ui.lab_tab.setText("About > Reports")
                self.ui.frame_reports.setStyleSheet(
                    "background:rgb(80,180,180)")  # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

        #ADD ANOTHER ELIF STATEMENT HERE FOR EXECTUITING A NEW MENU BUTTON STACK PAGE.
    ########################################################################################################################


    #----> STACKWIDGET EACH PAGE FUNCTION PAGE FUNCTIONS
    # CODE TO PERFOMR THE TASK IN THE STACKED WIDGET PAGE 
    # WHAT EVER WIDGET IS IN THE STACKED PAGES ITS ACTION IS EVALUATED HERE AND THEN THE REST FUNCTION IS PASSED.
    def stackPage(self):

        """
        ######### PAGE_HOME ############# BELOW DISPLAYS THE FUNCTION OF WIDGET, LABEL, PROGRESS BAR, E.T.C IN STACKEDWIDGET page_HOME
        self.ui.lab_home_main_hed.setText("Profile")
        self.ui.lab_home_stat_hed.setText("Stat")

        ######### PAGE_BUG ############## BELOW DISPLAYS THE FUNCTION OF WIDGET, LABEL, PROGRESS BAR, E.T.C IN STACKEDWIDGET page_bug
        self.ui.bn_bug_start.clicked.connect(lambda: APFunction.addNumbers(self, self.ui.comboBox_bug.currentText(), True))

        # THIS CALLS A SIMPLE FUNCTION LOOPS THROW THE NUMBER FORWARDED BY THE COMBOBOX 'comboBox_bug' AND DISPLAY IN PROGRESS BAR
        #ALONGWITH MOVING THE PROGRESS CHUNK FROM 0 TO 100%

        #########PAGE CLOUD #############
        self.ui.bn_cloud_connect.clicked.connect(lambda: APFunction.cloudConnect(self))
        #self.ui.bn_cloud_clear.clicked.connect(lambda: self.dialogexec("Warning", "Do you want to save the file", "icons/1x/errorAsset 55.png", "Cancel", "Save"))
        self.ui.bn_cloud_clear.clicked.connect(lambda: APFunction.cloudClear(self))

        #########PAGE ANDROID WIDGET AND ITS STACKANDROID WIDGET PAGES
        self.ui.bn_android_contact.clicked.connect(lambda: UIFunction.androidStackPages(self, "page_contact"))
        self.ui.bn_android_game.clicked.connect(lambda: UIFunction.androidStackPages(self, "page_game"))
        self.ui.bn_android_clean.clicked.connect(lambda: UIFunction.androidStackPages(self, "page_clean"))
        self.ui.bn_android_world.clicked.connect(lambda: UIFunction.androidStackPages(self, "page_world"))

        
        ######ANDROID > PAGE CONTACT >>>>>>>>>>>>>>>>>>>>
        self.ui.bn_android_contact_delete.clicked.connect(lambda: self.dialogexec("Warning", "The Contact Infromtion will be Deleted, Do you want to continue.", "icons/1x/errorAsset 55.png", "Cancel", "Yes"))

        self.ui.bn_android_contact_edit.clicked.connect(lambda: APFunction.editable(self))

        self.ui.bn_android_contact_save.clicked.connect(lambda: APFunction.saveContact(self))

        #######ANDROID > PAGE GAMEPAD >>>>>>>>>>>>>>>>>>>
        self.ui.textEdit_gamepad.setVerticalScrollBar(self.ui.vsb_gamepad)   # SETTING THE TEXT FILED AREA A SCROLL BAR
        self.ui.textEdit_gamepad.setText("Type Here Something, or paste something here")

        ######ANDROID > PAGE CLEAN >>>>>>>>>>>>>>>>>>>>>>
        #NOTHING HERE
        self.ui.horizontalSlider_2.valueChanged.connect(lambda: print("Slider: Horizondal: ", self.ui.horizontalSlider_2.value())) #CHECK WEATHER THE SLIDER IS MOVED OR NOT
        self.ui.checkBox.stateChanged.connect(lambda: self.errorexec("Happy to Know you liked the UI", "icons/1x/smile2Asset 1.png", "Ok")) #WHEN THE CHECK BOX IS CHECKED IT ECECUTES THE ERROR BOX WITH MESSAGE.
        self.ui.checkBox_2.stateChanged.connect(lambda: self.errorexec("Even More Happy to hear this", "icons/1x/smileAsset 1.png", "Ok"))

        self.measurementGroups['Group1'].activate()
        """
        ######MEASUREMENTS  >>>>>>>>>>>>>>>>>>>>>>
        self.ui.bn_view_read_meas.clicked.connect(
            lambda: UIFunction.measurementStackPages(self, "page_read_measurement"))
        self.ui.bn_view_measurement.clicked.connect(
            lambda: UIFunction.measurementStackPages(self, "page_view_measurement"))
        self.ui.bn_view_parameters.clicked.connect(
            lambda: UIFunction.measurementStackPages(self, "page_view_parameters"))
        self.ui.bn_view_graph.clicked.connect(lambda: UIFunction.measurementStackPages(self, "page_view_graph"))

        ######MEASUREMENTS > PAGE READ MEASUREMENTS >>>>>>>>>>>>>>>>>>>>>>
        self.ui.bn_meas_open_folder.clicked.connect(lambda: APFunction.openFileDialog(self))
        self.ui.bn_meas_grp_rename.clicked.connect(lambda: APFunction.changeGroupName(self))
        self.ui.bn_read_meas.clicked.connect(lambda: APFunction.readGroup(self))
        self.ui.bn_graph_format.clicked.connect(lambda: APFunction.plotGraph(self))

        APFunction.updateMeasCombos(self)
        self.ui.bn_update_par_files.clicked.connect(lambda: APFunction.getParamFunFiles(self))
        self.ui.bn_update_hdr_files.clicked.connect(lambda: APFunction.getHeaderFiles(self))
        self.ui.bn_update_sfun_files.clicked.connect(lambda: APFunction.getSerFunctionFiles(self))
        self.ui.bn_update_graph_files.clicked.connect(lambda: APFunction.getGraphFiles(self))


        ######MEASUREMENTS > PAGE VIEW MEASUREMENTS >>>>>>>>>>>>>>>>>>>>>>
        self.ui.bn_meas_prev.clicked.connect(lambda: APFunction.viewPrevMeas(self))
        self.ui.bn_meas_next.clicked.connect(lambda: APFunction.viewNextMeas(self))
        self.ui.bn_show_meas.clicked.connect(lambda: APFunction.showMeas(self))

        ######MEASUREMENTS > PAGE VIEW GRAPHS >>>>>>>>>>>>>>>>>>>>>>
        self.ui.bn_graph_prev.clicked.connect(lambda: APFunction.viewPrevGraph(self))
        self.ui.bn_graph_next.clicked.connect(lambda: APFunction.viewNextGraph(self))
        self.ui.bn_show_graph.clicked.connect(lambda: APFunction.showGraph(self))

        #####FUNCTIONS > FUNCTION DEFINE >>>>>>>>>>>>>>>>>>>>>
        self.ui.bn_series_function_load.clicked.connect(lambda: APFunction.loadSeriesFunctions(self))
        self.ui.bn_parameter_function_load.clicked.connect(lambda: APFunction.loadParameterFunctions(self))

        self.ui.bn_series_function_save.clicked.connect(lambda: APFunction.saveSeriesFunctions(self))
        self.ui.bn_parameter_function_save.clicked.connect(lambda: APFunction.saveParameterFunctions(self))

        #####FUNCTIONS > FUNCTION VIEW >>>>>>>>>>>>>>>>>>>>>
        self.ui.bn_function_define.clicked.connect(
            lambda: UIFunction.stackedFunctionDefine(self, "page_function_define"))
        self.ui.bn_function_sett.clicked.connect(
            lambda: UIFunction.stackedFunctionDefine(self, "page_function_sett"))
        self.ui.bn_series_function.clicked.connect(
            lambda: UIFunction.stackedFunctionType(self, "page_series_function"))
        self.ui.bn_parameter_function.clicked.connect(
            lambda: UIFunction.stackedFunctionType(self, "page_parameter_function"))

        #####REPORTS > FUNCTION VIEW >>>>>>>>>>>>>>>>>>>>>
        self.ui.bn_report_pick.clicked.connect(
            lambda: UIFunction.stackedReportDefine(self, "page_report_pick"))
        self.ui.bn_report_sett.clicked.connect(
            lambda: UIFunction.stackedReportDefine(self, "page_report_sett"))
        self.ui.bn_report_create.clicked.connect(
            lambda: UIFunction.stackedReportDefine(self, "page_report_create"))
        self.ui.bn_excel_report.clicked.connect(
            lambda: UIFunction.stackedReportType(self, "page_excel_report"))
        self.ui.bn_word_report.clicked.connect(
            lambda: UIFunction.stackedReportType(self, "page_word_report"))


        """
        ##########PAGE: ABOUT HOME #############
        self.ui.text_about_home.setVerticalScrollBar(self.ui.vsb_about_home)
        self.ui.text_about_home.setText(aboutHome)
        """
    ################################################################################################################################

    """
    #-----> FUNCTION TO SHOW CORRESPONDING STACK PAGE WHEN THE ANDROID BUTTONS ARE PRESSED: CONTACT, GAME, CLOUD, WORLD
    # SINCE THE ANDROID PAGE AHS A SUB STACKED WIDGET WIT FOUR MORE BUTTONS, ALL THIS 4 PAGES CONTENT: BUTTONS, TEXT, LABEL E.T.C ARE INITIALIED OVER HERE. 
    def androidStackPages(self, page):
        #------> THIS LINE CLEARS THE BG COLOR OF PREVIOUS TABS
        for each in self.ui.frame_android_menu.findChildren(QFrame):
            each.setStyleSheet("background:rgb(51,51,51)")

        if page == "page_contact":
            self.ui.stackedWidget_android.setCurrentWidget(self.ui.page_android_contact)
            self.ui.lab_tab.setText("Android > Contact")
            self.ui.frame_android_contact.setStyleSheet("background:rgb(91,90,90)")

        elif page == "page_game":
            self.ui.stackedWidget_android.setCurrentWidget(self.ui.page_android_game)
            self.ui.lab_tab.setText("Android > GamePad")
            self.ui.frame_android_game.setStyleSheet("background:rgb(91,90,90)")

        elif page == "page_clean":
            self.ui.stackedWidget_android.setCurrentWidget(self.ui.page_android_clean)
            self.ui.lab_tab.setText("Android > Clean")
            self.ui.frame_android_clean.setStyleSheet("background:rgb(91,90,90)")

        elif page == "page_world":
            self.ui.stackedWidget_android.setCurrentWidget(self.ui.page_android_world)
            self.ui.lab_tab.setText("Android > World")
            self.ui.frame_android_world.setStyleSheet("background:rgb(91,90,90)")
    """

    def measurementStackPages(self, page):
        # ------> THIS LINE CLEARS THE BG COLOR OF PREVIOUS TABS
        for each in self.ui.frame_measurement_view.findChildren(QFrame):
            each.setStyleSheet("background:rgb(51,51,51)")

        if page == "page_read_measurement":
            self.ui.stackedWidget_measurements.setCurrentWidget(self.ui.page_read_measurements)
            self.ui.lab_tab.setText("Measurement > Read measurement")
            self.ui.frame_read_measurement.setStyleSheet("background:rgb(91,90,90)")

        elif page == "page_view_measurement":
            self.ui.stackedWidget_measurements.setCurrentWidget(self.ui.page_view_measurements)
            self.ui.lab_tab.setText("Measurement > View measurement")
            self.ui.frame_view_measurement.setStyleSheet("background:rgb(91,90,90)")

        elif page == "page_view_parameters":
            self.ui.stackedWidget_measurements.setCurrentWidget(self.ui.page_view_parameters)
            self.ui.lab_tab.setText("Measurement > View parameters")
            self.ui.frame_view_parameters.setStyleSheet("background:rgb(91,90,90)")


        elif page == "page_view_graph":
            self.ui.stackedWidget_measurements.setCurrentWidget(self.ui.page_view_graphs)
            self.ui.lab_tab.setText("Measurement > View graph")
            self.ui.frame_view_graph.setStyleSheet("background:rgb(91,90,90)")

    def stackedFunctionDefine(self, page):
        for each in self.ui.frame_function_view.findChildren(QFrame):
            each.setStyleSheet("background:rgb(51,51,51)")

        if page == "page_function_sett":
            self.ui.stackedFunction_define.setCurrentWidget(self.ui.page_function_sett)
            self.ui.lab_tab.setText("Function > Settings")
            self.ui.frame_function_sett_bn.setStyleSheet("background:rgb(91,90,90)")
        elif page == "page_function_define":
            self.ui.stackedFunction_define.setCurrentWidget(self.ui.page_function_define)
            self.ui.lab_tab.setText("Function > Define")
            self.ui.frame_function_define_bn.setStyleSheet("background:rgb(91,90,90)")
            #APFunction.setupFunctionItems(self)

    def stackedFunctionType(self, page):
        for each in self.ui.frame_function_type.findChildren(QFrame):
            each.setStyleSheet("background:rgb(51,51,51)")

        if page == "page_series_function":
            self.ui.sw_function_define.setCurrentWidget(self.ui.page_series_function_define)
            self.ui.sw_function_sett.setCurrentWidget(self.ui.page_series_function_sett)
            #self.ui.lab_tab.setText("Function > Settings")
            self.ui.frame_series_function.setStyleSheet("background:rgb(91,90,90)")
        elif page == "page_parameter_function":
            self.ui.sw_function_define.setCurrentWidget(self.ui.page_parameter_function_define)
            self.ui.sw_function_sett.setCurrentWidget(self.ui.page_parameter_function_sett)
            #self.ui.lab_tab.setText("Function > Settings")
            self.ui.frame_parameter_function.setStyleSheet("background:rgb(91,90,90)")

    def stackedReportDefine(self, page):
        for each in self.ui.frame_report_view.findChildren(QFrame):
            each.setStyleSheet("background:rgb(51,51,51)")

        if page == "page_report_pick":
            self.ui.stackedReport_define.setCurrentWidget(self.ui.page_report_pick)
            self.ui.lab_tab.setText("Report > Pick")
            self.ui.frame_report_pick_bn.setStyleSheet("background:rgb(91,90,90)")
        elif page == "page_report_sett":
            self.ui.stackedReport_define.setCurrentWidget(self.ui.page_report_define)
            self.ui.lab_tab.setText("Report > Settings")
            self.ui.frame_report_sett_bn.setStyleSheet("background:rgb(91,90,90)")
        elif page == "page_report_create":
            self.ui.stackedReport_define.setCurrentWidget(self.ui.page_report_create)
            self.ui.lab_tab.setText("Report > Create")
            self.ui.frame_report_create_bn.setStyleSheet("background:rgb(91,90,90)")

    def stackedReportType(self, page):
        for each in self.ui.frame_report_type.findChildren(QFrame):
            each.setStyleSheet("background:rgb(51,51,51)")

        if page == "page_excel_report":
            self.ui.sw_report_pick.setCurrentWidget(self.ui.page_excel_report_pick)
            self.ui.sw_report_define.setCurrentWidget(self.ui.page_excel_report_define)
            self.ui.sw_report_create.setCurrentWidget(self.ui.page_excel_report_create)
            # self.ui.lab_tab.setText("Function > Settings")
            self.ui.frame_excel_report.setStyleSheet("background:rgb(91,90,90)")
        elif page == "page_word_report":
            self.ui.sw_report_pick.setCurrentWidget(self.ui.page_word_report_pick)
            self.ui.sw_report_define.setCurrentWidget(self.ui.page_word_report_define)
            self.ui.sw_report_create.setCurrentWidget(self.ui.page_word_report_create)
            # self.ui.lab_tab.setText("Function > Settings")
            self.ui.frame_word_report.setStyleSheet("background:rgb(91,90,90)")




        # ADD A ADDITIONAL ELIF STATEMNT WITH THE SIMILAR CODE UP ABOVE FOR YOUR NEW SUBMENU BUTTON IN THE ANDROID STACK PAGE.

    ##############################################################################################################





    
#------> CLASS WHERE ALL THE ACTION OF TH SOFTWARE IS PERFORMED:
# THIS CLASS IS WHERE THE APPLICATION OF THE UI OR THE BRAINOF THE SOFTWARE GOES
# UNTILL NOW WE SEPCIFIED THE BUTTON CLICKS, SLIDERS, E.T.C WIDGET, WHOSE APPLICATION IS EXPLORED HERE. THOSE FUNCTION WHEN DONE IS 
# REDIRECTED TO THIS AREA FOR THE PROCESSING AND THEN THE RESULT ARE EXPOTED.
#REMEMBER THE SOFTWARE UI HAS A FUNCTION WHOSE CODE SHOULD BE HERE    
class APFunction():

    """
    #-----> ADDING NUMBER TO ILLUSTRATE THE CAPABILITY OF THE PROGRESS BAR WHEN THE 'START' BUTTON IS PRESSED
    def addNumbers(self, number, enable):
        if enable:
            lastProgress = 0
            for x in range(0, int(number), 1):
                progress = int((x/int(number))*100)
                if progress!=lastProgress:
                    self.ui.progressBar_bug.setValue(progress)
                    lastProgress = progress
            self.ui.progressBar_bug.setValue(100)
    ###########################

    #---> FUNCTION TO CONNECT THE CLOUD USING ADRESS AND RETURN A ERROR STATEMENT
    def cloudConnect(self):
        self.ui.bn_cloud_clear.setEnabled(False)
        textID = self.ui.line_cloud_id.text()
        textADRESS = self.ui.line_cloud_adress.text()
        if textID=='asd' and textADRESS=='1234':
            self.ui.line_cloud_adress.setText("")
            self.ui.line_cloud_id.setText("")
            self.ui.line_cloud_proxy.setText("Connection established")
        else:
            self.errorexec("Incorrect Credentials", "icons/1x/errorAsset 55.png", "Retry")

    def cloudClear(self):
        self.ui.line_cloud_proxy.setText("")
        self.ui.line_cloud_adress.setText("")
        self.ui.line_cloud_id.setText("")

    #-----> FUNCTION IN ACCOUNT OF CONTACT PAGE IN ANDROID MENU
    def editable(self):
        self.ui.line_android_name.setEnabled(True)
        self.ui.line_android_adress.setEnabled(True)
        self.ui.line_android_org.setEnabled(True)
        self.ui.line_android_email.setEnabled(True)
        self.ui.line_android_ph.setEnabled(True)

        self.ui.bn_android_contact_save.setEnabled(True)
        self.ui.bn_android_contact_edit.setEnabled(False)
        self.ui.bn_android_contact_share.setEnabled(False)
        self.ui.bn_android_contact_delete.setEnabled(False)

#-----> FUNCTION TO SAVE THE MODOFOED TEXT FIELD
    def saveContact(self):
        self.ui.line_android_name.setEnabled(False)
        self.ui.line_android_adress.setEnabled(False)
        self.ui.line_android_org.setEnabled(False)
        self.ui.line_android_email.setEnabled(False)
        self.ui.line_android_ph.setEnabled(False)

        self.ui.bn_android_contact_save.setEnabled(False)
        self.ui.bn_android_contact_edit.setEnabled(True)
        self.ui.bn_android_contact_share.setEnabled(True)
        self.ui.bn_android_contact_delete.setEnabled(True)
    """

    def drawGaph(self):
        import numpy as np
        t = np.linspace(0, 10, 501)
        self.graph.ax.clear()
        self.graph.format()
        self.graph.ax.plot(t, np.tan(t))
        self.graph.draw()

    def openFileDialog(self):
        folder = QFileDialog.getExistingDirectory(self, "Izberi mapo", self.ui.line_meas_folder.text())
        if folder != '':
            folderSrting = str(folder)
            self.ui.line_meas_folder.setText(folderSrting)
            self.GUIsett.setFolder(folderSrting)

    def changeGroupName(self):
        newName = self.ui.line_meas_grp_name.text()
        self.GUIsett.changeGroupName(newName)
        self.measurementGroups[self.GUIsett.currentGroup].changeGroupName(newName)
        self.excelGroupChooseItems.updateChooseCombos()

    def setParamTable(self):
        table = self.ui.table_parameters
        data = self.GUIsett.getParameters()
        APFunction.setTable(self, table, data, evaluate=True, idx="Sample")

    def setMeasTable(self):
        table = self.ui.table_meas
        data = self.GUIsett.getMeasurement()
        APFunction.setTable(self, table, data)
        if self.GUIsett.isDefined():
            self.ui.bn_meas_prev.setEnabled(True)
            self.ui.bn_meas_next.setEnabled(True)
        else:
            self.ui.bn_meas_prev.setEnabled(False)
            self.ui.bn_meas_next.setEnabled(False)
        name, prev, nex = self.GUIsett.getMeasName()
        if prev:
            self.ui.bn_meas_prev.setEnabled(False)
        if nex:
            self.ui.bn_meas_next.setEnabled(False)
        self.ui.line_view_meas.setText(name)

    def setTable(self, table, data=None, evaluate=False, idx=None):
        ts = TableSubst(table)
        table.keyPressEvent = ts.myKeyPressEvent
        if data is None:
            table.setRowCount(0)
            table.setColumnCount(0)
        else:
            dataShape = data.shape()


            # Row count
            table.setRowCount(dataShape[0])

            # Column count
            if idx:
                add = 1

            else:
                add = 0
            table.setColumnCount(dataShape[1] + add)

            if idx:
                table.setHorizontalHeaderItem(0, MyTableWidgetItem(idx))
                for row, index in enumerate(data.df.index):
                    tableItem = MyTableWidgetItem(str(index))
                    if evaluate:
                        if data.areValid(index):
                            tableItem.setBackground(QtGui.QColor(30, 130, 130))
                        else:
                            tableItem.setBackground(QtGui.QColor(130, 30, 30))
                    table.setItem(row, 0, tableItem)

            for i, entity in enumerate(data):
                col = i + add
                table.setHorizontalHeaderItem(col, MyTableWidgetItem(entity))
                for j, dPoint in enumerate(data[entity]):
            #table.setHorizontalHeaderItem(1, QTableWidgetItem("City"))
                    tableItem = MyTableWidgetItem(str(dPoint))
                    if evaluate:
                        if data[j][i].isValid():
                            tableItem.setBackground(QtGui.QColor(85, 145, 145))
                        else:
                            tableItem.setBackground(QtGui.QColor(145, 85, 85))
                    table.setItem(j, col, tableItem)

            # table.setItem(0, 1, QTableWidgetItem("Indore"))
            # table.setItem(1, 0, QTableWidgetItem("Alan"))
            # table.setItem(1, 1, QTableWidgetItem("Bhopal"))
            # table.setItem(2, 0, QTableWidgetItem("Arnavi"))
            # table.setItem(2, 1, QTableWidgetItem("Mandsaur"))

    def setMeasurementTab(self):
        APFunction.setMeasTable(self)
        APFunction.setParamTable(self)



    def readGroup(self):
        hdrFile = self.ui.combo_header.currentText()
        sfunFile = self.ui.combo_sfunction.currentText()
        if hdrFile:
            self.GUIsett.setHdrFile(hdrFile)
        # if sfunFile:
        self.GUIsett.setSerFunFile(sfunFile)
        self.GUIsett.readGroup(self)
        APFunction.setMeasTable(self)
        APFunction.readParam(self)
        APFunction.plotGraph(self)
        self.GUIsett.saveMeasUserPreset()


    def readParam(self):
        paramFile = self.ui.combo_parameter.currentText()
        if paramFile:
            self.GUIsett.setParamFile(paramFile)
        self.GUIsett.readParam()
        APFunction.setParamTable(self)

    def viewPrevMeas(self):
        self.GUIsett.viewPrevMeas()
        APFunction.setMeasTable(self)

    def viewNextMeas(self):
        self.GUIsett.viewNextMeas()
        APFunction.setMeasTable(self)

    def showMeas(self):
        measName = self.ui.line_view_meas.text()
        name, exists = self.GUIsett.getMeas(measName)
        if not exists:
            self.errorexec("Datoteka '{0}' v izbrani skupini ne obstaja".format(measName), "icons/1x/errorAsset 55.png", "OK")
            self.ui.line_view_meas.setText(name)
        else:
            APFunction.setMeasTable(self)

    def viewPrevGraph(self):
        self.GUIsett.viewPrevMeas()
        self.graph.setCurrIdx(self.GUIsett.getCurrIdx())
        APFunction.plotGraph(self)

    def viewNextGraph(self):
        self.GUIsett.viewNextMeas()
        self.graph.setCurrIdx(self.GUIsett.getCurrIdx())
        APFunction.plotGraph(self)

    def showGraph(self):
        measName = self.ui.line_view_graph.text()
        name, exists = self.GUIsett.getMeas(measName)
        if not exists:
            self.errorexec("Datoteka '{0}' v izbrani skupini ne obstaja".format(measName), "icons/1x/errorAsset 55.png", "OK")
            self.ui.line_view_graph.setText(name)
        else:
            self.graph.setCurrIdx(self.GUIsett.getCurrIdx())
            APFunction.plotGraph(self)

    @staticmethod
    def changeCombo(combo, fileFun, function=None, GUIobj=None):
        combo.clear()
        for file in fileFun(GUIobj):
            combo.addItem(QIcon(), file)
        if function is not None:
            combo.currentIndexChanged.connect(function)
            function(0)

    @staticmethod
    def setCombo(combo, text):
        index = combo.findText(text, QtCore.Qt.MatchFixedString)
        if index >= 0:
            combo.setCurrentIndex(index)

    def getParamFunFiles(self):
        APFunction.changeCombo(self.ui.combo_parameter,
                               Basic.getUserParFunFiles,
                               GUIobj=self.GUIsett.GUIfunObj)

    def getHeaderFiles(self):
        APFunction.changeCombo(self.ui.combo_header,
                               Basic.getUserHdrFiles,
                               GUIobj=self.GUIsett.GUIfunObj)

    def getSerFunctionFiles(self):
        APFunction.changeCombo(self.ui.combo_sfunction,
                               Basic.getUserSerFunFiles,
                               GUIobj=self.GUIsett.GUIfunObj)

    def getGraphFiles(self):
        APFunction.changeCombo(self.ui.combo_graph,
                               Basic.getUserGrfFiles,
                               GUIobj=self.GUIsett.GUIfunObj)

    def populateFunctionCombos(self):
        APFunction.populateSeriesFunctionCombo(self)
        APFunction.populateParameterFunctionCombo(self)

    def populateSeriesFunctionCombo(self):
        APFunction.changeCombo(self.ui.combo_series_function_load,
                               Basic.getUserSerFunFiles,
                               function=None,
                               GUIobj=self.GUIsett.GUIfunObj)

    def populateParameterFunctionCombo(self):
        APFunction.changeCombo(self.ui.combo_parameter_function_load,
                               Basic.getUserParFunFiles,
                               function=None,
                               GUIobj=self.GUIsett.GUIfunObj)

    def populateGroupChooseCombo(self, parent):
        APFunction.changeCombo(self.combo_excel_group_choose,
                               parent.GUIsett.getGroupNames,
                               function=None,
                               GUIobj=parent.GUIsett.GUIfunObj)

    def updateMeasCombos(self):
        APFunction.getParamFunFiles(self)
        APFunction.getHeaderFiles(self)
        APFunction.getSerFunctionFiles(self)
        APFunction.getGraphFiles(self)

    def plotGraph(self):
        if self.GUIsett.isDefined():
            self.ui.bn_graph_prev.setEnabled(True)
            self.ui.bn_graph_next.setEnabled(True)
        else:
            self.ui.bn_graph_prev.setEnabled(False)
            self.ui.bn_graph_next.setEnabled(False)
        name, prev, nex = self.GUIsett.getMeasName()
        if prev:
            self.ui.bn_graph_prev.setEnabled(False)
        if nex:
            self.ui.bn_graph_next.setEnabled(False)
        self.ui.line_view_graph.setText(name)
        graphFile = self.ui.combo_graph.currentText()
        if graphFile:
            self.GUIsett.setGraphFile(graphFile)
        graphFile = self.GUIsett.getGraphFile()
        if graphFile is not None:
            self.graph.setGraphFile(graphFile)
        mg = self.GUIsett.getMeasGroup()
        self.graph.plot(mg)

    @staticmethod
    def setComboBoxText(comboBox, text):
        index = comboBox.findText(text)
        comboBox.setCurrentIndex(index)

    def setGraphFileToCurr(self):
        graphFile = self.GUIsett.getGraphFile()
        APFunction.setComboBoxText(self.ui.combo_graph, graphFile)

    def setParamFileToCurr(self):
        paramFile = self.GUIsett.getParamFile()
        APFunction.setComboBoxText(self.ui.combo_parameter, paramFile)

    def setHdrFileToCurr(self):
        hdrFile = self.GUIsett.getHdrFile()
        APFunction.setComboBoxText(self.ui.combo_header, hdrFile)

    def setSerFileToCurr(self):
        serFile = self.GUIsett.getSerFunFile()
        APFunction.setComboBoxText(self.ui.combo_sfunction, serFile)

    def loadSeriesFile(self):
        functionFile = self.ui.combo_series_function_load.currentText()
        self.ui.line_series_function_name.setText(functionFile)
        self.loadSeriesFunctions(self, functionFile)

    def loadSeriesFunctions(self):
        functionFile = self.ui.combo_series_function_load.currentText()
        if functionFile:
            self.ui.line_series_function_name.setText(functionFile)
            self.seriesFunctionItems.resetLayout()
            self.seriesFunctionItems.populate(functionFile, self.GUIsett.GUIfunObj)

    def loadParameterFunctions(self):
        functionFile = self.ui.combo_parameter_function_load.currentText()
        if functionFile:
            self.ui.line_parameter_function_name.setText(functionFile)
            self.parameterFunctionItems.resetLayout()
            self.parameterFunctionItems.populate(functionFile, self.GUIsett.GUIfunObj)

    def saveSeriesFunctions(self):
        functionFileName = self.ui.line_series_function_name.text()
        self.seriesFunctionItems.saveAs(functionFileName, self.GUIsett.GUIfunObj)

    def saveParameterFunctions(self):
        functionFileName = self.ui.line_parameter_function_name.text()
        self.parameterFunctionItems.saveAs(functionFileName, self.GUIsett.GUIfunObj)

    def initializeUser(self):
        Basic.initiateUserFolders(self.GUIsett.GUIfunObj.username)





class GUIsettings(object):

    def __init__(self, user):
        self.user = user
        self.measGroupNames = {}
        self.measGroupSettings = {}
        self.groupMeasurements = {}
        self.currentGroup = 'Group1'
        self.GUIfunObj = GUIfunObj(self.user)
        #self.addMeasGroupSetting()

    def addMeasGroupSetting(self):

        groupName = 'Group{0}'.format(len(self.measGroupNames)+1)
        self.measGroupNames[groupName] = groupName
        self.measGroupSettings[groupName] = Basic.getGUIMeasPresets(self.GUIfunObj)
        self.groupMeasurements[groupName] = DataGroup(groupDir=self.measGroupSettings[groupName]["dataFolder"],
                                                      GUIobj=self.GUIfunObj)


    def setFolder(self, folder):
        self.measGroupSettings[self.currentGroup]["dataFolder"] = folder
        self.groupMeasurements[self.currentGroup].setFolder(folder)

    def setCurrentGroup(self, group):
        if group[:-1] == 'Group':
            if group[-1] in '123456':
                self.currentGroup = group

    def changeGroupName(self, groupName):
        self.measGroupNames[self.currentGroup] = groupName

    def readGroup(self, main):
        self.GUIfunObj.setProgressBar(main.ui.progressBar_read_meas)
        #self.GUIsett.setParamFile(paramFile)
        hdrFile = self.measGroupSettings[self.currentGroup]["headerFile"]
        sfunFile = self.measGroupSettings[self.currentGroup]["serFunFile"]
        self.groupMeasurements[self.currentGroup].reset()
        if hdrFile is not None:
            self.groupMeasurements[self.currentGroup].readPyro(hdrFile)
        if sfunFile:
            self.groupMeasurements[self.currentGroup].applySerFunctions(sfunFile)
        self.GUIfunObj.resetProgessBar()

    def readParam(self):
        paramFile = self.measGroupSettings[self.currentGroup]["parameterFile"]
        if paramFile is not None:
            self.groupMeasurements[self.currentGroup].getParameters(paramFile)

    def getMeasurement(self):
        if self.groupMeasurements[self.currentGroup].isDefined():
            currIdx = self.measGroupSettings[self.currentGroup]["currViewIdx"]
            return self.groupMeasurements[self.currentGroup][currIdx]
        else:
            return None

    def getMeasGroup(self):
        return self.groupMeasurements[self.currentGroup]


    def getParameters(self):
        if self.groupMeasurements[self.currentGroup].parametersDefined():
            return self.groupMeasurements[self.currentGroup]['parameters']
        else:
            return None

    def isDefined(self):
        return self.groupMeasurements[self.currentGroup].isDefined()

    def viewPrevMeas(self):
        if self.groupMeasurements[self.currentGroup].isDefined():
            self.measGroupSettings[self.currentGroup]["currViewIdx"] -= 1

    def viewNextMeas(self):
        if self.groupMeasurements[self.currentGroup].isDefined():
            self.measGroupSettings[self.currentGroup]["currViewIdx"] += 1

    def getCurrIdx(self):
        return self.measGroupSettings[self.currentGroup]["currViewIdx"]

    def getMeasName(self):
        next = False
        prev = False
        measName = None
        if self.groupMeasurements[self.currentGroup].isDefined():
            currIdx = self.measGroupSettings[self.currentGroup]["currViewIdx"]
            measNames = list(self.groupMeasurements[self.currentGroup])
            measName = measNames[currIdx]
            if currIdx+1 == len(measNames):
                next = True
            if currIdx == 0:
                prev = True
        return measName, prev, next

    def getMeas(self, measName):
        if measName in self.groupMeasurements[self.currentGroup]:
            idx = list(self.groupMeasurements[self.currentGroup]).index(measName)
            self.measGroupSettings[self.currentGroup]["currViewIdx"] = idx
            return measName, True
        else:
            currIdx = self.measGroupSettings[self.currentGroup]["currViewIdx"]
            measNames = list(self.groupMeasurements[self.currentGroup])
            return measNames[currIdx], False

    def setHdrFile(self, hdrFile):
        self.measGroupSettings[self.currentGroup]["headerFile"] = hdrFile

    def getHdrFile(self):
        return self.measGroupSettings[self.currentGroup]["headerFile"]

    def setSerFunFile(self, sfunFile):
        self.measGroupSettings[self.currentGroup]["serFunFile"] = sfunFile
        
    def getSerFunFile(self):
        return self.measGroupSettings[self.currentGroup]["serFunFile"]

    def setParamFile(self, paramFile):
        self.measGroupSettings[self.currentGroup]["parameterFile"] = paramFile

    def getParamFile(self):
        return self.measGroupSettings[self.currentGroup]["parameterFile"]

    def getCurrGroup(self):
        return self.currentGroup

    def setGraphFile(self, graphFile):
        self.measGroupSettings[self.currentGroup]["graphFile"] = graphFile

    def getGraphFile(self):
        return self.measGroupSettings[self.currentGroup]["graphFile"]

    def saveMeasUserPreset(self):
        Basic.saveGUIMeasUserPreset(self.measGroupSettings[self.currentGroup], self.GUIfunObj)

    def getGroupNames(self, GUIobj):
        return [self.measGroupNames[group] for group in self.measGroupNames]



class GUIfunObj(object):

    def __init__(self, username):
        self.username = username
        self.error = None
        self.warnings = []
        self.text = Text()
        self.progGoal = 100
        self.currProgress = 0
        self.progressBar = None

    def setLan(self, lan):
        self.text.setLan(lan)

    def checkError(self):
        out = self.error
        self.error = None
        return out

    def checkWarnings(self):
        if self.checkWarnings:
            out = self.warnings.copy()
            self.warnings = []
            return out

    def storeWarnings(self, warnings):
        self.warnings += warnings

    def storeWarning(self, warning):
        self.warnings.append(warning)

    def storeError(self, error):
        self.error = error

    def getWarning(self, warnType, *args):
        self.storeWarning(self.text.getWarning(warnType, *args))

    def getError(self, errType, *args):
        self.storeError(self.text.getError(errType, *args))

    def checkErrors(self):
        error = self.error
        self.error = None
        return error

    def moveErrorsToWarnings(self):
        error = self.checkErrors()
        if error is not None:
            self.storeWarning(error)

    def resetProgessBar(self):
        if self.progressBar is not None:
            self.progressBar.setValue(0)

    def setProgressBar(self, progressBar):
        self.progressBar = progressBar



    def getProgressBar(self, iterable):
        class ProgressBar:
            def __init__(self, iterable, progressBar):
                self.iterable = iterable
                self.progressBar = progressBar

            def __iter__(self):
                class ProgressIterator:
                    def __init__(self, iterator, progressBar):
                        self.currProgress = 0
                        self.progressBar = progressBar
                        self.progGoal = len(iterator)
                        self.iterator = iterator.__iter__()

                    def __next__(self):
                        o = 'out'
                        if self.progressBar is not None:
                            o = 'in'
                            progress = int((self.currProgress / self.progGoal) * 100)
                            self.progressBar.setValue(progress)
                        self.currProgress += 1
                        return self.iterator.__next__()

                return ProgressIterator(self.iterable, self.progressBar)

        return ProgressBar(iterable, self.progressBar)

class GUIgraph():

    def __init__(self, main):
        class showNext(ToolBase):
            """Show next graph."""
            default_keymap = 'N'
            description = 'Show next graph'

            def trigger(self, *args, **kwargs):
                self.main.GUIsett.viewNextMeas()
                mg = self.main.GUIsett.getMeasGroup()
                self.main.graph.plot(mg)
        #plt.tight_layout()
        self.graph = GraphWrapper(GUIobj=main.GUIsett.GUIfunObj, mlObj=self)
        self.layout = QtWidgMat.QVBoxLayout(main.ui.frame_view_graphs)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.figure = plt.Figure()
        self.figure.subplots_adjust(bottom=0.15)

        self.bacgroundHex = QColor.fromRgb(qRgb(91, 90, 90)).name()
        self.markingsHex = QColor.fromRgb(qRgb(51, 51, 51)).name()
        self.figure.patch.set_facecolor(self.bacgroundHex)
        self.static_canvas = FigureCanvas(self.figure)

        self.toolbar = NavigationToolbar(self.static_canvas, main.ui.page_view_graphs)
        self.toolbar.setStyleSheet("""QTabWidget::pane {border: none;background: rgb(91, 90, 90);;}
                                        QTabBar::tab {background: rgb(51, 51, 51); border: 1px solid lightgray;
                                                        border-color: rgb(51, 51, 51);padding: 5px; }
                                       QTabBar::tab:selected {background: rgb(70, 70, 70);margin-bottom: -1px;}""")
        #self.toolbar.add_tool('Next', showNext, main=main)
        self.layout.addWidget(self.toolbar)
        self.layout.addWidget(self.static_canvas)
        # self.addToolBar(NavigationToolbar(static_canvas, frame))
        self.ax = self.static_canvas.figure.subplots()
        # self._static_ax.style.use('ggplot')
        self.format()


        self.ax.tick_params(colors=self.markingsHex)
        self.ax.xaxis.label.set_color(self.markingsHex)
        self.ax.yaxis.label.set_color(self.markingsHex)
        self.ax2 = None

    def format(self):
        self.ax.patch.set_facecolor(self.bacgroundHex)
        self.ax.grid(color=self.markingsHex)
        self.ax.spines['top'].set_color(self.markingsHex)
        self.ax.spines['bottom'].set_color(self.markingsHex)
        self.ax.spines['left'].set_color(self.markingsHex)
        self.ax.spines['right'].set_color(self.markingsHex)

    def draw(self):
        self.ax.figure.canvas.draw()
        if self.ax2 is not None:
            self.ax2.figure.canvas.draw()

    def addYAxis(self):
        if self.ax2 is not None:
            self.ax2.remove()
        self.ax2 = self.ax.twinx()
        self.ax2.tick_params(colors=self.markingsHex)
        self.ax2.xaxis.label.set_color(self.markingsHex)
        self.ax2.yaxis.label.set_color(self.markingsHex)

    def plot(self, dgObj):
        #plt.tight_layout()
        self.graph.draw(dgObj)

    def setGraphFile(self, graphFile):
        self.graph.setGraphSettings(graphFile)

    def setCurrIdx(self, idx):
        self.graph.setCurrIdx(idx)





class MeasurementGroup():

    def __init__(self, main, name, button, frame):
        self.main = main
        self.button = button
        self.frame = frame
        self.name = name
        self.addIcon = QIcon("icons/1x/addAsset.png")  #TODO popravi na Path.icon
        self.noIcon = QIcon()
        self.active = False
        self.button.clicked.connect(lambda: self.clicked())

    def activate(self):
        self.button.setText(self.name)
        self.button.setIcon(self.noIcon)
        self.active = True
        self.main.GUIsett.addMeasGroupSetting()
        self.changeData()

    def enableNext(self):
        enable = False
        for group in self.main.measurementGroups:
            if group == self.name:
                enable = True
            elif enable:
                self.main.measurementGroups[group].enable()
                break

    def enable(self):
        self.button.setIcon(self.addIcon)
        self.button.setEnabled(True)


    def clicked(self):
        self.main.GUIsett.setCurrentGroup(self.name)
        for each in self.main.ui.frame_measurement_menu.findChildren(QFrame):
            each.setStyleSheet("background:rgb(51,51,51)")
        self.frame.setStyleSheet("background:rgb(91,90,90)")
        if self.active:
            self.changeData()
        else:
            self.activate()
            self.enableNext()

    def changeData(self):
        self.main.ui.line_meas_folder.setText(self.main.GUIsett.measGroupSettings[self.name]["dataFolder"])
        self.main.ui.line_meas_grp_name.setText(self.main.GUIsett.measGroupNames[self.name])
        self.main.excelGroupChooseItems.updateChooseCombos()
        APFunction.setMeasTable(self.main)
        APFunction.setParamTable(self.main)
        APFunction.setHdrFileToCurr(self.main)
        APFunction.setSerFileToCurr(self.main)
        APFunction.setParamFileToCurr(self.main)
        APFunction.setGraphFileToCurr(self.main)
        APFunction.plotGraph(self.main)


        # TODO dodaj da nastavi ostale stvari

    def changeGroupName(self, name):
        self.button.setText(name)

class SortFilterProxyModel(QtCore.QSortFilterProxyModel):

    def lessThan(self, left_index, right_index):

        left_var = left_index.data(Qt.EditRole)
        right_var = right_index.data(Qt.EditRole)

        try:
            return float(left_var) < float(right_var)
        except (ValueError, TypeError):
            pass
        return left_var < right_var

class MyTableWidgetItem(QTableWidgetItem):
    def __lt__(self, other):
        if isinstance(other, QTableWidgetItem):
            #my_value, my_ok = self.data(Qt.EditRole).toInt()
            #other_value, other_ok = other.data(Qt.EditRole).toInt()

            #if ( my_ok and other_ok ):
            return Basic.lessThan(self.text(), other.text())

        return super(MyTableWidgetItem, self).__lt__(other)



class TableSubst(object):
    def __init__(self, table):
        self.table = table

    def myKeyPressEvent(self, event):
        if event:
            #super().keyPressEvent(event)
            if event.key() == Qt.Key_C and (event.modifiers() & Qt.ControlModifier):
                self.copied_cells = sorted(self.table.selectedIndexes())
                copiedText = ""
                sep = ""
                prevRow = None
                headerIdx = []
                for cell in self.copied_cells:
                    row = cell.row()
                    column = cell.column()
                    if column not in headerIdx:
                        headerIdx.append(column)
                    if not prevRow is None:
                        if prevRow != row:
                            sep = '\n'
                            prevRow = row
                        else:
                            sep = '\t'
                    else:
                        prevRow = row

                    text = self.table.item(row, column).text()
                    copiedText += sep + text
                headerIdx = sorted(headerIdx)
                header = ""
                for idx in headerIdx:
                    header += self.table.horizontalHeaderItem(idx).text() + '\t'
                header = header[:-1] + '\n'
                allText = (header+copiedText).replace('.', ',')
                cb = QApplication.clipboard()
                cb.clear(mode=cb.Clipboard)
                cb.setText(allText, mode=cb.Clipboard)


class FunctionItems(object):

    def __init__(self, parent, ftype="s"):
        self.functionItems = []
        self.ftype = ftype
        self.parent = parent
        if ftype == "s":
            self.addFrame = self.parent.frame_series_function_define_add
            self.blankFrame = self.parent.frame_series_function_item_blank
            self.loadSettingsFile = Basic.loadUserSerFunFile
            self.functions = Interface.getSeriesFunctions
            self.getFilePath = Paths.getUserSerFunFile
            self.p = False
        elif ftype == "p":
            self.addFrame = self.parent.frame_parameter_function_define_add
            self.blankFrame = self.parent.frame_parameter_function_item_blank
            self.loadSettingsFile = Basic.loadUserParFunFile
            self.functions = Interface.getParameterFunctions
            self.getFilePath = Paths.getUserParFunFile
            self.p = True
        self.vl_function_define_add = QVBoxLayout(self.addFrame)
        self.vl_function_define_add.setSpacing(3)
        self.vl_function_define_add.setContentsMargins(0, 0, 0, 0)
        self.initializeFrame()

    def initializeFrame(self):
        self.addInactiveFunction()

    def resetLayout(self):
        for functionItem in self.functionItems:
            self.vl_function_define_add.removeWidget(functionItem[0])
            #sip.delete(functionItem[0])
            #functionItem[0] = None
        self.functionItems = []

    def delete(self, a, functionItem):
        n = self.functionItems.index(functionItem)
        self.vl_function_define_add.removeWidget(functionItem[0])
        #functionItem[0].setParent(None)
        del self.functionItems[n]
        # for i, functionItem in enumerate(self.functionItems):
        #     print("i:", i)
        #     functionItem[1].bn_function_delete.clicked.disconnect()
        #     functionItem[1].bn_function_delete.clicked.connect(lambda: self.delete(i))
        #     functionItem[1].cb_evaluate.stateChanged.disconnect()
        #     functionItem[1].cb_evaluate.stateChanged.connect(lambda: self.functionEvaluation(i))


    def addInactiveFunction(self):
        qsw = QStackedWidget()
        qsw.setFrameShape(QFrame.NoFrame)
        qsw.setFrameShadow(QFrame.Plain)
        qsw.setLineWidth(0)
        fi = Ui_StackedWidget()
        fi.setupUi(qsw)
        qsw.setCurrentWidget(fi.page_add)
        self.functionItems.append((qsw, fi))
        self.functionItems[-1][1].bn_add_function.clicked.connect(lambda: self.addBlankFunction())
        n = len(self.functionItems) - 1
        self.functionItems[-1][1].bn_function_delete.clicked.connect(lambda a=False, fi=self.functionItems[-1]:
                                                                     self.delete(a, fi))
        self.functionEvaluation(False, self.functionItems[-1])
        self.functionItems[-1][1].cb_evaluate.stateChanged.connect(lambda a=False, fi=self.functionItems[-1]:
                                                                   self.functionEvaluation(a, fi))
        self.functionItems[-1][1].cb_evaluate.setEnabled(self.p)
        self.functionItems[-1][1].combo_rounding_function.setEnabled(self.p)
        self.functionItems[-1][1].line_series_function_name.setEnabled(not self.p)
        # for qsw, fi in self.functionItems:
        #     self.vl_function_define_add.addWidget(qsw)
        self.vl_function_define_add.addWidget(qsw)

    def addActiveFunction(self):
        qsw = QStackedWidget()
        qsw.setFrameShape(QFrame.NoFrame)
        qsw.setFrameShadow(QFrame.Plain)
        qsw.setLineWidth(0)
        fi = Ui_StackedWidget()
        fi.setupUi(qsw)
        qsw.setCurrentWidget(fi.page_define)
        self.functionItems.append((qsw, fi))
        n = len(self.functionItems) - 1
        self.functionItems[-1][1].bn_function_delete.clicked.connect(lambda a=False, fi=self.functionItems[-1]:
                                                                     self.delete(a, fi))
        self.functionEvaluation(False, self.functionItems[-1])
        self.setFunctionTypes(self.functionItems[-1][1])
        self.functionItems[-1][1].cb_evaluate.stateChanged.connect(lambda a=False, fi=self.functionItems[-1]:
                                                                     self.functionEvaluation(a, fi))
        #self.functionItems[-1][1].bn_add_function.clicked.connect(lambda: self.addBlankFunction())
        # for qsw, fi in self.functionItems:
        #     self.vl_function_define_add.addWidget(qsw)
        self.functionItems[-1][1].cb_evaluate.setEnabled(self.p)
        self.functionItems[-1][1].combo_rounding_function.setEnabled(self.p)
        self.functionItems[-1][1].line_series_function_name.setEnabled(not self.p)
        self.vl_function_define_add.addWidget(qsw)


    def addBlankFunction(self):
        functionItem = self.functionItems[-1][1]
        self.functionItems[-1][0].setCurrentWidget(functionItem.page_define)
        self.setFunctionName(functionItem, len(self.functionItems))
        self.setFunctionTypes(functionItem)
        self.changeFunctionType(fi=functionItem)
        self.blankFrame.setParent(None)
        self.addInactiveFunction()
        self.vl_function_define_add.addWidget(self.blankFrame)

    def setFunctionName(self, functionItem, n):
        #n = self.functionItems.index(functionItem)
        if type(n) == int:
            name = 'Funckija {}'.format(n)
        else:
            name = str(n)
        functionItem.groupBox.setTitle(name)
        functionItem.line_function_name.setText(name)

    def setFunctionTypes(self, functionItem):
        APFunction.changeCombo(functionItem.combo_function_type,
                               self.functions,
                               function=lambda x, fi=functionItem: self.changeFunctionType(x, fi=fi),
                               GUIobj=None)

    def changeFunctionType(self, *args, **kwargs):
        functionItem = kwargs["fi"]
        functionName = functionItem.combo_function_type.currentText()
        mandatory = Interface.getMandatorySett(self.ftype, functionName)
        functionItem.line_function_par1.setEnabled("feature1" in mandatory)
        functionItem.line_function_par2.setEnabled("feature2" in mandatory)
        functionItem.line_function_val1.setEnabled("value1" in mandatory)
        functionItem.line_function_val2.setEnabled("value2" in mandatory)

    def functionEvaluation(self, a, functionItem):
        cb = functionItem[1].cb_evaluate.isChecked()
        functionItem[1].line_function_min.setEnabled(cb)
        functionItem[1].line_function_max.setEnabled(cb)


    def populate(self, functionName, GUIobj=None):
        functions = self.loadSettingsFile(functionName, GUIobj)
        self.resetLayout()
        for functionName in functions:
            self.addDefinedFunction(functionName, functions[functionName])
        self.addInactiveFunction()
        self.vl_function_define_add.addWidget(self.blankFrame)



    def addDefinedFunction(self, functionName, content):
        self.addActiveFunction()
        functionItem = self.functionItems[-1][1]
        self.setFunctionName(functionItem, functionName)
        if "function" in content:
            APFunction.setCombo(functionItem.combo_function_type, content["function"])
        if "parameters" in content:
            if "feature1" in content["parameters"]:
                functionItem.line_function_par1.setText(content["parameters"]["feature1"])
            if "value1" in content["parameters"]:
                functionItem.line_function_val1.setText(str(content["parameters"]["value1"]))
            if "feature2" in content["parameters"]:
                functionItem.line_function_par2.setText(content["parameters"]["feature2"])
            if "value2" in content["parameters"]:
                functionItem.line_function_val2.setText(str(content["parameters"]["value2"]))
            if "rounding" in content["parameters"]:
                rounding = ['1', '0,1', '0,01', '0,001', '0,0001']
                if 0 <= int(content["parameters"]["rounding"]) < 5:
                    APFunction.setCombo(functionItem.combo_rounding_function,
                                        rounding[int(content["parameters"]["rounding"])])
            if "newName" in content["parameters"]:
                functionItem.line_series_function_name.setText(content["parameters"]["newName"])
        if "evaluation" in content:
            functionItem.cb_evaluate.setChecked(True)
            if "min" in content["evaluation"]:
                functionItem.line_function_min.setText(str(content["evaluation"]["min"]))
            if "max" in content["evaluation"]:
                functionItem.line_function_max.setText(str(content["evaluation"]["max"]))
        else:
            functionItem.cb_evaluate.setChecked(False)


    def toJson(self):
        content = {}
        for functionItem in self.functionItems[:-1]:
            fi = functionItem[1]
            functionParam = {"feature1": (fi.line_function_par1, "s"),
                             "value1": (fi.line_function_val1, "f"),
                             "feature2": (fi.line_function_par2, "s"),
                             "value2": (fi.line_function_val2, "f"),
                             }

            functionName = fi.line_function_name.text()
            content[functionName] = {}
            content[functionName]["function"] = fi.combo_function_type.currentText()
            content[functionName]["parameters"] = {}
            for fParam in functionParam:
                if functionParam[fParam][0].isEnabled():
                    text = functionParam[fParam][0].text()
                    if functionParam[fParam][1] == "f":
                        if Basic.isNumericalText(text):
                            content[functionName]["parameters"][fParam] = float(text)
                        else:
                            content[functionName]["parameters"][fParam] = 0
                    else:
                        content[functionName]["parameters"][fParam] = text
                if fi.combo_rounding_function.isEnabled():
                    idx = fi.combo_rounding_function.currentIndex()
                    if idx:
                        content[functionName]["parameters"]["rounding"] = idx - 1
                if fi.line_series_function_name.isEnabled():
                    newName = fi.line_series_function_name.text()
                    if newName:
                        content[functionName]["parameters"]["newName"] = newName
            if fi.cb_evaluate.isChecked():
                evaluationParam = {"min": fi.line_function_min,
                                   "max": fi.line_function_max,}
                content[functionName]["evaluation"] = {}
                for eParam in evaluationParam:
                    text = evaluationParam[eParam].text()
                    if Basic.isNumericalText(text):
                        content[functionName]["evaluation"][eParam] = float(text)
        return content

    def saveAs(self, fileName, GUIobj):
        filePath = self.getFilePath(GUIobj.username, fileName)
        Basic.saveJsonFile(filePath, self.toJson(), GUIobj)
        #print(filePath)


class GroupCooseItems(object):

    def __init__(self, parent, rtype="e"):
        self.groupChooseItems = []
        self.rtype = rtype
        self.parent = parent
        if rtype == "e":
            self.addFrame = self.parent.ui.frame_excel_report_create_sa#frame_excel_report_create_item_create
            self.blankFrame = self.parent.ui.frame_excel_report_create_item_create
            self.loadSettingsFile = Basic.loadUserExcReportFile
            #self.functions = Interface.getSeriesFunctions
            self.getFilePath = Paths.getUserExcelReportFile
            self.w = False
        # elif rtype == "w":
        #     self.addFrame = self.parent.ui.frame_word_report_create_sa  # frame_excel_report_create_item_create
        #     self.blankFrame = self.parent.ui.frame_word_report_create_item_create
        #     self.loadSettingsFile = Basic.loadUserWordReportFile
        #     # self.functions = Interface.getSeriesFunctions
        #     self.getFilePath = Paths.getUserExcelReportFile
        #     self.w = False
        self.vl_report_group_choose = self.parent.ui.verticalLayout_excel_create
        self.initializeFrame()
        #self.vl_function_define_add.setSpacing(3)
        #self.vl_function_define_add.setContentsMargins(0, 0, 0, 0)

    def initializeFrame(self):
        self.addGroups(1)

    def resetLayout(self):
        self.blankFrame.setParent(None)
        for groupChooseItem in self.groupChooseItems:
            self.vl_report_group_choose.removeWidget(groupChooseItem[0])
            #sip.delete(functionItem[0])
            #functionItem[0] = None
        self.groupChooseItems = []

    # def delete(self, a, functionItem):
    #     n = self.functionItems.index(functionItem)
    #     self.vl_function_define_add.removeWidget(functionItem[0])
    #     #functionItem[0].setParent(None)
    #     del self.functionItems[n]
        # for i, functionItem in enumerate(self.functionItems):
        #     print("i:", i)
        #     functionItem[1].bn_function_delete.clicked.disconnect()
        #     functionItem[1].bn_function_delete.clicked.connect(lambda: self.delete(i))
        #     functionItem[1].cb_evaluate.stateChanged.disconnect()
        #     functionItem[1].cb_evaluate.stateChanged.connect(lambda: self.functionEvaluation(i))


    def addGroups(self, n):
        self.resetLayout()
        self.vl_report_group_choose = QVBoxLayout(self.addFrame)
        self.vl_report_group_choose.setSpacing(3)
        self.vl_report_group_choose.setContentsMargins(0, 0, 0, 0)
        for i in range(n):
            qsw = QStackedWidget()
            qsw.setFrameShape(QFrame.NoFrame)
            qsw.setFrameShadow(QFrame.Plain)
            qsw.setLineWidth(0)
            gci = rgi_StacketWidget()
            gci.setupUi(qsw)
            qsw.setCurrentWidget(gci.page_group_choose)
            self.setGroupName(gci, i+1)
            self.groupChooseItems.append((qsw, gci))
            self.vl_report_group_choose.addWidget(qsw)
        self.vl_report_group_choose.addWidget(self.blankFrame)
        self.updateChooseCombos()
        if n > 0:
            self.parent.ui.bn_excel_report_create.setEnabled(True)
        else:
            self.parent.ui.bn_excel_report_create.setEnabled(False)

        # self.functionItems[-1][1].bn_add_function.clicked.connect(lambda: self.addBlankFunction())
        # n = len(self.functionItems) - 1
        # self.functionItems[-1][1].bn_function_delete.clicked.connect(lambda a=False, fi=self.functionItems[-1]:
        #                                                              self.delete(a, fi))
        # self.functionEvaluation(False, self.functionItems[-1])
        # self.functionItems[-1][1].cb_evaluate.stateChanged.connect(lambda a=False, fi=self.functionItems[-1]:
        #                                                            self.functionEvaluation(a, fi))
        # self.functionItems[-1][1].cb_evaluate.setEnabled(self.p)
        # self.functionItems[-1][1].combo_rounding_function.setEnabled(self.p)
        # self.functionItems[-1][1].line_series_function_name.setEnabled(not self.p)
        # # for qsw, fi in self.functionItems:
        # #     self.vl_function_define_add.addWidget(qsw)
        # self.vl_report_group_choose.addWidget(qsw)

    def updateChooseCombos(self):
        for groupChooseItem in self.groupChooseItems:
            APFunction.populateGroupChooseCombo(groupChooseItem[1], self.parent)

    # def addActiveFunction(self):
    #     qsw = QStackedWidget()
    #     qsw.setFrameShape(QFrame.NoFrame)
    #     qsw.setFrameShadow(QFrame.Plain)
    #     qsw.setLineWidth(0)
    #     fi = Ui_StackedWidget()
    #     fi.setupUi(qsw)
    #     qsw.setCurrentWidget(fi.page_define)
    #     self.functionItems.append((qsw, fi))
    #     n = len(self.functionItems) - 1
    #     self.functionItems[-1][1].bn_function_delete.clicked.connect(lambda a=False, fi=self.functionItems[-1]:
    #                                                                  self.delete(a, fi))
    #     self.functionEvaluation(False, self.functionItems[-1])
    #     self.setFunctionTypes(self.functionItems[-1][1])
    #     self.functionItems[-1][1].cb_evaluate.stateChanged.connect(lambda a=False, fi=self.functionItems[-1]:
    #                                                                  self.functionEvaluation(a, fi))
    #     #self.functionItems[-1][1].bn_add_function.clicked.connect(lambda: self.addBlankFunction())
    #     # for qsw, fi in self.functionItems:
    #     #     self.vl_function_define_add.addWidget(qsw)
    #     self.functionItems[-1][1].cb_evaluate.setEnabled(self.p)
    #     self.functionItems[-1][1].combo_rounding_function.setEnabled(self.p)
    #     self.functionItems[-1][1].line_series_function_name.setEnabled(not self.p)
    #     self.vl_report_group_choose.addWidget(qsw)
    #
    #
    # def addBlankFunction(self):
    #     functionItem = self.functionItems[-1][1]
    #     self.functionItems[-1][0].setCurrentWidget(functionItem.page_define)
    #     self.setFunctionName(functionItem, len(self.functionItems))
    #     self.setFunctionTypes(functionItem)
    #     self.changeFunctionType(fi=functionItem)
    #     self.blankFrame.setParent(None)
    #     self.addInactiveFunction()
    #     self.vl_report_group_choose.addWidget(self.blankFrame)

    def setGroupName(self, groupChooseItem, n):
        #n = self.functionItems.index(functionItem)
        if type(n) == int:
            name = 'Skupina {}:'.format(n)
        else:
            name = str(n)
        #groupChooseItem.groupBox.setTitle(name)
        groupChooseItem.lab_excel_report_load.setText(name)


######################################################################################################################