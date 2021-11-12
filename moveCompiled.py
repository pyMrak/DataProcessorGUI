import shutil
import os
import Paths
import DataProcessorGUI
#from DataProcessor import Basic




for file in ["Updater.exe"]:
    shutil.copy(Paths.join(Paths.compiledUpdater, file), Paths.compiledMain)

if not DataProcessorGUI.debug:
    if os.path.exists(Paths.sourcePath):
        shutil.rmtree(Paths.sourcePath)

    #os.mkdir(Paths.sourcePath)
    shutil.move(Paths.compiledMain, Paths.downloadPath)

    for folder in ["icons", "exe", "DataProcessor/Text"]:
        shutil.copytree(folder, Paths.sourcePath+'/'+folder, dirs_exist_ok=True)

    shutil.copy(Paths.configFile, Paths.getConfigFile(Paths.sourcePath))
    for file in []:
        shutil.copy(file, Paths.sourcePath + "/" + file)

    for folder in ["dist", "build"]:
        shutil.rmtree(folder)


