@echo off
if '%1'=='' goto usage

:loop 

C:\ktcsrc\Projects\SmartphoneBasedTolling\SmartToll\trunk\Tools\message_creator\app_cfg.py spbt_config CONVERT %1 --in-format=json --out-format=dat

shift
if '%1'=='' goto end

goto loop

:usage
echo Usage:
echo    %0 [filename]
pause

:end
pause