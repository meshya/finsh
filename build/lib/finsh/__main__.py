from genericpath import isfile
import os
import subprocess
import sys
from posixpath import dirname
from pathlib import Path
import re
import time
try:
    from .sad.conf import c
except:
    from sad.conf import c


_here_path_argv = dirname(__file__)
if len(sys.argv) == 2 :_here_path_argv = sys.argv[1]
_listen = '0.0.0.0:8000'
for argv in sys.argv[1:]:
    if re.match(r'^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}(:\d{1-6})?$',argv):
        _listen = f"{argv}"


def list_dir(main_path,path=None,prefix="|"):
    if path is None :
        path = main_path
    
    url = f'http://{_listen}/'

    ismain = main_path == path

    for file_path in os.listdir(path) :
        file_path = path/file_path
        file_name = os.path.basename(file_path)
        if not ismain :
            mol_path = re.findall(f"{str(main_path)}[/,\\\\](.+)", str(path)) [0]
            file_name = mol_path+'/'+file_name #type: ignore

        if isfile(file_path):
            file_info = f"{prefix}{c.green(file_name)} {c.red('->')} {c.blue(url)}{c.blue(file_name)}"
            print(file_info)
        else :
            folder_info = f"{prefix}{c.yellow(file_name)}{c.yellow(':')}"
            print(folder_info)
            list_dir(main_path,path=file_path,prefix=prefix+'  |')
print()
print(c.yellow(_here_path_argv+':'))
print("_____________________________")
list_dir(Path(_here_path_argv))
print()
w = 0
print(f'Running server {c.blue("."*w)}   ',end='\r')
try:
    process = subprocess.Popen([f"env python {Path(dirname(__file__))/'finsh.py'}  {_here_path_argv} --listen {_listen}"] ,shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    def shell_iterator ():
        while True :
            line = process.stdout.readline() #type: ignore
            if line != '':
                yield line.strip()
            time.sleep(0.05)

    for log in shell_iterator():
        if _listen in log :
            break
        print(f'Running server {c.blue("."*w)}   ',end='\r')
        time.sleep(1)
        if w < 3 :
            w += 1
        else:
            w = 0
    print(f"listenning on {c.blue(_listen)}")
    print()

    for log in shell_iterator():
        if re.match(r'^__finshlognow__:::.*$',log):
            _log = log[(len('__finshlognow__:::.')-1):]
            file_name,size = re.findall(r'^FILE:(.+):\]',_log)[0], re.findall(r'SIZE:(.+):\}$',log)[0]
            out = f"Request {c.green(file_name)}   ({c.blue(size)})"
            print(out)
except:
    print()
    print(f"{c.red('Exiting...')}")
    exit()