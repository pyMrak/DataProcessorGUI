from DataProcessor.Paths import *

mainExe = "DataProcessor.exe"
updaterExe = "Updater.exe"
sourceUpdaterExe = sourcePath + updaterExe
sourceMainExe = sourcePath + mainExe

debugLog = sourcePath + "debug.log"

compiledUpdater = r"dist\Updater"
compiledMain = r"dist\DataProcessor"

icons = "icons/1x/"
mainIcon = icons + "mainIcon.png"


def getLocalMainExe(localPath):
    if localPath:
        return localPath + "\\" + mainExe
    else:
        return mainExe

def getLocalUpdaterExe(localPath):
    if localPath:
        return localPath + "\\" + updaterExe
    else:
        return updaterExe

def getConfigFile(path):
    if path:
        return path + "/" + configFile
    else:
        return configFile


