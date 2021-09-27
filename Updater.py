from os import getcwd, path, system
import shutil
import sys
import subprocess
#from PySide2.QtWidgets import QApplication, QMessageBox

from DataProcessor import Basic
import Paths
#from main import errorUi


def main(localDir, debug=False):
    localContent = None
    sourceContent = None
    if Paths.sourcePath:
        sourceDir = Paths.sourcePath
    else:
        sourceDir = getcwd()
    if path.exists(Paths.getConfigFile(sourceDir)):
        sourceContent = Basic.loadJsonFile(Paths.getConfigFile(sourceDir))
    if path.exists(Paths.getConfigFile(localDir)):
        localContent = Basic.loadJsonFile(Paths.getConfigFile(localDir))
    if sourceContent:
        if checkForUpdates(localContent, sourceContent, debug):
            update(sourceDir, localDir)
    runlocal(localDir, debug)

def checkForUpdates(localContent, sourceContent, debug=False):
    currVersion = "0"
    # if Paths.isfile(Paths.debugLog):
    #     out = Basic.loadJsonFile(Paths.debugLog)
    # out["check for updates"] = True
    # Basic.saveJsonFile(Paths.debugLog, out)
    if localContent:
        if "version" in localContent:
            currVersion = localContent["version"]
    if "version" in sourceContent:
        sourceVersion = sourceContent["version"]
        currVersionInt = 0
        sourceVersionInt = 0
        for i, s in enumerate(currVersion.split('.')):
            currVersionInt += int(s)*10**(6-2*i)
        for i, s in enumerate(sourceVersion.split('.')):
            sourceVersionInt += int(s) * 10 ** (6 - 2 * i)
        # if Paths.isfile(Paths.debugLog):
        #     out = Basic.loadJsonFile(Paths.debugLog)
        # out["source version"] = sourceVersionInt
        # out["local version"] = currVersionInt
        # Basic.saveJsonFile(Paths.debugLog, out)
        if debug:
            print("source version:", sourceVersionInt)
            print("local version:", currVersionInt)
        elif sourceVersionInt > currVersionInt:
            return True

def update(sourceDir, localDir):
    print("Updating... May take a minute.")
    # if Paths.isfile(Paths.debugLog):
    #     out = Basic.loadJsonFile(Paths.debugLog)
    # out["update"] = True
    # Basic.saveJsonFile(Paths.debugLog, out)
    # app = QApplication(sys.argv)
    # app = errorUi()
    # errorUi.errorConstrict(app, "Data Processor is downloading updates. This could take a few minutes.",
    #                        "icons/1x/infoAsset_50.png", "OK")
    # app.exec_()
    try:
        shutil.copytree(sourceDir, localDir, dirs_exist_ok=True)
    except:
        return


def runlocal(localDir, debug=False):
    # if Paths.isfile(Paths.debugLog):
    #     out = Basic.loadJsonFile(Paths.debugLog)
    # out["runlocal"] = True
    # Basic.saveJsonFile(Paths.debugLog, out)
    if debug:
        system("debugMain.bat")
    else:
        a = subprocess.Popen([Paths.getLocalMainExe(localDir), "2512"])

if __name__ == "__main__":
    cd = path.dirname(path.realpath(__file__))
    #content = Basic.loadJsonFile(Paths.getSettingsFile(cd))
    if len(sys.argv) > 1:
        if sys.argv[1] != "checkSource":
            print("Checking for updates...")
            if sys.argv[-1] == "update":
                subprocess.Popen([Paths.sourceUpdaterExe, "checkSource", cd])
            elif sys.argv[-1] == "debug":
                if Paths.isfile(Paths.sourceUpdaterExe):
                    print("Would run:", Paths.sourceUpdaterExe)
                    main("", True)
                else:
                    print('Source updater does not exists:', Paths.sourceUpdaterExe)
            else:
                out = {
                    "cd": cd,
                    "source": Paths.sourcePath
                }
                Basic.saveJsonFile(Paths.debugLog, out)
        else:
            if sys.argv[-1] == "update":
                runlocal(cd)
            else:
                localDir = sys.argv[-1]
                main(localDir)
    else:
        print("Checking for updates...")
        if cd == Paths.sourcePath:
            runlocal(Paths.sourcePath)
        else:
            subprocess.Popen([Paths.sourceUpdaterExe, "checkSource", cd])
    #sys.exit(0)
