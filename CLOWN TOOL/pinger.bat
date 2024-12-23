@echo off
color D
title IP PINGER
set /p ip="Enter the ip: "

:loop
start /b ping %ip% -n 1 -l 65500 -w 1 >nul
echo Pinging %ip%
goto loop

