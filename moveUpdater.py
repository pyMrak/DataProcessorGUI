import shutil
import os
import Paths
#from DataProcessor import Basic




for file in ["Updater.exe"]:
    shutil.copy(Paths.join(Paths.compiledUpdater, file), Paths.sourceUpdaterExe)

for file in ["Updater.exe"]:
    shutil.copy(Paths.join(Paths.compiledUpdater, file), "C:/Users/andmra2/Desktop/DataProcessor/Updater.exe")

# if os.path.exists(Paths.sourcePath):
#     shutil.rmtree(Paths.sourcePath)

#os.mkdir(Paths.sourcePath)
#shutil.move(Paths.compiledMain, Paths.downloadPath)


# for folder in ["icons", "exe", "DataProcessor/Text"]:
#     shutil.copytree(folder, Paths.sourcePath+'/'+folder, dirs_exist_ok=True)

# shutil.copy(Paths.configFile, Paths.getConfigFile(Paths.sourcePath))
# for file in ["debug.log"]:
#     shutil.copy(file, Paths.sourcePath + "/" + file)

for folder in ["dist", "build"]:
    shutil.rmtree(folder)


