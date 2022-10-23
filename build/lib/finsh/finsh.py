#!env python3
from posixpath import dirname
import sys
import os

import time


i = 0
def exec ():
    
    path = sys.argv[1]

    os.environ.setdefault('FINSH_HERE',path)


    #time.sleep(10)
    try:
        from .manage import main
    except:
        from manage import main

    _listen = '0.0.0.0:8000'

    if '--listen' in sys.argv :
        _listen = sys.argv[sys.argv.index('--listen') + 1]

    argv = (
        __file__,
        'runserver',
        _listen
    )
    main(argv)

if __name__ == "__main__" :
    exec()
