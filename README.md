# bf_to_alist
使用webdav协议，自动将本地路径上传到指定路径。
注意：会自动在D盘建立一个bfsoft文件夹，然后把日志放在log那边，如果没D盘估计会报错，嘿嘿
|  使用方法   | 推荐度  |
|  ----  | ----  |
| py运行  | 推荐 |
| exe传参  | 单元格 |
| bat脚本  | 推荐 |

# 使用原因
办公室内，想把某一个电脑的某个文件夹路径备份到alist系统内（其实就是另一个电脑的某个文件夹）由于我们办公室都是小白，资料也不想通过网络共享给办公室人员（要保密），所以就找到了alist，可以ip+端口，隐蔽性高一点。当然如果遇到了那个特别强的电脑大佬，那也没办法。

# 传递方法
bat脚本
----------

@echo off
setlocal

:: 设置默认参数
set USERNAME=zzz
set PASSWORD=123456
set WEBDAV_URL=http://192.168.31.152:5244/dav
set LOCAL_FOLDER_PATH=D:\pytestaaa\kmi
set TOKEN = SCT228306TA-ftvYRo6Cb

:: 检查命令行参数，并覆盖默认值
if "%~1" neq "" set USERNAME=%~1
if "%~2" neq "" set PASSWORD=%~2
if "%~3" neq "" set WEBDAV_URL=%~3
if "%~4" neq "" set LOCAL_FOLDER_PATH=%~4
if "%~5" neq "" set TOKEN=%~5

:: 启动备份程序
start your_script.exe --username "%USERNAME%" --password "%PASSWORD%" --webdav_url "%WEBDAV_URL%" --local_folder_path "%LOCAL_FOLDER_PATH%" --token "%TOKEN%"

endlocal

----------