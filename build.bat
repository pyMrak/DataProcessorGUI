call activateVenv.bat & pyinstaller BuildTools/DataProcessorGUI.spec -y & pyinstaller BuildTools/Updater.spec -y & python moveCompiled.py

