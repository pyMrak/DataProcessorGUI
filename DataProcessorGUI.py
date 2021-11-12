from PySide2.QtWidgets import QApplication, QDialog
from main import MainWindow, errorUi
import sys
import subprocess
import os

#from libs.logger import newLog
from libs import Permission, Login
import Paths


debug = True
debugUpdater = False
version = "1.0"

if __name__ == "__main__":
    if ("2512" in sys.argv) or (not debugUpdater and debug):
        app = QApplication(sys.argv)
        allowed, online = Permission.check(version)
        log = None

        if allowed:
            window = None
            if debug:
                window = MainWindow(version, "debug")#program = GUI.Main(version, online, None)
            else:
                log = Login.Login()
                if log.exec_() == QDialog.Accepted:
                    window = MainWindow(version, Login.logMod.username)
            if window:
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
    else:
        if debugUpdater:
            print("would run:", Paths.updaterExe)
            os.system("debugUpdater.bat")
            #a = subprocess.Popen(["debug.bat", "none"])
            #print(a)
        else:
            a = subprocess.Popen([Paths.updaterExe, "update"])
        sys.exit(0)


