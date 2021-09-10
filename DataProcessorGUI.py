from PySide2.QtWidgets import QApplication, QDialog
from main import MainWindow, errorUi
import sys

#from libs.logger import newLog
from libs import Permission, Login
from DataProcessor import Paths


debug = False
version = "1.0"

##############################
# version = 'ver2_4'
# app = QApplication(argv)
# alowed, online = Permission.check(version)
# log = None
#
# if __name__ =="__main__":
#     if alowed:
#         if debug:
#             program = GUI.Main(version, online, None)
#         else:
#             log = login.Login()
#             if log.exec_() == QDialog.Accepted:
#                 #print(login.logMod.username, login.logMod.userType)
#                 program = GUI.Main(version, online, login.logMod)
#
#     else:
#         zapisi = newLog(version, log)
#         zapisi.writeLocation('Not alowed ', version)
#         GUI.permissionError(app, 'Verzija ' + version.replace('_', '.').strip('ver') +
#                             ' je zastarela ali pa nimate dostopa do mreže.\nNove verzije so dostopne na '+
#                             globalPaths.path.download+'.')
#     sysExit(app.exec_())
#############################


if __name__ == "__main__":
    app = QApplication(sys.argv)
    allowed, online = Permission.check(version)
    log = None
    if allowed:
        if debug:
            window = MainWindow(version, "debug")#program = GUI.Main(version, online, None)
        else:
            log = Login.Login()
            if log.exec_() == QDialog.Accepted:
                #print(login.logMod.username, login.logMod.userType)
                window = MainWindow(version, Login.logMod.username)
        window.show()
    else:
        #zapisi = newLog(version, log)
        #zapisi.writeLocation('Not alowed ', version)
        app = errorUi()
        heading = ('Verzija ' + version +
                   ' je zastarela ali pa nimate dostopa do mreže.\nNove verzije so dostopne na '+
                   Paths.downloadPath+'.')
        errorUi.errorConstrict(app, heading, "exe/icons/1x/errorAsset 55.png", "OK")
    sys.exit(app.exec_())
        #GUI.permissionError(app, )


