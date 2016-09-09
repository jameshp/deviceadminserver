@echo off
if '%1'=='' goto usage

:loop 

python C:\ktcsrc\Projects\SmartphoneBasedTolling\SmartToll\trunk\Tools\message_creator\encode_base64.py %1

shift
if '%1'=='' goto end

goto loop

:usage
echo Usage:
echo    %0 [filename]
pause

:end
pause