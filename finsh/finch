#!env python3
from posixpath import dirname
import sys
import os

i = 0
def exec ():
    if len(sys.argv) == 2 :
        path = sys.argv[1]
    else:
        path = dirname(__file__)
    os.environ.setdefault('FINCH_HERE',path)
    
    try:
        from .manage import main
    except:
        from manage import main

    argv = [
        __file__,
        'runserver',
        '0.0.0.0:8000'
    ]
    main(argv)

if __name__ == "__main__" :
    exec()
