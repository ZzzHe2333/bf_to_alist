import os
import requests
from requests.auth import HTTPBasicAuth
import time
import argparse
from datetime import datetime

class bfyfb():
    def __init__(self, username, password, webdav_url, token=None):
        self.username = username
        self.password = password
        self.webdav_url = webdav_url
        self.token = token if token is not None else "S"  # 在此处设置默认token
        self.beifen_msg = ""
        self.wenjian_up_ok = 0
        self.wenjian_up_error = 0

    def upload_file(self, local_file_path):
        file_name = os.path.basename(local_file_path)  # 确保 file_name 已被初始化
        try:
            # 使用webdav协议上传
            with open(local_file_path, 'rb') as file:
                response = requests.put(
                    f"{self.webdav_url}/{file_name}",
                    data=file,
                    auth=HTTPBasicAuth(self.username, self.password)
                )
            # 检查响应状态码
            if response.status_code == 201:
                self.beifen_msg += f"备份成功-->{file_name}\n\n"
                self.wenjian_up_ok += 1
                print(f"[上传成功]{file_name}")
            else:
                self.beifen_msg += f"备份失败-->{file_name}\n\n"
                self.wenjian_up_error += 1
                print(f"[上传失败]{file_name}")
        except requests.exceptions.RequestException as e:
            self.beifen_msg += f"备份失败-->{file_name} - {str(e)}\n\n"
            self.wenjian_up_error += 1
            print(f"[上传失败]{file_name} - {str(e)}")

    def get_recent_files(self, folder_path, days=7):
        # 获取最近days天修改过的文件列表
        current_time = time.time()  # 当前时间
        recent_files = []
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                file_mtime = os.path.getmtime(file_path)
                if current_time - file_mtime < days * 86400:  # 86400 秒 = 1 天
                    recent_files.append(file_path)  # 添加至上传列表
        return recent_files

    def upload_recent_files(self, folder_path, days=7):
        recent_files = self.get_recent_files(folder_path, days)
        for file_path in recent_files:
            self.upload_file(file_path)
        self.beifen_msg = f"成功: {self.wenjian_up_ok} 个\n失败: {self.wenjian_up_error} 个\n\n" + self.beifen_msg

    def serverchan(self, title, msg="", token=None):
        return

    def save_to_log(self, message, log_folder=None):
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        log_file_name = f"bfsoft_{current_time}.txt"
        if log_folder is None:
            log_folder = r'D:\bfsoft\log'
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)
        log_file_path = os.path.join(log_folder, log_file_name)
        with open(log_file_path, 'w') as log_file:
            log_file.write(message + '\n')

def main(username, password, webdav_url, local_folder_path, token):
    # 实例化类
    backup = bfyfb(username, password, webdav_url, token)
    # 上传最近7天修改过的文件
    backup.upload_recent_files(local_folder_path)
    # 发送通知
    # backup.serverchan("备份情况", backup.beifen_msg)
    # 保存日志
    backup.save_to_log(backup.beifen_msg)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Backup script")
    parser.add_argument("--username", default="zzz", help="WebDAV server username")
    parser.add_argument("--password", default="123456", help="WebDAV server password")
    parser.add_argument("--webdav_url", default="http://192.168.31.152:5244/dav", help="WebDAV server URL")
    parser.add_argument("--local_folder_path", default=r"D:\pytestaaa\kmi", help="Path to the local folder to back up")
    parser.add_argument("--token", default=None, help="ServerChan token")

    try:
        args = parser.parse_args()
        main(args.username, args.password, args.webdav_url, args.local_folder_path, args.token)
    except SystemExit as e:
        if e.code == 2:
            parser.print_help()
        else:
            raise
