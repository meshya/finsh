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


_here_path_argv = Path(os.getcwd())
if len(sys.argv) == 2 :_here_path_argv = Path(os.path.abspath(sys.argv[1]))
log_file_path = Path(dirname(__file__))/'log.txt'
_listen = '0.0.0.0:8053'
for argv in sys.argv[1:]:
    if re.match(r'^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}(:\d{1,6})?$',argv):
        _listen = f"{argv}"
_port = re.findall(r'.+:(\d{1,6})',_listen) [0]
with open(log_file_path,'wb+') as f:
    f.write(b'')
    f.close()


try:
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
    print(c.yellow(str(_here_path_argv)+':'))
    print("_____________________________")
    list_dir(Path(_here_path_argv))
    print()
except:
    print()
    print(f"{c.red('Exiting before start...')}")
    exit()

try:

    w = 0
    print(f'Running server {c.blue("."*w)}   ',end='\r')

    process = subprocess.Popen([
    "env" ,"python" ,
    str(Path(dirname(__file__))/'finsh.py'), 
    str(_here_path_argv),
    "--listen",
    _listen ,
#    ">",
#    str(Path(dirname(__file__))/'log.txt')
    ] 
    ,shell=False, 
    universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    logfile = open(log_file_path,'r')

    def shell_iterator ():
        def readline():
            #return process.stdout.readline() #type: ignore
            return logfile.readline() #type: ignore
        while True :
            #print('\nintro')
            line = readline() #type: ignore
            #print('outro')
            #print('\n'+line)
            if line != '':
                yield line.strip()
            time.sleep(0.05)

    def sleep_iter (sl):
        while True :
            yield None
            time.sleep(sl)

    import requests #type: ignore
    for _ in sleep_iter(0.3):
        try :
            res = requests.get(f'http://localhost:{_port}/core/test',verify=False,timeout=0.3)
            if str(res.status_code)[0] == '2':
                break
        except:
            pass

        print(f'Running server {c.blue("."*(w%4))}   ',end='\r')

        
        w += 1
    print(f"listenning on {c.blue(_listen)}")
    print()

    for log in shell_iterator():
        file_name,size = re.findall(r'^FILE:(.+):\]',log)[0], re.findall(r'SIZE:(.+):\}$',log)[0]
        out = f"{c.yellow('Upload')+c.red(' ->')} {c.green(file_name)}   ({c.blue(size)})"
        print(out)
except:
    print()
    print(f"{c.red('Exiting...')}")
    exit()