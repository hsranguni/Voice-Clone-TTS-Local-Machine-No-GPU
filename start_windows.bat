@echo off
REM We bypass the double-click shutdown bug by forcing a new command window to open
REM that is explicitly told to stay open using CMD /K

echo Re-launching securely to keep window active...
start cmd /k "echo Starting setup... & echo. & cmd_runner.bat"
exit
