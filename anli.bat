@echo off
setlocal

:: 设置默认参数
set USERNAME=zzz
set PASSWORD=123456
set WEBDAV_URL=http://192.168.31.152:5244/dav
set LOCAL_FOLDER_PATH=D:\pytestaaa\kmi
set TOKEN=SCT228306TA-ftvYRo6C

:: 检查命令行参数，并覆盖默认值
if "%~1" neq "" set USERNAME=%~1
if "%~2" neq "" set PASSWORD=%~2
if "%~3" neq "" set WEBDAV_URL=%~3
if "%~4" neq "" set LOCAL_FOLDER_PATH=%~4
if "%~5" neq "" set TOKEN=%~5

:: 启动备份程序
start ./zdbf.exe --username "%USERNAME%" --password "%PASSWORD%" --webdav_url "%WEBDAV_URL%" --local_folder_path "%LOCAL_FOLDER_PATH%" --token "%TOKEN%"

endlocal
