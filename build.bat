call activateVenv.bat & pyinstaller DataProcessorGUI.spec -y & pyinstaller Updater.spec -y & python moveCompiled.py

