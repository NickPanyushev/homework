#!/usr/bin/python3.4

import os.path
import subprocess
import shutil
import argparse

parser = argparse.ArgumentParser(description="SAD shows the status of the file"
                                             " and it's last changes"
                                             " status are saved at ~/.sad folder")

parser.add_argument("action",
                    choices=['store', 'diff'],
                    type=str,
                    help="-store - saves the current status"
                         " of file or directory "
                         "-diff - shows the differences with last change")
parser.add_argument("path",
                    type=str,
                    help="Path to the directory with saved file")

args = parser.parse_args()
action = args.action
path = args.path

if action == "store":
    sad_path = os.path.expanduser('~/.sad')  # преобразуем в абсолютный адрес без ~
    if os.path.isfile(path):  # проверяем, является ли файлом
        if not os.path.exists(sad_path):
            os.makedirs(sad_path)
        shutil.copy(path, sad_path)  # копируем файл в папку ~/.sad
        print('copied successfully')
    else:
        print("err: argument is a folder")

elif action == "diff":
    file_name = path.split('/')[-1]  # извлекаем имя из пути
    diff_args = "diff " + path + " ~/.sad/" + file_name
    print(subprocess.call(diff_args, shell=True))
